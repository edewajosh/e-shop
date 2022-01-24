from pyexpat import model
from django.shortcuts import render

from django.views.generic import (ListView, CreateView)

from products.models import Category, Product


class CategoryView(ListView):
    model = Category
    template_name = 'products/index.html'
    context_object_name = 'categories'

class ProductView(ListView):
    model = Product
    template_name = 'products/index.html'
    context_object_name = 'products'