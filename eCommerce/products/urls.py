from unicodedata import name
from django.urls import path
from products.views import (ProductView, CategoryView, ProductDetailView)
urlpatterns = [
    path('products/', ProductView.as_view(), name='products'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('categories/', CategoryView.as_view(), name='category'),
]
