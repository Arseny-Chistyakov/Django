import json

from django.conf import settings
from django.shortcuts import render


def index(request):
    context = {'title': 'geekShop'}
    return render(request, 'products/index.html', context)


def products(request):
    file_path = settings.BASE_DIR /'products/fixtures/goods.json'

    context = {
        'title': 'geekShop - Продукты',
        'products': json.load(open(file_path, encoding='utf-8'))
    }
    return render(request, 'products/products.html', context)
