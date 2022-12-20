from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from locations_api.permissions import IsOwnerOrReadOnly
from .models import Review
from .serializers import ReviewSerializer


class ReviewList(generics.ListCreateAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Review.objects.all()
    filter_backends = [
        DjangoFilterBackend
    ]
    filterset_fields = [
        'post'
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()