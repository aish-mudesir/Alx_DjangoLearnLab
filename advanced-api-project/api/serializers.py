from rest_framework import serializers
from .models import Author, Book
from datetime import date

# Book serializer with custom validation
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year', 'author']

    # Validate publication year not in future
    def validate_publication_year(self, value):
        current_year = date.today().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value

# Author serializer with nested books
class AuthorSerializer(serializers.ModelSerializer):
    # Nest BookSerializer to include all books by this author
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']
