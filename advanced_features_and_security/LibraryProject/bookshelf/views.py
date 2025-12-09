from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import permission_required, login_required
from .models import Book
from .forms import BookForm, BookSearchForm

def book_list(request):
    """
    Public list view — uses ORM & optionally a validated search parameter.
    Using BookSearchForm validates user input and prevents injection or malformed queries.
    """
    form = BookSearchForm(request.GET or None)
    books = Book.objects.all()

    # Use cleaned data from the form instead of request.GET directly
    if form.is_valid():
        q = form.cleaned_data.get("q")
        if q:
            # parameterized ORM filter; safe from SQL injection
            books = books.filter(title__icontains=q)

    return render(request, "bookshelf/book_list.html", {"books": books, "form": form})


@login_required
@permission_required("bookshelf.can_create", raise_exception=True)
@require_http_methods(["GET", "POST"])
def create_book(request):
    """
    Protected create view. Uses BookForm to validate and save.
    CSRF protection is provided by template via {% csrf_token %}.
    """
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("book_list")
    else:
        form = BookForm()
    return render(request, "bookshelf/form_example.html", {"form": form, "action": "Create"})


@login_required
@permission_required("bookshelf.can_edit", raise_exception=True)
@require_http_methods(["GET", "POST"])
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect("book_list")
    else:
        form = BookForm(instance=book)
    return render(request, "bookshelf/form_example.html", {"form": form, "action": "Edit"})


@login_required
@permission_required("bookshelf.can_delete", raise_exception=True)
@require_http_methods(["POST"])
def delete_book(request, pk):
    """
    Delete via POST only to avoid accidental deletes via GET.
    """
    book = get_object_or_404(Book, pk=pk)
    book.delete()
    return redirect("book_list")


