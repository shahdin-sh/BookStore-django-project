# Generated by Django 4.0.3 on 2022-05-01 09:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('books', '0010_comment_is_active_comment_recommended'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='books_author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='کاربر'),
            preserve_default=False,
        ),
    ]