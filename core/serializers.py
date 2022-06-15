from djoser.serializers import  UserSerializer as BaseUserSerializer, UserCreateSerializer  as BaseUserCreateSerializer
from .models import User
from API.models import UserProfile
from rest_framework import serializers

class UserCreateSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        fields=['id','account_type','username','email','password','first_name','last_name','avatar','phone','description','location']

class UserSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        fields=['id','account_type','username','email','password','first_name','last_name','avatar','phone','description','location']

class CurrentUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'id','first_name','password','last_name','account_type','avatar','phone','description','location')

class userProfileSerializer(serializers.ModelSerializer):
    user=CurrentUserSerializer(read_only=True)
    class Meta:
        model=UserProfile
        fields='__all__'
