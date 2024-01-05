import csv
from project import (
    Book,
    view_books,
    view_cart,
    get_numeric_input,
    ask_shopping_preference,
    load_inventory,
    save_cart,
    load_cart,
    save_inventory,
    add_to_cart,
    place_order,
)

# Sample inventory data
sample_inventory_data = [
    ["Book ID", "Title", "Author", "Price"],
    [1, "Test Book 1", "Test Author 1", 9.99],
]

# Sample cart data
sample_cart_data = [["Book ID", "Title", "Price"], [1, "Test Book 1", 9.99]]


# Test for viewing books
def test_view_books(capsys):
    inventory = [
        Book(book_id=1, title="Test Book 1", author="Test Author 1", price=9.99)
    ]

    # Capture the printed output
    view_books(inventory)
    captured = capsys.readouterr()

    # Check if expected strings are present in the captured output
    assert "Book ID" in captured.out
    assert "Test Book 1" in captured.out
    assert "Test Author 1" in captured.out
    assert "9.99" in captured.out


# Test for viewing the cart
def test_view_cart(capsys):
    cart = [Book(book_id=1, title="Test Book 1", author="", price=9.99)]

    # Capture the printed output
    view_cart(cart)
    captured = capsys.readouterr()

    # Check if expected strings are present in the captured output
    assert "Book ID" in captured.out
    assert "Test Book 1" in captured.out
    assert "9.99" in captured.out


# Test for getting numeric input
def test_get_numeric_input(capsys, monkeypatch):
    # Set the user input to "42"
    monkeypatch.setattr("builtins.input", lambda _: "42")

    # Call the function and capture printed output
    result = get_numeric_input("Enter a number: ")

    # Check if the result is of type int and equal to 42
    assert isinstance(result, int)
    assert result == 42


# Test for asking shopping preference
def test_ask_shopping_preference(monkeypatch):
    # Set the user input to "y"
    monkeypatch.setattr("builtins.input", lambda _: "y")

    # Call the function
    result = ask_shopping_preference()

    # Check if the result is True
    assert result is True


# Test for loading inventory
def test_load_inventory(tmp_path, monkeypatch):
    # Create a sample CSV file with inventory data
    csv_file = tmp_path / "test_inventory.csv"
    with open(csv_file, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(sample_inventory_data)

    # Set the filename to the created CSV file
    monkeypatch.setattr("builtins.input", lambda _: str(csv_file))

    # Call the function
    result = load_inventory()

    # Check if the result is a non-empty list
    assert isinstance(result, list)


# Test for saving and loading cart
def test_save_and_load_cart(tmp_path):
    # Create a sample cart and save it
    original_cart = [Book(book_id=1, title="Test Book 1", author="", price=9.99)]
    save_cart(original_cart, "test_user")

    # Load the saved cart
    loaded_cart = load_cart("test_user")

    # Check if the loaded cart is the same as the original cart
    assert len(loaded_cart) == len(original_cart)

    for loaded_book, original_book in zip(loaded_cart, original_cart):
        assert loaded_book.book_id == original_book.book_id
        assert loaded_book.title == original_book.title
        assert loaded_book.price == original_book.price


# Test for saving and loading inventory
def test_save_and_load_inventory(tmp_path):
    # Create a sample inventory and save it
    original_inventory = [
        Book(book_id=1, title="Test Book 1", author="Test Author 1", price=9.99)
    ]
    save_inventory(original_inventory, "test_inventory.csv")

    # Load the saved inventory
    loaded_inventory = load_inventory("test_inventory.csv")

    # Check if the loaded inventory is the same as the original inventory
    assert len(loaded_inventory) == len(original_inventory)

    for loaded_book, original_book in zip(loaded_inventory, original_inventory):
        assert loaded_book.book_id == original_book.book_id
        assert loaded_book.title == original_book.title
        assert loaded_book.author == original_book.author
        assert loaded_book.price == original_book.price


# Test for adding a book to the cart
def test_add_to_cart(tmp_path):
    # Create a sample inventory and save it
    inventory = [
        Book(book_id=1, title="Test Book 1", author="Test Author 1", price=9.99)
    ]
    save_inventory(inventory, "test_inventory.csv")

    # Add a book to the cart
    cart = []
    add_to_cart(cart, inventory, "test_user", 1)

    # Check if the cart contains the added book
    assert len(cart) == 1
    assert cart[0].book_id == 1


# Test for placing an order
def test_place_order(capsys):
    # Create a sample cart
    cart = [Book(book_id=1, title="Test Book 1", author="", price=9.99)]

    # Place an order with the sample cart
    place_order(cart, "test_user")

    # Capture the printed output
    captured = capsys.readouterr()

    # Check if expected strings are present in the captured output
    assert "Order Summary" in captured.out
    assert "Test Book 1" in captured.out
    assert "9.99" in captured.out
    assert "Total Price" in captured.out
    assert "Order placed successfully" in captured.out
