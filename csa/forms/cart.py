from django import forms


class AddProductForm(forms.Form):
    stock_id = forms.IntegerField(widget=forms.HiddenInput())
    quantity = forms.FloatField(initial=1)
