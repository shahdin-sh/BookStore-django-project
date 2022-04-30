from django.contrib import admin

from .models import Book, Comment


class AdminComment(admin.ModelAdmin):
    list_display = ('user', 'comment_text', 'book', 'datetime_comment')
    ordering = ['-datetime_comment']


admin.site.register(Book)
admin.site.register(Comment, AdminComment)
