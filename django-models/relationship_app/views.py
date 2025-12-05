from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from .models import Book
from .forms import BookForm  # You must create a simple form for this


# -----------------------------
# ADD BOOK (Requires can_add_book)
# -----------------------------
@permission_required('relationship_app.can_add_book')
def add_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_books')
    else:
        form = BookForm()

    return render(request, 'relationship_app/add_book.html', {'form': form})


# -----------------------------
# EDIT BOOK (Requires can_change_book)
# -----------------------------
@permission_required('relationship_app.can_change_book')
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    form = BookForm(request.POST or None, instance=book)

    if form.is_valid():
        form.save()
        return redirect('list_books')

    return render(request, 'relationship_app/edit_book.html', {'form': form, 'book': book})


# -----------------------------
# DELETE BOOK (Requires can_delete_book)
# -----------------------------
@permission_required('relationship_app.can_delete_book')
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)

    if request.method == "POST":
        book.delete()
        return redirect('list_books')

    return render(request, 'relationship_app/delete_book.html', {'book': book})

