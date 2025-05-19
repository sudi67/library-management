import sqlite3
import datetime

def connect_db():
    return sqlite3.connect('library_management.db')

def table_exists(conn, table_name):
    cursor = conn.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=?", (table_name,))
    return cursor.fetchone() is not None

def test_tables_exist(conn):
    tables = ['Author', 'Category', 'Book', 'Member', 'Loan', 'BookAuthor', 'BookCategory']
    for table in tables:
        assert table_exists(conn, table), f"Table {table} does not exist."

def test_insert_and_query(conn):
    cursor = conn.cursor()

    # Insert Author
    cursor.execute("INSERT INTO Author (first_name, last_name, surname, age, dob) VALUES (?, ?, ?, ?, ?)",
                   ('John', 'Doe', 'JD', 45, '1978-01-01'))
    author_id = cursor.lastrowid

    # Insert Category
    cursor.execute("INSERT INTO Category (name) VALUES (?)", ('Science Fiction',))
    category_id = cursor.lastrowid

    # Insert Book
    cursor.execute("INSERT INTO Book (title, isbn, published_date, total_copies, available_copies) VALUES (?, ?, ?, ?, ?)",
                   ('The Time Machine', '1234567890', '1895-05-07', 5, 5))
    book_id = cursor.lastrowid

    # Link Book and Author
    cursor.execute("INSERT INTO BookAuthor (book_id, author_id) VALUES (?, ?)", (book_id, author_id))

    # Link Book and Category
    cursor.execute("INSERT INTO BookCategory (book_id, category_id) VALUES (?, ?)", (book_id, category_id))

    # Insert Member
    cursor.execute("INSERT INTO Member (first_name, last_name, surname, email, joined_date) VALUES (?, ?, ?, ?, ?)",
                   ('Alice', 'Smith', 'AS', 'alice@example.com', '2023-01-01'))
    member_id = cursor.lastrowid

    # Insert Loan
    loaned_on = '2023-06-01'
    due_back_on = '2023-06-15'
    returned_on = None
    status = 'loaned'
    cursor.execute("""INSERT INTO Loan (book_id, member_id, loaned_on, due_back_on, returned_on, status)
                      VALUES (?, ?, ?, ?, ?, ?)""",
                   (book_id, member_id, loaned_on, due_back_on, returned_on, status))
    loan_id = cursor.lastrowid

    conn.commit()

    # Query to verify
    cursor.execute("""SELECT b.title, a.first_name, c.name, m.first_name, l.status
                      FROM Loan l
                      JOIN Book b ON l.book_id = b.id
                      JOIN Member m ON l.member_id = m.id
                      JOIN BookAuthor ba ON ba.book_id = b.id
                      JOIN Author a ON ba.author_id = a.id
                      JOIN BookCategory bc ON bc.book_id = b.id
                      JOIN Category c ON bc.category_id = c.id
                      WHERE l.id = ?""", (loan_id,))
    row = cursor.fetchone()
    assert row is not None, "Loan query returned no results."
    title, author_first_name, category_name, member_first_name, loan_status = row
    assert title == 'The Time Machine'
    assert author_first_name == 'John'
    assert category_name == 'Science Fiction'
    assert member_first_name == 'Alice'
    assert loan_status == 'loaned'

def test_foreign_key_constraints(conn):
    cursor = conn.cursor()
    # Try to insert Loan with invalid book_id
    try:
        cursor.execute("""INSERT INTO Loan (book_id, member_id, loaned_on, due_back_on, returned_on, status)
                          VALUES (?, ?, ?, ?, ?, ?)""",
                       (9999, 1, '2023-06-01', '2023-06-15', None, 'loaned'))
        conn.commit()
        assert False, "Foreign key constraint failed: invalid book_id accepted."
    except sqlite3.IntegrityError:
        pass

    # Try to insert Loan with invalid member_id
    try:
        cursor.execute("""INSERT INTO Loan (book_id, member_id, loaned_on, due_back_on, returned_on, status)
                          VALUES (?, ?, ?, ?, ?, ?)""",
                       (1, 9999, '2023-06-01', '2023-06-15', None, 'loaned'))
        conn.commit()
        assert False, "Foreign key constraint failed: invalid member_id accepted."
    except sqlite3.IntegrityError:
        pass

def run_all_tests():
    conn = connect_db()
    conn.execute("PRAGMA foreign_keys = ON;")
    try:
        test_tables_exist(conn)
        test_insert_and_query(conn)
        test_foreign_key_constraints(conn)
        print("All tests passed successfully.")
    finally:
        conn.close()

if __name__ == "__main__":
    run_all_tests()
