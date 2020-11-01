from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Product
from .serializers import ProductListSerializer, ProductDetailSerializer, ReviewCreateSerializer


class ProductListView(APIView):
    """Сonclusion list products"""

    def get(self, request):
        products = Product.objects.filter(draft=False)
        serializer = ProductListSerializer(products, many=True)
        return Response(serializer.data)


class ProductDetailView(APIView):
    """Сonclusion detail product"""

    def get(self, request, pk):
        product = Product.objects.get(id=pk)
        serializer = ProductDetailSerializer(product)
        return Response(serializer.data)


class ReviewCreateView(APIView):
    """Create reviews"""

    def post(self, request):
        review = ReviewCreateSerializer(data=request.data)
        if review.is_valid():
            review.save()
        return Response(status=200)
