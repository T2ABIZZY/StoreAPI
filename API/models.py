from django.conf import settings
from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(
        max_digits=6,
        decimal_places=2,
       )
    last_update = models.DateTimeField(auto_now=True)
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