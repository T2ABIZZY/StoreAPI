from dataclasses import fields
from decimal import Decimal
from tkinter import Image
from rest_framework.exceptions import ValidationError
from rest_framework import serializers
from .models import Product, ProductImages, Review

class ProductSerializer(serializers.ModelSerializer) :
    # email = serializers.CharField(source='owner.email')
    # first_name = serializers.EmailField(source="owner.first_name",read_only=True)
    # last_name = serializers.EmailField(source="owner.last_name",read_only=True)
    # email = serializers.EmailField(source="owner.email",read_only=True)
    # phone = serializers.DecimalField(source="owner.phone",read_only=True,decimal_places=0,max_digits=10)
    image = serializers.ImageField(required=True, write_only=True)
    class Meta:
        model = Product
        fields = ('id','title','price','description','purpose','category','size','rooms','Location','Lat','Long','owner_id','image')
        
    def validate(self, data):
        data['owner'] = self.context.get("user", None)
        if not data["owner"]:
            raise ValidationError("invalid user")
        return data   
    
    def create(self, validated_data):
        image = validated_data["image"]
        validated_data.pop("image")
        product = Product.objects.create(**validated_data)
        ProductImages.objects.create(product=product, image=image)
        self._data = ProductSerializer(product).data
        return True

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret["category"] = dict(Product.CATEGORIES)[instance.category]
        ret["purpose"] = dict(Product.PURPOSES)[instance.purpose]
        return ret


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'date', 'description','owner_id']
        extra_kwargs = {"user":{"read_only":True}}
    def validate(self, attrs):
        attrs['owner'] = self.context.get("request").user
        return attrs   














    def create(self, validated_data):
        product_id = self.context['product_id']
        return Review.objects.create(product_id=product_id, **validated_data)

