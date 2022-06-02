from django_filters.rest_framework import FilterSet
from .models import Offer

class OfferFilter(FilterSet):
    class Meta:
        model = Offer
        fields = {
            'price': ['lt','gt'],
            'categories': ['exact'],
            'whatfor': ['exact'],
        }