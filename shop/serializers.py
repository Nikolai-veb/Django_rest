from rest_framework import serializers

from .models import Product


class ProductListSerializer(serializers.ModelSerializer):
    """List Products"""

    class Meta:
        model = Product
        field = ("category", "name", "discription"
                 )


class ProductDetailSerializer(serializers.ModelSerializer):
    """Detail Products"""
    category = serializers.SlugRelatedField(slug_field="name", read_only=True)

    class Meta:
        model = Product
        exclude = ("draft",)