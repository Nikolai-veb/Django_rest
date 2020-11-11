from django.db import models
from django.db.models import Q
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Tag, Article, Comment
from .serializers import TagSerializer, ArticleSerializer, ArticleDetailSerializer

class TagView(generics.ListAPIView):
    """View Tags"""
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

class ArticleView(generics.ListAPIView):
    """View Articles"""
    queryset = Article.objects.filter(draft=False)
    serializer_class = ArticleSerializer


class ArticleDetailView(generics.RetrieveAPIView):
    """View Articles"""
    queryset = Article.objects.filter(draft=False)
    serializer_class = ArticleDetailSerializer
