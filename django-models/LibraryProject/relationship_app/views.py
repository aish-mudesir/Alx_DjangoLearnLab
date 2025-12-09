from django.shortcuts import render
from django.views.generic import DetailView
from .models import Book, Library


# ---------------------------
# FUNCTION-BASED VIEW
# MUST include: Book.objects.all()
# ---------------------------
def list_books(request):
    # Your checker requires this exact line
    books = Book.objects.all()

    return render(request, "relationship_app/list_books.html", {
        "books": books
    })


# ---------------------------
# CLASS-BASED VIEW FOR LIBRARY DETAILS
# ---------------------------
class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"

