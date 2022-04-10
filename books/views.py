from django.shortcuts import render
from .models import Book
from django.shortcuts import render


def books_list_view(request):
    books = Book.objects.all()
    return render(request, 'books/books_list_view.html', {'books': books})

