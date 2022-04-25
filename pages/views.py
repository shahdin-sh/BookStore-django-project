from django.shortcuts import render
from books.models import Book
from django.core.paginator import Paginator


def home_page_view(request):
    books = Book.objects.all()
    paginator = Paginator(books, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'pages/home.html', {'books': page_obj})
