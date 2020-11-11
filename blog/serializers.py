from rest_framework import serializers
from .models import Article, Tag, Comment


class TagSerializer(serializers.ModelSerializer):
    """Serializer Teg"""

    class Meta:
        model = Tag
        fields = "__all__"


class ArticleSerializer(serializers.ModelSerializer):
    """Serializer Article"""
    #tags = serializers.SlugRelatedField(slug_field="name", read_only=True)

    class Meta:
        model = Article
        fields = ("user", "title", "tags")


class ArticleDetailSerializer(serializers.ModelSerializer):
    """Serializer Article"""

    class Meta:
        model = Article
        fields = "__all__"
