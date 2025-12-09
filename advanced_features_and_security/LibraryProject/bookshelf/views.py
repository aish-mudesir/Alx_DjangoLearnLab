from django.shortcuts import render
from .forms import ExampleForm
from .models import Book
from django.contrib.auth.decorators import login_required

@login_required
def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})

def form_example(request):
    form = ExampleForm()

    if request.method == "POST":
        form = ExampleForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            return render(request, 'bookshelf/form_example.html',
                          {'form': form, 'message': f"Submitted by {name}"})

    return render(request, 'bookshelf/form_example.html', {'form': form})



