from django.urls import path
from .views import *

urlpatterns = [
    path('', books_list_view, name='books_list')
]