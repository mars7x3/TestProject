from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets, generics, status

from crud_app.models import Category, Color, Product
from crud_app.serializers import CategorySerializer, ColorSerializer, ProductListSerializer, ProductDetailSerializer
from crud_app.utils import create_product_images, delete_product_images


class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ColorListView(generics.ListAPIView):
    queryset = Color.objects.all()
    serializer_class = ColorSerializer


class ProductCRUDView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer

    def get_serializer_class(self):
        if self.action == 'list':
            return ProductListSerializer
        else:
            return self.serializer_class


class ProductImageView(APIView):
    def post(self, request):
        product_id = request.data.get('product_id')
        create_files = request.FILES.getlist('files_to_create')
        delete_files = request.data.getlist('files_to_delete')
        create_product_images(product_id, create_files)
        delete_product_images(product_id, delete_files)
        return Response('Success!', status=status.HTTP_200_OK)




