from django_filters import rest_framework as filters
from shop.models import Product, ProductImages


def get_client_ip(request):
    x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get("REMOTE_ADDR")
    return ip


class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    pass


class IntegerInFilter(filters.BaseInFilter, filters.NumberFilter):
    pass


class ProductFilter(filters.FilterSet):
    category = CharFilterInFilter(field_name='category__name', lookup_expr='in')
    price = filters.RangeFilter()
    ratings = IntegerInFilter(field_name='ratings__star', lookup_expr='in')

    class Meta:
        model = Product
        fields = ['category', 'price', 'ratings']


class ImageProductFilter(filters.FilterSet):
    """Filter Images Product"""
    product = CharFilterInFilter(field_name='product__name', lookup_expr='in')

    class Meta:
        model = ProductImages
        fields = ["product"]
