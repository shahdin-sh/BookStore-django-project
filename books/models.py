from django.urls import reverse
from django.db import models
from django.contrib.auth import get_user_model


class Book(models.Model):
    title = models.CharField(max_length=100, verbose_name='عنوان')
    author = models.CharField(max_length=50, verbose_name='نویسنده')
    translator = models.CharField(max_length=50, verbose_name='مترجم')
    description = models.TextField(verbose_name='توضیحات کتاب')
    publisher = models.CharField(max_length=50, null=True, verbose_name='انتشارات')
    price = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='قیمت')
    books_author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True, verbose_name='کاربر')
    book_cover = models.ImageField(upload_to='book_covers/', blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('books_detail', args=[self.id])
