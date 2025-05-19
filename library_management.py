from typing import List

class Person:
    def __init__(self, name: str):
        self._name = name 

    def introduce(self):
        print(f"Hello, my name is {self._name}.")

class Member(Person):
    def __init__(self, name: str, member_id: str):
        super().__init__(name)
        self.__member_id = member_id
        self.__borrowed = []

    def borrow(self, book, library) -> bool:
        if library.lend_book(book, self):
            self.__borrowed.append(book)
            return True
        return False

    def return_book(self, book, library):
        if book in self.__borrowed:
            library.receive_book(book)
            self.__borrowed.remove(book)

    def list_borrowed(self) -> List[str]:
        return [f"{book.title} by {book.author}" for book in self.__borrowed]

    def introduce(self):
        print(f"Hello, my name is {self._name} and I am a member with ID {self.__member_id}.")

class Librarian(Person):
    def __init__(self, name: str, employee_id: str):
        super().__init__(name)
        self.__employee_id = employee_id

    def introduce(self):
        print(f"Hello, my name is {self._name} and I am a librarian with employee ID {self.__employee_id}.")

class Book:
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author

class Library:
    def __init__(self):
        self.__catalog = {}
        self.__available = set()

    def add_book(self, code: str, book: Book):
        self.__catalog[code] = book
        self.__available.add(code)

    def lend_book(self, book: Book, member: Member) -> bool:
        for code, b in self.__catalog.items():
            if b == book and code in self.__available:
                self.__available.remove(code)
                return True
        return False

    def receive_book(self, book: Book):
        # Find the code for the
        for code, b in self.__catalog.items():
            if b == book:
                self.__available.add(code)
                break

    def list_available(self) -> List[str]:
        return [f"{self.__catalog[code].title} by {self.__catalog[code].author}" for code in self.__available]