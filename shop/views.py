from django.db import models
from django.db.models import Q
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend

from .models import Product, Category, ProductImages
from .serializers import (ProductListSerializer, ProductDetailSerializer,
                          ReviewCreateSerializer, CreateRatingSerializer,
                          CategorySerializer, ProductImageSerializer
                          )

from .service import get_client_ip, ProductFilter, ImageProductFilter


class CategoryView(generics.ListAPIView):
    """Category"""
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class ProductListView(generics.ListAPIView):
    """Сonclusion list products"""
    serializer_class = ProductListSerializer
    permission_classes = [permissions.IsAuthenticated]

    # Connecting filters in Django
    filter_backends = (DjangoFilterBackend,)
    filterset_class = ProductFilter

    def get_queryset(self):
        products = Product.objects.filter(draft=False).annotate(
            rating_user=models.Count("ratings", filter=models.Q(ratings__ip=get_client_ip(self.request)))
        ).annotate(
            middle_star=models.Sum(models.F("ratings__star")) / models.Count(models.F("ratings"))
        )

        query = self.request.GET.get("f")
        if query:
            print(query)
            products = products.filter(category__in=query)

        return products


class ProductDetailView(generics.RetrieveAPIView):
    """Сonclusion detail product"""
    queryset = Product.objects.filter(draft=False)
    serializer_class = ProductDetailSerializer


class ProductImageView(generics.ListAPIView):
    """Images Product"""
    queryset = ProductImages.objects.all()
    serializer_class = ProductImageSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = ImageProductFilter


class ReviewCreateView(generics.CreateAPIView):
    """Create reviews"""
    serializer_class = ReviewCreateSerializer


class AddRatingView(generics.CreateAPIView):
    """Add rating"""
    serializer_class = CreateRatingSerializer

    def perform_create(self, serializer):
        serializer.save(ip=get_client_ip(self.request))
