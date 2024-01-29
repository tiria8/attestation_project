from django.urls import path

from retail.apps import RetailConfig
from retail.views import RetailCreateAPIView, RetailListAPIView, RetailRetrieveAPIView, RetailUpdateAPIView, \
    RetailDestroyAPIView

app_name = RetailConfig.name


urlpatterns = [
    path('create/', RetailCreateAPIView.as_view(), name='company_create'),
    path('list/', RetailListAPIView.as_view(), name='company_list'),
    path('company/<int:pk>/', RetailRetrieveAPIView.as_view(), name='company_detail'),
    path('update/<int:pk>/', RetailUpdateAPIView.as_view(), name='company_update'),
    path('delete/<int:pk>/', RetailDestroyAPIView.as_view(), name='company_delete'),
]
