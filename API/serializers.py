from decimal import Decimal
from rest_framework import serializers
from .models import Product, Review

class Productserializer(serializers.ModelSerializer) :
    class Meta:
        model = Product
        fields = ('id','title','price','price_with_discount')
    price_with_discount = serializers.SerializerMethodField(method_name='calculate')

    def calculate(self , product : Product):
        return product.price * Decimal(0.9)



class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'date', 'name', 'description']

    def create(self, validated_data):
        product_id = self.context['product_id']
        return Review.objects.create(product_id=product_id, **validated_data)