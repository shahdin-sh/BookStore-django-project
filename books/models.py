from django.urls import reverse
from django.db import models
from django.contrib.auth import get_user_model


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    translator = models.CharField(max_length=50)
    description = models.TextField()
    publisher = models.CharField(max_length=50, null=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    books_author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('books_detail', args=[self.id])
