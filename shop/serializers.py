from rest_framework import serializers

from .models import Product, Category, Review, Rating, ProductImages


class FiletrReviewListSerializer(serializers.ListSerializer):
    """Add only review parent"""

    def to_representation(self, data):
        data = data.filter(parent=None)
        return super().to_representation(data)


class RatingStarSerializer(serializers.ModelSerializer):
    """Star"""

    class Meta:
        model = Rating
        fields = ("star",)


class RecursiveSerializer(serializers.Serializer):
    """recursive children"""

    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data


class ReviewCreateSerializer(serializers.ModelSerializer):
    """Create reviews"""

    class Meta:
        model = Review
        fields = "__all__"


class ReviewSerializer(serializers.ModelSerializer):
    children = RecursiveSerializer(many=True)

    class Meta:
        list_serializer_filter_class = FiletrReviewListSerializer
        model = Review
        fields = ("email", "name", "text", "children")


class CategorySerializer(serializers.ModelSerializer):
    """Serializer Category"""

    class Meta:
        model = Category
        fields = "__all__"


class ProductListSerializer(serializers.ModelSerializer):
    """List Products"""
    category = serializers.SlugRelatedField(slug_field="name", read_only=True)
    rating_user = serializers.BooleanField()
    middle_star = serializers.IntegerField()

    class Meta:
        model = Product
        fields = ("category", "name", "description", "price", "rating_user", "middle_star")


class ProductImageSerializer(serializers.ModelSerializer):
    """Product Images"""
    product = serializers.SlugRelatedField(slug_field="name", read_only=True)

    class Meta:
        model = ProductImages
        fields = "__all__"


class ProductDetailSerializer(serializers.ModelSerializer):
    """Detail Products"""
    category = serializers.SlugRelatedField(slug_field="name", read_only=True)
    reviews = ReviewSerializer(many=True)
    product_images = ProductImageSerializer(many=True)
    ratings = RatingStarSerializer(many=True)

    class Meta:
        model = Product
        exclude = ("draft",)


class CreateRatingSerializer(serializers.ModelSerializer):
    """Create rating"""

    class Meta:
        model = Rating
        fields = ("star", "product")

    def create(self, validated_data):
        rating, _ = Rating.objects.update_or_create(
            ip=validated_data.get("ip", None),
            product=validated_data.get("product", None),
            defaults={"star": validated_data.get("star")}
        )
        return rating
