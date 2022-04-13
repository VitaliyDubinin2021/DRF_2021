from django.db import models
from django.contrib.auth.models import AbstractBaseUser


class User(AbstractBaseUser):
    user_name = models.CharField(max_length=128, unique=True)
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    email = models.EmailField(max_length=40, unique=True)

    class Meta:
        ordering = ['pk']

    def __str__(self):
        return f'{self.user_name} | {self.email} | {self.first_name} {self.last_name}'
