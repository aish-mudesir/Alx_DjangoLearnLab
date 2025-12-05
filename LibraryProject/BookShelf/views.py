
from django.shortcuts import render
from .models import Book

def index(request):
    return render(request, 'BookShelf/index.html')

def book_list(request):
    books = Book.objects.all()
    return render(request, 'BookShelf/book_list.html', {'books': books})
