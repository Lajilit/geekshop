import json
import os

from django.shortcuts import render

from products.models import ProductCategory, Product

MODULE_DIR = os.path.dirname(__file__)


def index(request):
    context = {
        'title': 'GeekShop',
    }
    return render(request, 'products/index.html', context)


def products(request):
    categories = ProductCategory.objects.all()
    products = Product.objects.all()

    context = {
        'title': 'товары',
        'products': products,
        'categories': categories,
    }

    return render(request, 'products/products.html', context)
