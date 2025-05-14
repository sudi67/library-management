# Library Management System and Bank Classes

This project demonstrates Object-Oriented Programming (OOP) principles through the implementation of a Library Management System and a Bank class.

## Library Management System

The system demonstrates the four pillars of OOP:

- **Inheritance:** `Member` and `Librarian` classes inherit from the `Person` base class.
- **Encapsulation:** Internal states such as borrowed books and catalog are private and accessed via getters/setters.
- **Polymorphism:** The `introduce()` method is overridden in each subclass to provide specific introductions.
- **Abstraction:** The `Library` class provides methods like `add_book()`, `lend_book()`, `receive_book()`, and `list_available()` to interact with the library without exposing internal details.

### Classes

- `Person`: Base class with a protected attribute `_name` and a generic `introduce()` method.
- `Member`: Inherits from `Person`, has private attributes for member ID and borrowed books, and overrides `introduce()`.
- `Librarian`: Inherits from `Person`, has a private employee ID, and overrides `introduce()`.
- `Book`: Represents a book with public attributes `title` and `author`.
- `Library`: Manages a catalog of books and their availability.

## Bank Class

The `Bank` class demonstrates encapsulation and abstraction with private balance and PIN attributes, and methods for:

- `withdraw(amount)`: Withdraw money if sufficient balance and account not blocked.
- `deposit(amount)`: Deposit money.
- `get_balance()`: Get current balance.
- `reset_pin(pin, otp)`: Abstract method to reset PIN.
- `login(pin)`: Login with PIN, blocks account after 3 failed attempts.
- `set_pin(pin)`: Set the account PIN.

## Usage

Implementations of the classes are provided in the `library_management.py` file.

## Notes

- The Bank class is abstract and requires subclassing to implement the `reset_pin` method.
- The Library Management System enforces encapsulation by using private attributes and exposing only necessary methods.
