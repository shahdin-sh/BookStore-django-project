from django.shortcuts import render
from .models import Book
from django.shortcuts import render


def books_list_view(request):
    books = Book.objects.all()
    return render(request, 'books/books_list_view.html', {'books': books})


def books_detail_view(request, pk):
    books_detail = Book.objects.get(pk=pk)
    return render(request, 'books/books_detail_view.html', {'books_detail': books_detail})

