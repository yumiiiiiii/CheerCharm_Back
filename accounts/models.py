from django.db import models
from django.contrib.auth.models import AbstractUser


class TimestampZone(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True)

    class Meta:
        abstract = True


class User(AbstractUser):
    first_name=None
    last_name=None

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True)
    email = models.EmailField(unique=True)
    username = models.CharField(unique=True, default='', max_length=256)
    nickname = models.CharField(max_length=8)
    password=models.CharField(max_length=128)
    url_value = models.CharField(max_length=2000)

    def __str__(self):
        return f'{self.username}'
