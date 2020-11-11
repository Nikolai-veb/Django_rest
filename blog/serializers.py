from rest_framework import serializers
from .models import Article, Tag, Comment


class FilterCommentListSerializer(serializers.ListSerializer):
    """Filter comment only parent"""

    def to_representation(self, data):
        """ here data is our queryset"""
        data = data.filter(parent=None)
        return super().to_representation(data)


class RecursiveSerializer(serializers.Serializer):
    """Get all our children"""

    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data


class CommentCreateSerializer(serializers.ModelSerializer):
    """Create reviews"""

    class Meta:
        model = Comment
        fields = "__all__"


class CommentSerializer(serializers.ModelSerializer):
    children = RecursiveSerializer(many=True)

    class Meta:
        list_serializer_class = FilterCommentListSerializer
        model = Comment
        fields = ("email", "name", "text", "children")


class TagSerializer(serializers.ModelSerializer):
    """Serializer Teg"""

    class Meta:
        model = Tag
        fields = "__all__"


class ArticleSerializer(serializers.ModelSerializer):
    """Serializer Article"""
    user = serializers.SlugRelatedField(slug_field="username", read_only=True)
    tags = serializers.SlugRelatedField(slug_field="name", read_only=True, many=True)

    class Meta:
        model = Article
        fields = ("user", "title", "tags")


class ArticleDetailSerializer(serializers.ModelSerializer):
    """Serializer Article"""
    user = serializers.SlugRelatedField(slug_field="username", read_only=True)
    tags = serializers.SlugRelatedField(slug_field="name", read_only=True, many=True)
    comments = CommentSerializer(many=True)

    class Meta:
        model = Article
        exclude = ("draft",)
