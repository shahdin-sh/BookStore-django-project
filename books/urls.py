from django.urls import path
from .views import *

urlpatterns = [
    path('', books_list_view, name='books_list'),
    path('<int:pk>/', books_detail_view, name='books_detail'),
    path('create/', BookCreateView.as_view(), name='create_books'),
    path('<int:pk>/update', BookUpdateView.as_view(), name='update_books'),
    path('<int:pk>/delete', BookDeleteView.as_view(), name='delete_books')
]