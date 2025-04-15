class Book:
    def __init__(self, title, author, isbn, publication_year, genre):
        """
        Constructor to initialize a Book object.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
            isbn (str): The International Standard Book Number.
            publication_year (int): The year the book was published.
            genre (str): The genre of the book.
        """
        self.title = title
        self.author = author
        self.isbn = isbn
        self.publication_year = publication_year
        self.genre = genre
        self.is_borrowed = False

    def __str__(self):
        """
        String representation of the Book object.
        """
        return f"Title: {self.title}\nAuthor: {self.author}\nISBN: {self.isbn}\nPublished: {self.publication_year}\nGenre: {self.genre}\nBorrowed: {self.is_borrowed}"

    def borrow(self):
        """
        Marks the book as borrowed.
        """
        if not self.is_borrowed:
            self.is_borrowed = True
            print(f"'{self.title}' has been borrowed.")
        else:
            print(f"'{self.title}' is already borrowed.")

    def return_book(self):
        """
        Marks the book as returned.
        """
        if self.is_borrowed:
            self.is_borrowed = False
            print(f"'{self.title}' has been returned.")
        else:
            print(f"'{self.title}' was not borrowed.")

    def get_details(self):
        """
        Returns a dictionary of the book's details.
        """
        return {
            "title": self.title,
            "author": self.author,
            "isbn": self.isbn,
            "publication_year": self.publication_year,
            "genre": self.genre,
            "is_borrowed": self.is_borrowed
        }

# Inheritance Layer: Creating a specialized type of Book - EBook
class EBook(Book):
    def __init__(self, title, author, isbn, publication_year, genre, file_format, file_size_mb):
        """
        Constructor for an EBook object, inheriting from Book.

        Args:
            title (str): The title of the ebook.
            author (str): The author of the ebook.
            isbn (str): The International Standard Book Number.
            publication_year (int): The year the ebook was published.
            genre (str): The genre of the ebook.
            file_format (str): The format of the ebook file (e.g., PDF, EPUB).
            file_size_mb (float): The size of the ebook file in megabytes.
        """
        super().__init__(title, author, isbn, publication_year, genre)
        self.file_format = file_format
        self.file_size_mb = file_size_mb

    def __str__(self):
        """
        String representation of the EBook object, extending the parent's.
        """
        return f"{super().__str__()} \nFile Format: {self.file_format}\nFile Size: {self.file_size_mb} MB"

    def read(self):
        """
        Simulates reading the ebook.
        """
        print(f"Opening and reading '{self.title}' in {self.file_format} format...")

# Creating instances of the classes
book1 = Book("The Hitchhiker's Guide to the Galaxy", "Douglas Adams", "978-0345391803", 1979, "Science Fiction")
ebook1 = EBook("Foundation", "Isaac Asimov", "978-0553803712", 1951, "Science Fiction", "EPUB", 2.5)

# Demonstrating the methods
print("--- Book 1 ---")
print(book1)
book1.borrow()
print(book1)
book1.return_book()
print(book1)
print("\n--- EBook 1 ---")
print(ebook1)
ebook1.borrow()
ebook1.read()
ebook1.return_book()