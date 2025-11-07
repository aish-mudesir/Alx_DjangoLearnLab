
from relationship_app.models import Author, Book, Library, Librarian
from django.core.exceptions import ObjectDoesNotExist


def get_books_by_author(author_name):
    """
    Return all books written by a specific author.
    """
    try:
        author = Author.objects.get(name=author_name)
        books = author.books.all()  # Uses related_name from Book model
        return books
    except ObjectDoesNotExist:
        print(f"❌ Author '{author_name}' not found.")
        return []


def get_books_in_library(library_name):
    """
    Return all books available in a specific library.
    """
    try:
        library = Library.objects.get(name=library_name)
        books = library.books.all()
        return books
    except ObjectDoesNotExist:
        print(f"❌ Library '{library_name}' not found.")
        return []


def get_librarian_for_library(library_name):
    """
    Retrieve the librarian assigned to a specific library.
    """
    try:
        library = Library.objects.get(name=library_name)
        librarian = library.librarian  # Accesses OneToOne relationship
        return librarian
    except ObjectDoesNotExist:
        print(f"❌ Library '{library_name}' or librarian not found.")
        return None


def display_books(books):
    """
    Helper function to print book titles in a formatted way.
    """
    if not books:
        print("No books found.")
    else:
        for book in books:
            print(f"- {book.title}")


if __name__ == "__main__":
    print("\n📚 Books by John Doe:")
    display_books(get_books_by_author("John Doe"))

    print("\n🏛️ Books in Central Library:")
    display_books(get_books_in_library("Central Library"))

    print("\n👩‍💼 Librarian of Central Library:")
    librarian = get_librarian_for_library("Central Library")
    if librarian:
        print(f"- {librarian.name}")
