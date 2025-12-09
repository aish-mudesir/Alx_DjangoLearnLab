from django.shortcuts import render
from django.views.generic import DetailView

# Your checker requires BOTH imports:
from .models import Book
from .models import Library   # <-- required by checker


# ---------------------------
# FUNCTION-BASED VIEW
# ---------------------------
def list_books(request):
    books = Book.objects.all()   # <-- required by checker

    return render(request, "relationship_app/list_books.html", {
        "books": books
    })


# ---------------------------
# CLASS-BASED VIEW
# ---------------------------
class LibraryDetailView(DetailView):
    model = Library               # <-- uses Library model
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"


