# relationship_app/query_samples.py
from relationship_app.models import Author, Book, Library, Librarian

# Query 1: All books by a specific author
def get_books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    return Book.objects.filter(author=author)


# Query 2: List all books in a library
def get_books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    return library.books.all()


# Query 3: Retrieve the librarian for a library
def get_librarian_for_library(library_name):
    library = Library.objects.get(name=library_name)
    return library.librarian


# Example usage (you can run this inside Django shell or for testing)
if __name__ == "__main__":
    # Assuming you already have data in your database
    print("Books by John Doe:")
    for book in get_books_by_author("John Doe"):
        print(book.title)

    print("\nBooks in Central Library:")
    for book in get_books_in_library("Central Library"):
        print(book.title)

    print("\nLibrarian of Central Library:")
    librarian = get_librarian_for_library("Central Library")
    print(librarian.name)
