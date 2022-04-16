from django.urls import path
from .views import *
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', books_list_view, name='books_list'),
    path('<int:pk>/', books_detail_view, name='books_detail'),
    path('create/', login_required(BookCreateView.as_view()), name='create_books'),
    path('<int:pk>/update', login_required(BookUpdateView.as_view()), name='update_books'),
    path('<int:pk>/delete', login_required(BookDeleteView.as_view()), name='delete_books')
]