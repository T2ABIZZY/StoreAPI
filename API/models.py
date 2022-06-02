
from unittest.util import _MAX_LENGTH
from django.conf import settings
from django.db import models
from django.forms import CharField
User = settings.AUTH_USER_MODEL

class Offer(models.Model):
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
    owner = models.ForeignKey(User, related_name='Offers', on_delete=models.CASCADE,null=True)
    def __str__(self) -> str:
        return self.title

    class Meta:
        ordering = ['title']

class OfferImages(models.Model):
      Offer = models.ForeignKey(Offer, on_delete=models.CASCADE, related_name='images')
      images = models.FileField(upload_to='API/images',max_length=100,null=True)



class Comment(models.Model):
    Offer = models.ForeignKey(Offer, on_delete=models.CASCADE, related_name='comments')
    owner = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE,null=True)
    description = models.TextField()
    date = models.DateField(auto_now_add=True)

class UserProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name="profile")
    date_joined=models.DateTimeField(auto_now_add=True)
    updated_on=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.user.username

class Bookmark(models.Model):
    Offer = models.ForeignKey(Offer, on_delete=models.CASCADE, related_name='bookmark')
    bookmarked_by = models.ForeignKey(User, related_name='bookmark', on_delete=models.CASCADE,null=True)
    bookmarked_at = models.DateTimeField(auto_now_add=True)
