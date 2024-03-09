
from Library import Library
from Book import Book
def main():
    # Create a library instance
    my_library = Library()

    # Create some book instances
    book1 = Book("Python Programming", "John Doe")
    book2 = Book("Learning Python", "Jane Doe")
    book3 = Book("Data Structure", "Mark John")

    # Add books to the library
    my_library.add_book(book1)
    my_library.add_book(book2)
    my_library.add_book(book3)

    # List all books in the library
    my_library.list_books()

    # Check out a book
    my_library.check_out_book("Python Programming")
    my_library.list_books()


if __name__ == "__main__":
    main()
