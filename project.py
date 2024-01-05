import csv
from tabulate import tabulate
import os
import shutil


class Book:
    def __init__(self, book_id, title, author, price):
        # Constructor for the Book class
        self.book_id = book_id
        self.title = title
        self.author = author
        self.price = price


def load_inventory(filename="books.csv"):
    inventory = []
    if os.path.exists(filename):
        with open(filename, "r") as file:
            reader = csv.reader(file)
            header = next(reader)
            if header != ["Book ID", "Title", "Author", "Price"]:
                print("Invalid CSV file format. Exiting.")
                return inventory
            for row in reader:
                if len(row) == 4 and row[0].isdigit():
                    book_id, title, author, price = row
                    inventory.append(Book(int(book_id), title, author, float(price)))
                else:
                    print("Invalid data in CSV file. Exiting.")
                    return inventory
    return inventory


def save_cart(cart, username):
    # Save the user's cart to a CSV file
    cart_filename = f"cart-{username}.csv"
    with open(cart_filename, "w", newline="") as file:
        writer = csv.writer(file)
        for book in cart:
            writer.writerow([book.book_id, book.title, book.price])


def load_cart(username):
    # Load the user's cart from a CSV file
    cart_filename = f"cart-{username}.csv"
    cart = []
    if os.path.exists(cart_filename):
        with open(cart_filename, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                book_id, title, price = row
                cart.append(Book(int(book_id), title, "", float(price)))
    return cart


def save_inventory(inventory, filename="books.csv"):
    # Save the inventory to a CSV file
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Book ID", "Title", "Author", "Price"])
        for book in inventory:
            writer.writerow([book.book_id, book.title, book.author, book.price])


def add_to_cart(cart, inventory, user, book_id):
    # Add a selected book to the user's cart
    selected_book = next((book for book in inventory if book.book_id == book_id), None)
    if selected_book and selected_book.price > 0:
        if any(book.book_id == selected_book.book_id for book in cart):
            print(f"{selected_book.title} is already in your cart.")
        else:
            cart.append(selected_book)
            print(f"{selected_book.title} added to your cart.")
            selected_book.price -= 1
            save_inventory(inventory)
            save_cart(cart, user)
    elif selected_book:
        print("Book is out of stock. Please select another book.")
    else:
        print("Book not found. Please enter a valid Book ID.")
    return selected_book


def place_order(cart, user):
    # Place an order with the items in the user's cart
    if not cart:
        print("Your cart is empty. Add books before placing an order.")
        return

    headers = ["Book ID", "Title", "Price"]
    order_data = [(book.book_id, book.title, f"${book.price}") for book in cart]
    print("\nOrder Summary:")
    print(tabulate(order_data, headers=headers, tablefmt="pretty"))

    total_price = sum(book.price for book in cart)
    print(f"\nTotal Price: ${total_price}")
    print(f"Order placed successfully. Thank you, {user}!")

    cart.clear()
    save_cart(cart, user)
    cart_filename = f"cart-{user}.csv"
    if os.path.exists(cart_filename):
        os.remove(cart_filename)


def get_numeric_input(prompt, error_message="Invalid input. Please enter a number."):
    # Get numeric input from the user
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print(error_message)


def ask_shopping_preference():
    # Ask the user if they want to continue shopping
    while True:
        response = input("Do you want to shop more? (y/n): ").lower()
        if response == "y":
            return True
        elif response == "n":
            return False
        else:
            print("Invalid response. Please enter 'y' or 'n'.")


def view_books(inventory):
    # Display the list of books in the inventory
    headers = ["Book ID", "Title", "Author", "Price"]
    book_data = [
        (book.book_id, book.title, book.author, f"${book.price}") for book in inventory
    ]
    print(tabulate(book_data, headers=headers, tablefmt="pretty"))


def view_cart(cart):
    # Display the contents of the user's cart
    headers = ["Book ID", "Title", "Price"]
    cart_data = [(book.book_id, book.title, f"${book.price}") for book in cart]
    print(tabulate(cart_data, headers=headers, tablefmt="pretty"))


def main(input_function=input):
    # Main function for the online bookstore
    inventory = load_inventory()
    print("WELCOME TO THE VIRTUAL BOOKSTORE !!!")
    user = input("Enter your name: ").strip()

    while True:
        cart = load_cart(user)
        print("*" * 50)
        print(
            "Option 1 - View books in the bookstore \nOption 2 - View books in your cart\nOption 3 - Add books to your cart\nOption 4 - Place an order\nOption 5 - Exit the bookstore"
        )
        print("*" * 50)
        choice = get_numeric_input(
            "Enter your option (1-5): ",
            "Invalid choice. Please enter a number from 1 to 5.",
        )

        if choice == 1:
            view_books(inventory)
        elif choice == 2:
            view_cart(cart)
        elif choice == 3:
            while True:
                book_id = get_numeric_input(
                    "Enter the Book ID of the book you want to add to your cart (or 0 to go back): "
                )
                if book_id == 0:
                    break
                add_to_cart(cart, inventory, user, book_id)
        elif choice == 4:
            place_order(cart, user)
            save_inventory(inventory)
            if not ask_shopping_preference():
                print("Exiting the Online Bookstore. Goodbye!")
                return
        elif choice == 5:
            print("Exiting the Online Bookstore. Goodbye!")
            return
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")


if __name__ == "__main__":
    try:
        shutil.copyfile("./books_backup.csv", "./books.csv")
        print("Books.csv successfully restored from backup.")
    except FileNotFoundError:
        # Handle the case where books_backup.csv doesn't exist yet
        print("No backup found. Starting with a fresh books.csv.")
    main()
