from django.db import models
from django.db.models import Q
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from  django_filters.rest_framework import  DjangoFilterBackend
from .models import Tag, Article, Comment
from .serializers import TagSerializer, ArticleSerializer, ArticleDetailSerializer, CommentCreateSerializer
from .service import ArticleFilter


class TagView(generics.ListAPIView):
    """View Tags"""
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class ArticleView(generics.ListAPIView):
    """View Articles"""
    queryset = Article.objects.filter(draft=False)
    serializer_class = ArticleSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = ArticleFilter


class ArticleDetailView(generics.RetrieveAPIView):
    """View Articles"""
    queryset = Article.objects.filter(draft=False)
    serializer_class = ArticleDetailSerializer


class CommentCreateView(APIView):
    """Add comments for article"""

    def post(self, request):
        comment = CommentCreateSerializer(data=request.data)
        if comment.is_valid():
            comment.save()
        return Response(status=200)
