
from django.urls import path
from .views import *

urlpatterns = [
    path('home/', home_page_view, name='homepage'),
]
