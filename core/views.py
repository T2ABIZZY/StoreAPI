
from .serializers import userProfileSerializer,UserProfile
from rest_framework import generics
class userAccountsListView(generics.ListAPIView):

    queryset=UserProfile.objects.all()
    serializer_class=userProfileSerializer