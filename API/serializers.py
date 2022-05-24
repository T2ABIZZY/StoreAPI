from dataclasses import fields
from decimal import Decimal
from pyexpat import model
from rest_framework import serializers
from .models import Product, Review,ProductImages,Bookmark

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImages
        fields = ['images']
class Productserializer(serializers.ModelSerializer) :
    images= ProductImageSerializer(many=True, read_only = True)
    uploaded_images = serializers.ListField(
        child = serializers.FileField(max_length = 1000000, allow_empty_file = False, use_url = False),
        write_only = True
    )
    class Meta:
        model = Product
        fields = ('id','title','price','description','whatfor','categories','size','rooms','Location','Lat','Long','owner_id','images','uploaded_images',)
        extra_kwargs = {"user":{"read_only":True}}

        
    def validate(self, attrs):
        attrs['owner'] = self.context.get("request").user
        return attrs   
    def create(self, validated_data):
        uploaded_data = validated_data.pop('uploaded_images')
        new_product = Product.objects.create(**validated_data)
        for uploaded_item in uploaded_data:
            ProductImages.objects.create(product = new_product, images = uploaded_item)
        return new_product




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
        def validate(self, attrs):
            attrs['bookmarked_by'] = self.context.get("request").user
            return attrs            

        # def create(self, validated_data):
        #     request = self.context["request"]
        #     ModelClass = self.Meta.model

        #     instance = ModelClass.objects.create(
        #         **validated_data, **{"bookmarked_by": request.user}
        #     )
        #     return instance
   

