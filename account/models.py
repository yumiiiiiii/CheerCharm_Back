from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    nickname=models.TextField(max_length=50)
    create_time=models.DateTimeField(auto_now_add=True)
    delete_time=models.DateTimeField(auto_now=True)
    
