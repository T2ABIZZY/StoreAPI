from email.policy import default
from random import choices
from unittest.util import _MAX_LENGTH
from django.conf import settings
from django.db import models
from django.forms import CharField
User = settings.AUTH_USER_MODEL

class Product(models.Model):
    for_rent='for_rent'
    for_sale='for_sale'
    for_choices = [
        (for_rent,'for rent'),
        (for_sale,'for sale'),
    ]
    appartement = 'Appartement'
    house = 'House'
    industrial = 'Industrial'
    commercial = 'Commercial'
    Land = 'Land'
    categories_CHOICES = [
        (appartement, 'appartement'),
        (house, 'house'),
        (industrial, 'industrial'),
        (commercial, 'commercial'),
        (Land, 'Land'),
    ]
    categories = models.CharField(
        max_length=11,
        choices=categories_CHOICES,
        default=appartement,
    )

    title = models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(
        max_digits=9,
        decimal_places=00,
        unique=True
       )
    whatfor = models.CharField(
        max_length=8,choices=for_choices, default=for_rent
    )
    size = models.DecimalField(
        max_digits=6,
        decimal_places=0,
        null=True
    )
    rooms = models.DecimalField(
        max_digits=1,
        decimal_places=0,
        null=True
    )
    last_update = models.DateTimeField(auto_now=True)
    dasdsa= models.BooleanField
    owner = models.ForeignKey(User, related_name='Products', on_delete=models.CASCADE,null=True)
    def __str__(self) -> str:
        return self.title

    class Meta:
        ordering = ['title']

class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    name = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateField(auto_now_add=True)

class Customer(models.Model):
    phone = models.DecimalField(max_digits=9,decimal_places=0,null=True)
    State = models.CharField(max_length=20) 
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    def __str__(self) :
        return f'{self.user.first_name},{self.user.last_name}'
class likedposts(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='likedposts')
    userid = models.DecimalField(max_digits=9,decimal_places=0)
    likedpostsid= models.DecimalField(max_digits=9,decimal_places=0)