from django.db import models
from django.utils import timezone

# Author model
class Author(models.Model):
    # Author name field
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

# Book model
class Book(models.Model):
    # Title of the book
    title = models.CharField(max_length=255)
    # Year of publication
    publication_year = models.IntegerField()
    # ForeignKey to Author: One-to-Many relationship
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
