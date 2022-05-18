from dataclasses import fields
from decimal import Decimal
from rest_framework import serializers
from .models import Product, Review

class Productserializer(serializers.ModelSerializer) :
    # email = serializers.CharField(source='owner.email')
    # first_name = serializers.EmailField(source="owner.first_name",read_only=True)
    # last_name = serializers.EmailField(source="owner.last_name",read_only=True)
    # email = serializers.EmailField(source="owner.email",read_only=True)
    # phone = serializers.DecimalField(source="owner.phone",read_only=True,decimal_places=0,max_digits=10)
    class Meta:
        model = Product
        fields = ('id','title','price','description','whatfor','categories','size','rooms','Location','Lat','Long','owner_id')
        extra_kwargs = {"user":{"read_only":True}}
        
    def validate(self, attrs):
        attrs['owner'] = self.context.get("request").user
        return attrs   

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'date', 'name', 'description']

    def create(self, validated_data):
        product_id = self.context['product_id']
        return Review.objects.create(product_id=product_id, **validated_data)

