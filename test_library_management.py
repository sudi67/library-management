from library_management import Person, Member, Librarian, Book, Library

def main():
    
    library = Library()
    print("Welcome to the Community Library!")

    
    book1 = Book("1984", "George Orwell")
    book2 = Book("To Kill a Mockingbird", "Harper Lee")
    book3 = Book("The Great Gatsby", "F. Scott Fitzgerald")

    
    library.add_book("B001", book1)
    library.add_book("B002", book2)
    library.add_book("B003", book3)

   
    member1 = Member("Alice", "M1001")
    member2 = Member("Bob", "M1002")
    librarian = Librarian("Eve", "L2001")

    
    print("\nLet's meet our library members and librarian:")
    member1.introduce()
    member2.introduce()
    librarian.introduce()

    
    print("\nEve, the librarian, shows the available books in the library:")
    for book_info in library.list_available():
        print(book_info)

    
    print("\nAlice decides to borrow '1984':")
    if member1.borrow(book1, library):
        print("Alice successfully borrows '1984'.")
    else:
        print("Alice fails to borrow '1984'.")

    
    print("\nAlice's currently borrowed books:")
    for b in member1.list_borrowed():
        print(b)

    
    print("\nAvailable books in the library after Alice's borrowing:")
    for book_info in library.list_available():
        print(book_info)

   
    print("\nAlice returns '1984' after finishing it:")
    member1.return_book(book1, library)

   
    print("\nAlice's currently borrowed books after returning '1984':")
    for b in member1.list_borrowed():
        print(b)

    
    print("\nAvailable books in the library after Alice's return:")
    for book_info in library.list_available():
        print(book_info)

    
    print("\n--- Thorough Testing of Edge Cases ---")

    
    book_not_in_catalog = Book("Invisible Man", "Ralph Ellison")
    print("\nBob tries to borrow 'Invisible Man', which is not in the catalog:")
    if member2.borrow(book_not_in_catalog, library):
        print("Bob successfully borrows 'Invisible Man'.")
    else:
        print("Bob fails to borrow 'Invisible Man' (not in catalog).")

   
    print("\nAlice borrows 'To Kill a Mockingbird':")
    if member1.borrow(book2, library):
        print("Alice successfully borrows 'To Kill a Mockingbird'.")
    else:
        print("Alice fails to borrow 'To Kill a Mockingbird'.")

    print("\nBob tries to borrow 'To Kill a Mockingbird', which is already lent out:")
    if member2.borrow(book2, library):
        print("Bob successfully borrows 'To Kill a Mockingbird'.")
    else:
        print("Bob fails to borrow 'To Kill a Mockingbird' (already lent out).")

    
    print("\nBob tries to return '1984', which he did not borrow:")
    member2.return_book(book1, library)

    
    empty_library = Library()
    print("\nEve checks the available books in an empty library:")
    print(empty_library.list_available())

    
    print("\nMultiple members borrowing and returning books:")
    member2.borrow(book3, library)
    print("Bob's currently borrowed books:")
    for b in member2.list_borrowed():
        print(b)

    member2.return_book(book3, library)
    print("\nBob's currently borrowed books after returning 'The Great Gatsby':")
    for b in member2.list_borrowed():
        print(b)

    print("\nAvailable books in the library after Bob's return:")
    for book_info in library.list_available():
        print(book_info)

if _name_ == "_main_":
    main()