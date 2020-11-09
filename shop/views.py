from django.db import models
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend

from .models import Product
from .serializers import ProductListSerializer, ProductDetailSerializer, ReviewCreateSerializer, CreateRatingSerializer
from .service import get_client_ip, ProductFilter


class ProductListView(generics.ListAPIView):
    """Сonclusion list products"""
    serializer_class = ProductListSerializer
    permission_classes = [permissions.IsAuthenticated]
    # Connecting filters in Django
    # filter_backends = (DjangoFilterBackend)
    # filterset_class = ProductFilter

    def get_queryset(self):
        products = Product.objects.filter(draft=False).annotate(
            rating_user=models.Count("ratings", filter=models.Q(ratings__ip=get_client_ip(self.request)))
        ).annotate(
            middle_star=models.Sum(models.F("ratings__star")) / models.Count(models.F("ratings"))
        )

        return products


class ProductDetailView(generics.RetrieveAPIView):
    """Сonclusion detail product"""
    queryset = Product.objects.filter(draft=False)
    serializer_class = ProductDetailSerializer


class ReviewCreateView(generics.CreateAPIView):
    """Create reviews"""
    serializer_class = ReviewCreateSerializer


class AddRatingView(generics.CreateAPIView):
    """Add rating"""
    serializer_class = CreateRatingSerializer

    def perform_create(self, serializer):
        serializer.save(ip=get_client_ip(self.request))
