from django.contrib.auth.decorators import login_required
from django.shortcuts import HttpResponseRedirect
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.contrib import messages

from baskets.models import Basket
from products.models import Product


@login_required
def basket_add(request, product_id):
    if request.is_ajax():
        product = Product.objects.get(id=product_id)
        baskets = Basket.objects.filter(user=request.user, product=product)

        if not baskets:
            Basket.objects.create(user=request.user, product=product, quantity=1)
        else:
            basket = baskets.first()
            if basket.quantity <= product.quantity:
                basket.quantity += 1
                basket.save()
                # return HttpResponseRedirect(request.META['HTTP_REFERER'])
            else:
                messages.error(request, 'omg')
        baskets = Basket.objects.filter(user=request.user)
        context = {"baskets": baskets}
        result = render_to_string("products/products.html", context)
        return JsonResponse({"result": result})


@login_required
def basket_remove(request, id):
    basket = Basket.objects.get(id=id)
    basket.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


@login_required
def basket_edit(request, id, quantity):
    if request.is_ajax():
        basket = Basket.objects.get(id=id)
        if quantity > 0:
            basket.quantity = quantity
            basket.save()
        else:
            basket.delete()
        baskets = Basket.objects.filter(user=request.user)
        context = {"baskets": baskets}
        result = render_to_string("baskets/basket.html", context)
        return JsonResponse({"result": result})
