from django.urls import path
from products.views import (ProductView, ProductCategoryView, ProductDetailView)

app_name = 'products'

urlpatterns = [
    path('', ProductView.as_view(), name='products'),
    path('<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('categories/<int:pk>/', ProductCategoryView.as_view(), name='category'),
]
