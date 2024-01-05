# Virtual Bookstore

#### Video Demo: [https://youtu.be/2xXmWSgm4FA]

#### Description

The Virtual Bookstore is a command-line application implemented in Python. It allows users to browse a collection of books, add them to a shopping cart, and place orders. The Virtual Bookstore maintains an inventory of books and user-specific shopping carts. Data is stored in CSV files.

## Files

- `project.py`: Main script containing the Virtual Bookstore functionality.
- `test_project.py`: Test script for testing the functionality of the Virtual Bookstore.
- `books.csv`: Sample inventory data in CSV format.
- `books_backup.csv`: Backup file of `books.csv`
- `requirements.txt`: The file which contains the list of required libraries to be installed before running the script
- `README.md`: The file that explains the project.

## Project Requirements

- The project must be implemented in Python 3.x.
- The library tabulate should be installed before running the code.
- It should have a main function (`online_bookstore`) and at least three other functions, each accompanied by tests that can be executed without pytest.
- The main function should be in a file called `project.py`, located in the root folder of the project.
- The three required custom functions (other than the main function) should also be in `project.py` and defined at the same indentation level as the main function.
- The test functions should be in a file called `test_project.py`, also located in the root folder of the project. The test functions should have the same name as the custom functions, prepended with `test_`.
- Additional classes and functions can be implemented as desired.
- Any pip-installable libraries required by the project should be listed, one per line, in a file called `requirements.txt` in the root of the project.

## Usage

1. Navigate to the project directory.
2. Install the required dependencies using pip: `pip install -r requirements.txt`
3. Run the Virtual Bookstore by executing `project.py` in the terminal: `python project.py`
4. Follow the prompts to interact with the Virtual Bookstore in CLI.
5. Enjoy your virtual book shopping experience!
