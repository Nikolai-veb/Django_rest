from rest_framework import serializers

from .models import Product, Category, Review


class ReviewCreateSerializer(serializers.ModelSerializer):
    """Create reviews"""

    class Meta:
        model = Review
        fields = "__all__"


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ("email", "name", "text", "parent")


class ProductListSerializer(serializers.ModelSerializer):
    """List Products"""
    category = serializers.SlugRelatedField(slug_field="name", read_only=True)

    class Meta:
        model = Product
        fields = ("category", "name", "description")


class ProductDetailSerializer(serializers.ModelSerializer):
    """Detail Products"""
    category = serializers.SlugRelatedField(slug_field="name", read_only=True)
    reviews = ReviewSerializer(many=True)

    class Meta:
        model = Product
        exclude = ("draft",)
