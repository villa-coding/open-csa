from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.db.models import F
from csa.models.core import ProductStock
from csa import utils


@login_required
def index(request):
    cart = utils.get_user_cart(request.user.id)

    return render(request, 'cart/index.html', {
        'cart': cart
    })


@login_required
def add(request):
    stock_id = int(request.POST['stock_id'])
    stock = ProductStock.objects.get(pk=stock_id)
    cart = utils.get_user_cart(request.user.id)
    item, created = cart.items.get_or_create(
        product_stock=stock,
        defaults={"quantity": 1})
    if not created:
        item.quantity = F('quantity') + 1
        item.save()

    return redirect('products-index')
