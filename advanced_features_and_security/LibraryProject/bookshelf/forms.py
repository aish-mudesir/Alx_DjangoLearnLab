from django import forms
from .models import Book


class ExampleForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ["title", "author", "publication_year"]
        widgets = {
            "title": forms.TextInput(attrs={"maxlength": 200}),
            "author": forms.TextInput(attrs={"maxlength": 200}),
        }

# Search form to use validated fields instead of raw query strings
class BookSearchForm(forms.Form):
    q = forms.CharField(required=False, max_length=100)
