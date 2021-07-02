import json
import os

from django.shortcuts import render

MODULE_DIR = os.path.dirname(__file__)


def index(request):
    context = {
        'title': 'GeekShop',
    }
    return render(request, 'products/index.html', context)


def products(request):
    context = {'title': 'товары'}

    file_path_p = os.path.join(MODULE_DIR, 'fixtures/products.json')
    context['products'] = json.load(open(file_path_p, encoding='utf-8'))

    file_path_c = os.path.join(MODULE_DIR, 'fixtures/categories.json')
    context['categories'] = json.load(open(file_path_c, encoding='utf-8'))

    return render(request, 'products/products.html', context)
