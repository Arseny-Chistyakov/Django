from django.shortcuts import render


def index(request):
    context = {'title': 'GeekShop'}
    return render(request, 'products/index.html', context)


def products(request):
    context = {'title': 'GeekShop - Продукты'}
    return render(request, 'products/products.html', context)
