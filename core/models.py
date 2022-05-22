import email
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email=models.EmailField(unique=True)
    account_type=models.CharField(max_length=255)
    avatar = models.ImageField(upload_to='API/images',max_length=100,null=True)   