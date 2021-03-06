from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render

from products.models import ProductCategory, Product


def index(request):
    context = {"title": "geekShop"}
    return render(request, "products/index.html", context=context)


def products(request, category_id=None, page=1):
    if category_id:
        products = Product.objects.filter(category_id=category_id)
    else:
        products = Product.objects.all()
    paginator = Paginator(products, 3)
    try:
        products_paginator = paginator.page(page)
    except PageNotAnInteger:
        products_paginator = paginator.page(1)
    except EmptyPage:
        products_paginator = paginator.page(paginator.num_pages)
    context = {
        "title": "GeekShop - Каталог",
        "categories": ProductCategory.objects.all(),
        "products": products_paginator,
    }
    return render(request, "products/products.html", context)
