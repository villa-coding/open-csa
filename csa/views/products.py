from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from csa.models.core import Product


@login_required
def index(request):
    products = Product.objects.all()

    return render(request, 'products/index.html', {
        'products': products
    })
