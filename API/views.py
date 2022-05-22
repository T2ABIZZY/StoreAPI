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
from .models import  Product, Review
from .serializers import  ProductSerializer, ReviewSerializer
from rest_framework.mixins import CreateModelMixin, DestroyModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.permissions import AllowAny, DjangoModelPermissions, DjangoModelPermissionsOrAnonReadOnly, IsAdminUser, IsAuthenticated
from .permissions import Agencepermission

from rest_framework.views import APIView

class AddProduct(APIView):

    def post(self, request):
        serializer = ProductSerializer(data=request.data, context={"user":request.user})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ViewProducts(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = ProductFilter
    search_fields = ['title', 'description']
    ordering_fields = ['price', 'last_update']



    # def get_serializer_context(self):
    #     return {'request': self.request}









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

