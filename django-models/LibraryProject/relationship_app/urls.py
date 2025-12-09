from django.urls import path
from .views import login_view, logout_view, register_view
from .views import list_books, LibraryDetailView  # existing views

urlpatterns = [
    # Authentication URLs
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("register/", register_view, name="register"),

    # Book & Library URLs
    path("books/", list_books, name="list_books"),
    path("library/<int:pk>/", LibraryDetailView.as_view(), name="library_detail"),
]
