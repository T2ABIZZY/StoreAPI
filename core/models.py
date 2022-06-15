import email
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email=models.EmailField(unique=True)
    account_type=models.CharField(max_length=255)
    avatar = models.ImageField(upload_to='API/images',max_length=100)
    phone = models.DecimalField(max_digits=10,decimal_places=0,null=True)
    description = models.CharField(max_length=2550,null=True)
    location = models.CharField(max_length=255,null=True)
