from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.decorators import action

from .filters import OfferFilter
from .models import  Bookmark, Offer, Comment
from .serializers import  BookmarkSerializer, offerserializer, CommentSerializer



class offerViewSet(ModelViewSet):
    queryset = Offer.objects.all()
    serializer_class = offerserializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = OfferFilter
    search_fields = ['title', 'description']
    ordering_fields = ['price', 'last_update']
    def get_serializer_context(self):
        return {'request': self.request}







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
