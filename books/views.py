from django.views import generic
from .models import Book
from django.shortcuts import render
from .forms import BookForm
from django.urls import reverse_lazy

def books_list_view(request):
    books = Book.objects.all()
    return render(request, 'books/books_list_view.html', {'books': books})


def books_detail_view(request, pk):
    books_detail = Book.objects.get(pk=pk)
    return render(request, 'books/books_detail_view.html', {'books_detail': books_detail})


class BookCreateView(generic.CreateView):
    form_class = BookForm
    template_name = 'books/books_create_view.html'


class BookUpdateView(generic.UpdateView):
    model = Book
    fields = ['title', 'author', 'translator', 'description']
    template_name = 'books/books_update_view.html'


class BookDeleteView(generic.DeleteView):
    model = Book
    template_name = 'books/books_delete_view.html'
    success_url = reverse_lazy('books_list')
