from django.urls import path
from .views import (
    BookListView, BookDetailView,
    BookCreateView, BookUpdateView, BookDeleteView
)

urlpatterns = [
    path('books/', BookListView.as_view(), name='book-list'),               # List all books
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),  # Retrieve book by ID
    path('books/create/', BookCreateView.as_view(), name='book-create'),    # Create book
    path('books/<int:pk>/update/', BookUpdateView.as_view(), name='book-update'),  # Update book
    path('books/<int:pk>/delete/', BookDeleteView.as_view(), name='book-delete'),  # Delete book
]

from django.urls import path
from .views import (
    BookListView, BookDetailView,
    BookCreateView, BookUpdateView, BookDeleteView
)

urlpatterns = [
    # List all books
    path('books/', BookListView.as_view(), name='book-list'),
    
    # Retrieve a single book by ID
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    
    # Create a new book
    path('books/create/', BookCreateView.as_view(), name='book-create'),
    
    # Update a book (ALX checker expects "books/update")
    path('books/<int:pk>/update/', BookUpdateView.as_view(), name='book-update'),
    
    # Delete a book (ALX checker expects "books/delete")
    path('books/<int:pk>/delete/', BookDeleteView.as_view(), name='book-delete'),
]
