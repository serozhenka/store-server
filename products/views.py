from django.shortcuts import render, HttpResponseRedirect
from products.models import Product, ProductCategory, Basket
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

def index(request):
    context = {
        'title': 'Store',
    }
    return render(request, 'products/index.html', context)

def products(request, category_id=None, page=1):
    context = {'title': 'Products', 'categories': ProductCategory.objects.all()}
    if category_id:
        productsList = Product.objects.filter(category_id=category_id)
    else:
        productsList = Product.objects.all()

    paginator = Paginator(productsList, 3)
    products_paginator = paginator.page(page)
    context.update({'products': products_paginator})

    return render(request, 'products/products.html', context)

@login_required
def basket_add(request, product_id):
    product = Product.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user, product=product)

    if not baskets.exists():
        Basket.objects.create(user=request.user, product=product, quantity=1)
    else:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def basket_delete(request, id):
    basket = Basket.objects.get(id=id)
    basket.delete()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
