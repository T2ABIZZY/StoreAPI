from email.policy import default
from random import choices
from unittest.util import _MAX_LENGTH
from django.conf import settings
from django.db import models
from django.forms import CharField
User = settings.AUTH_USER_MODEL

class Product(models.Model):
    RENT=0
    SALE=1
    PURPOSES = [
        (RENT,'for rent'),
        (SALE,'for sale'),
    ]
    
    APPARTMENT = 0
    HOUSE = 1
    INDUSTRIAL = 2
    COMMERCIAL = 3
    LAND = 4
    CATEGORIES = [
        (APPARTMENT, 'Appartement'),
        (HOUSE, 'House'),
        (INDUSTRIAL, 'Industrial'),
        (COMMERCIAL, 'Commercial'),
        (LAND, 'Land'),
    ]
    category = models.IntegerField(
        choices=CATEGORIES,
        default=APPARTMENT,
    )

    title = models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(
        max_digits=9,
        decimal_places=00,
        unique=True
       )
    purpose = models.IntegerField(
        choices=PURPOSES, 
        default=RENT
    )
    size = models.DecimalField(
        max_digits=6,
        decimal_places=0,
        null=True
    )
    rooms = models.DecimalField(
        max_digits=2,
        decimal_places=0,
        null=True
    )
    last_update = models.DateTimeField(auto_now=True)
    Location = models.CharField(max_length=255,blank=True)
    Lat = models.DecimalField(
        max_digits=25, decimal_places=20,)
    Long = models.DecimalField(
        max_digits=25, decimal_places=20)   
    owner = models.ForeignKey(User, related_name='Products', on_delete=models.CASCADE,null=True)
    
    def __str__(self) -> str:
        return self.title

    class Meta:
        ordering = ['title']


class ProductImages(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="images", null=False)
    image = models.ImageField(upload_to='API/images',max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)


class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    owner = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE,null=True)
    description = models.TextField()
    date = models.DateField(auto_now_add=True)

class UserProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name="profile")
    date_joined=models.DateTimeField(auto_now_add=True)
    updated_on=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.user.username