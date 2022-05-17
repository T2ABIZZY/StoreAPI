from dataclasses import fields
from decimal import Decimal
from rest_framework import serializers
from .models import Customer, Product, Review

class Productserializer(serializers.ModelSerializer) :

    class Meta:
        model = Product
        fields = ('id','title','price','description','whatfor','categories','size','rooms','owner_id')
        extra_kwargs = {"user":{"read_only":True}}
        
    def validate(self, attrs):
        attrs['owner'] = self.context.get("request").user
        return attrs   


        # def save (self):
        #     owner = None
        #     request = self.context.get("request")
        #     if request and hasattr(request, "user"):
        #         owner = request.user    



class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'date', 'name', 'description']

    def create(self, validated_data):
        product_id = self.context['product_id']
        return Review.objects.create(product_id=product_id, **validated_data)
class CustomerSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(read_only=True)
    class Meta:
        model = Customer
        fields = ['id','user_id','phone','State']
