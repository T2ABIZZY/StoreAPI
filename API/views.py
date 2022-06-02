from django.db.models.aggregates import Count
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from requests import request
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.decorators import action
from rest_framework import status
from .filters import OfferFilter
from .models import  Bookmark, Offer, Comment
from .serializers import  BookmarkSerializer, offerserializer, CommentSerializer
from rest_framework.mixins import CreateModelMixin, DestroyModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.permissions import AllowAny, DjangoModelPermissions, DjangoModelPermissionsOrAnonReadOnly, IsAdminUser, IsAuthenticated
from .permissions import Agencepermission
from rest_framework import generics


class offerViewSet(ModelViewSet):
    queryset = Offer.objects.all()
    serializer_class = offerserializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = OfferFilter
    search_fields = ['title', 'description']
    ordering_fields = ['price', 'last_update']
    def get_serializer_context(self):
        return {'request': self.request}











    # def create(self, validated_data):
    #      images_data = self.context['request'].FILES
    #      offer = offer.objects.create
    #      for image_data in images_data.getlist('file'):
    #          offerImages.objects.create(offer=offer, image=image_data)










class offerByOwnerViewSet(ModelViewSet):
    serializer_class = offerserializer
    filterset_class = OfferFilter
    def get_queryset(self):
        user = self.request.user.id
        return Offer.objects.filter(owner=user)
    def get_serializer_context(self):
        return {'request': self.request}





class CommentViewSet(ModelViewSet):
    serializer_class = CommentSerializer

    def get_queryset(self):
        return Comment.objects.filter(Offer_id=self.kwargs['offer_pk'])

    def get_serializer_context(self):
        return {'Offer_id': self.kwargs['offer_pk'],
        'request': self.request
        }


class RecipeBookmarkView(ModelViewSet):
    serializer_class = BookmarkSerializer
    def get_queryset(self):
        return Bookmark.objects.filter(bookmarked_by=self.request.user)
    def get_serializer_context(self):
        return {'request': self.request}