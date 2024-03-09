class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"{book.title} by {book.author} has been added to the library.")

    def list_books(self):
        if not self.books:
            print("The library has no books.")
            return
        for book in self.books:
            status = "Available" if not book.is_checked_out else "Checked Out"
            print(f"{book.title} by {book.author} - {status}")

    def check_out_book(self, title):
        for book in self.books:
            if book.title == title and not book.is_checked_out:
                print(book.check_out())
                return
        print(f"{title} is not available for checkout.")
