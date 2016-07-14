from django.shortcuts import render
from csa.forms.products import ProductForm


def add_product(request):
    if request.method == 'GET':
        form = ProductForm()

    return render(request, 'products/add.html', {
        'form': form
    })
