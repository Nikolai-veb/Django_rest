from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Product
from .serializers import ProductListSerializer, ProductDetailSerializer


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
        serializer = ProductListSerializer(product)
        return Response(serializer.data)