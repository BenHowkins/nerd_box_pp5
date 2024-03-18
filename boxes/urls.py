from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('<product_sku>', views.product_detail, name='product_detail'),
]
