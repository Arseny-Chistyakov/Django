from django.shortcuts import render

from products.models import ProductCategory, Product


def index(request):
    context = {"title": "geekShop"}
    return render(request, "products/index.html", context=context)


def products(request):
    context = {
        "title": "GeekShop - Каталог",
        "productcategory": ProductCategory.objects.all(),
        "products": Product.objects.all()
    }
    return render(request, "products/products.html", context=context)
