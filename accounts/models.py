from django.db import models
from django.contrib.auth.models import AbstractUser
# AbstractUser is better than AbstractBaseUser


class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)

