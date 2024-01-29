from rest_framework import generics
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from retail.models import Retail
from retail.paginators import CustomPaginator
from retail.serializers import RetailSerializer, RetailListSerializer, RetailUpdateSerializer
from users.permissions import IsActive


class RetailCreateAPIView(generics.CreateAPIView):
    """ Создание компании """

    serializer_class = RetailSerializer
    permission_classes = [IsActive]


class RetailListAPIView(generics.ListAPIView):
    """ Вывод списка компаний """

    serializer_class = RetailListSerializer
    pagination_class = CustomPaginator

    permission_classes = [IsActive]

    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('company_country',)
    ordering_fields = ['company_country']

    def get_queryset(self):

        queryset = Retail.objects.all()
        return queryset


class RetailRetrieveAPIView(generics.RetrieveAPIView):
    """ Вывод информации по одной компании """

    serializer_class = RetailListSerializer
    queryset = Retail.objects.all()
    permission_classes = [IsActive]


class RetailUpdateAPIView(generics.UpdateAPIView):
    """ Изменение компании """

    serializer_class = RetailUpdateSerializer
    queryset = Retail.objects.all()
    permission_classes = [IsActive]


class RetailDestroyAPIView(generics.DestroyAPIView):
    """ Удаление компании """

    queryset = Retail.objects.all()
    permission_classes = [IsActive]
