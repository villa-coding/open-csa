from django import forms
from csa.models.core import Product


class ProductForm(forms.Form):
    class Meta:
        model = Product
