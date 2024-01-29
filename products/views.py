from rest_framework import generics

from products.models import Product
from retail.paginators import CustomPaginator
from products.serializers import ProductSerializer
from users.permissions import IsActive


class ProductCreateAPIView(generics.CreateAPIView):
    """ Создание товара """

    serializer_class = ProductSerializer
    permission_classes = [IsActive]


class ProductListAPIView(generics.ListAPIView):
    """ Вывод списка товаров """

    serializer_class = ProductSerializer
    pagination_class = CustomPaginator
    permission_classes = [IsActive]

    def get_queryset(self):

        queryset = Product.objects.all()
        return queryset


class ProductRetrieveAPIView(generics.RetrieveAPIView):
    """ Вывод информации по одному товару """

    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = [IsActive]


class ProductUpdateAPIView(generics.UpdateAPIView):
    """ Изменение товара """

    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = [IsActive]


class ProductDestroyAPIView(generics.DestroyAPIView):
    """ Удаление товара """

    queryset = Product.objects.all()
    permission_classes = [IsActive]
