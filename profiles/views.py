from django.db.models import Count
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from locations_api.permissions import IsOwnerOrReadOnly
from .models import Profile
from .serializers import ProfileSerializer


class ProfileList(generics.ListAPIView):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.annotate()
    #filter_backends = [
    #    filters.OrderingFilter,
    #    DjangoFilterBackend
    #]
    #ordering_fields = ['posts_count']


class ProfileDetail(generics.RetrieveUpdateAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = ProfileSerializer
    #queryset = Profile.objects.annotate(
    #    posts_count=Count('owner__post', distinct=True),
    #).order_by('-created_at')