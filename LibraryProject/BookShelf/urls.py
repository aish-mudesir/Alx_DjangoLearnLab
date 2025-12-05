
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='bookshelf-home'),
    path('books/', views.book_list, name='book-list'),
]
