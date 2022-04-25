from django.views import generic
from .models import Book, Comment
from django.shortcuts import render
from .forms import BookForm, CommentForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404


def books_list_view(request):
    books = Book.objects.all()
    paginator = Paginator(books, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    dic = {
        'books': page_obj,
    }
    return render(request, 'books/books_list_view.html', dic)


def books_detail_view(request, pk):
    books_detail = get_object_or_404(Book, pk=pk)
    # getting_comments
    comments = books_detail.comments.all()
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.book = books_detail
            new_comment.user = request.user
            new_comment.save()
            comment_form = CommentForm()
    else:
        comment_form = CommentForm()
    dic = {
        'books_detail': books_detail,
        'comments': comments,
        'comment_form': comment_form
    }
    return render(request, 'books/books_detail_view.html', dic)


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


@login_required
def user_books_view(request):
    current_user = request.user.id
    books_bool = Book.objects.all().filter(books_author_id=current_user).exists()
    books_pg = Book.objects.all().filter(books_author_id=current_user)
    paginator = Paginator(books_pg, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    dic = {'user_books_auth': books_bool,
           'books': page_obj,
           }
    return render(request, 'books/user_books_view.html', dic)
