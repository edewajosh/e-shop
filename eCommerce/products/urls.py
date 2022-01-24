from django.urls import path
from products.views import (ProductView, CategoryView)
urlpatterns = [
    path('products/', ProductView.as_view()),
    path('categories/', CategoryView.as_view()),
]
