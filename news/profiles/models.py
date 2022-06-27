from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='email')
    balance = models.PositiveIntegerField(blank=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []



