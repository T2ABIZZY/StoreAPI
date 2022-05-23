from dataclasses import fields
from decimal import Decimal
from pyexpat import model
from rest_framework import serializers
from .models import Product, Review,ProductImages,Bookmark,User

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImages
        fields = '__all__'
class Productserializer(serializers.ModelSerializer) :
    images= ProductImageSerializer(many=True)
    class Meta:
        model = Product
        fields = ('id','title','price','description','whatfor','categories','size','rooms','Location','Lat','Long','owner_id','images')
        extra_kwargs = {"user":{"read_only":True}}
        
    def validate(self, attrs):
        attrs['owner'] = self.context.get("request").user
        return attrs   

    def create(self, validated_data):
        images = validated_data["images"]
        validated_data.pop("images")
        product = Product.objects.create(**validated_data)
        ProductImages.objects.create(product=product, images=images)
        self._data = Productserializer(product).data
        return True
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

# class UserSerializer(serializers.ModelSerializer):
#         class Meta:
#             model = User
#             fields = ["username", "email", "date_joined"]

class BookmarkSerializer(serializers.ModelSerializer):
    title = serializers.EmailField(source="product.title",read_only=True)
    class Meta:
        model = Bookmark
        fields = ["product", "bookmarked_by", "bookmarked_at","title"]
        extra_kwargs = {"user":{"read_only":True}}
        def create(self, validated_data):
            request = self.context["request"]
            ModelClass = self.Meta.model

            instance = ModelClass.objects.create(
                **validated_data, **{"bookmarked_by": request.user}
            )
            return instance
        def validate(self, attrs):
            attrs['owner'] = self.context.get("request").user
            return attrs               

