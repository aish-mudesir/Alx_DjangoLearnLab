from django.http import HttpResponse
from .models import Book

def home(request):
    books = Book.objects.all()
    output = ", ".join([b.title for b in books])
    return HttpResponse(f"Books: {output}")

