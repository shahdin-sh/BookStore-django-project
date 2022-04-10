from django.urls import path
from .views import *

urlpatterns = [
    path('', books_list_view, name='books_list'),
    path('<int:pk>/', books_detail_view, name='books_detail'),
]