from django.db.models.aggregates import Count
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from requests import request
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.decorators import action
from rest_framework import status
from .filters import ProductFilter
from .models import  Bookmark, Product, Review,ProductImages
from .serializers import  BookmarkSerializer, Productserializer, ReviewSerializer
from rest_framework.mixins import CreateModelMixin, DestroyModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.permissions import AllowAny, DjangoModelPermissions, DjangoModelPermissionsOrAnonReadOnly, IsAdminUser, IsAuthenticated
from .permissions import Agencepermission
from rest_framework import generics


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = Productserializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = ProductFilter
    search_fields = ['title', 'description']
    ordering_fields = ['price', 'last_update']
    def get_serializer_context(self):
        return {'request': self.request}











    # def create(self, validated_data):
    #      images_data = self.context['request'].FILES
    #      Product = Product.objects.create
    #      for image_data in images_data.getlist('file'):
    #          ProductImages.objects.create(Product=Product, image=image_data)










class ProductByOwnerViewSet(ModelViewSet):
    serializer_class = Productserializer
    filterset_class = ProductFilter
    def get_queryset(self):
        user = self.request.user.id
        return Product.objects.filter(owner=user)
    def get_serializer_context(self):
        return {'request': self.request}





class ReviewViewSet(ModelViewSet):
    serializer_class = ReviewSerializer

    def get_queryset(self):
        return Review.objects.filter(product_id=self.kwargs['product_pk'])

    def get_serializer_context(self):
        return {'product_id': self.kwargs['product_pk'],
        'request': self.request
        }


class RecipeBookmarkView(ModelViewSet):
    serializer_class = BookmarkSerializer
    def get_queryset(self):
        return Bookmark.objects.filter(bookmarked_by=self.request.user)
