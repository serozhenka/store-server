from django.shortcuts import render

def index(request):
    context = {
        'title': 'Store',
    }
    return render(request, 'products/index.html', context)

def products(request):
    context = {
        'title': 'Products',
    }
    return render(request, 'products/products.html', context)

def test_context(request):
    context = {
        'title': 'store',
        'header': 'Welcome',
        'username': 'Johnny Armless',
        'products': [
            {'name': 'Худи черного цвета с монограммами adidas Originals', 'price': 6090.00},
            {'name': 'Синяя куртка The North Face', 'price': 23725.00},
            {'name': 'Коричневый спортивный oversized-топ ASOS DESIGN', 'price': 3390.00},
        ],
        # 'sale': True,
        'products_on_sale': [
            {'name': 'Черный рюкзак Nike Heritage', 'price': 2340.00},
        ]
    }
    return render(request, 'products/test-context.html', context)

