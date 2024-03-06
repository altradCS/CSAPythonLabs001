class Book:
    def __init__(self, title, author, year, editor):
        self.title = title
        self.author = author
        self.year = year
        self.editor = editor
        self.is_checked_out = False


    def check_out(self):
        if not self.is_checked_out:
            self.is_checked_out = True
            return f"{self.title} has been checked out."
        else:
            return f"{self.title} is already checked out."


