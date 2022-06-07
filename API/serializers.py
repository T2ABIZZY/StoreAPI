from rest_framework import serializers
from .models import Offer, Comment,OfferImages,Bookmark

class offerImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = OfferImages
        fields = ['images']
class offerserializer(serializers.ModelSerializer) :
    images= offerImageSerializer(many=True, read_only = True)
    uploaded_images = serializers.ListField(
        child = serializers.FileField(max_length = 1000000, allow_empty_file = False, use_url = False),
        write_only = True
    )
    class Meta:
        model = Offer
        fields = ('id','title','price','description','whatfor','categories','size','rooms','Location','Lat','Long','owner_id','images','uploaded_images',)
        extra_kwargs = {"user":{"read_only":True}}

        
    def validate(self, attrs):
        attrs['owner'] = self.context.get("request").user
        return attrs   
    def create(self, validated_data):
        uploaded_data = validated_data.pop('uploaded_images')
        new_offer = Offer.objects.create(**validated_data)
        for uploaded_item in uploaded_data:
            OfferImages.objects.create(Offer = new_offer, images = uploaded_item)
        return new_offer




class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'date', 'description','owner_id']
        extra_kwargs = {"user":{"read_only":True}}
    def validate(self, attrs):
        attrs['owner'] = self.context.get("request").user
        return attrs   

    def create(self, validated_data):
        Offer_id = self.context['Offer_id']
        return Comment.objects.create(Offer_id=Offer_id, **validated_data)

# class UserSerializer(serializers.ModelSerializer):
#         class Meta:
#             model = User
#             fields = ["username", "email", "date_joined"]

class BookmarkSerializer(serializers.ModelSerializer):
    title = serializers.EmailField(source="offer.title",read_only=True)
    class Meta:
        model = Bookmark
        fields = ["id","offer", "bookmarked_by", "bookmarked_at","title"]
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
   

