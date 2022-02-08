from itertools import product
from pyexpat import model
from django.shortcuts import render

from django.views.generic import (ListView, DetailView)

from products.models import Category, Product

from cart.forms import CartAddProductForm


class CategoryView(ListView):
    model = Category
    template_name = 'products/index.html'
    context_object_name = 'categories'

class ProductView(ListView):
    model = Product
    template_name = 'products/index.html'
    context_object_name = 'products'

class ProductDetailView(DetailView):
    model = Product
    cart_product_form = CartAddProductForm
    template_name = 'products/product_detail.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        context['cart_product_form'] = CartAddProductForm
        return context