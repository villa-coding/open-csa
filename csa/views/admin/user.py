from django import forms
from django.shortcuts import render, redirect
from csa.models.user import User
from csa.finance.payments import user_deposit_by_hand


class DepositByHandForm(forms.Form):
    amount = forms.FloatField()


def deposit_by_hand(request, user_id):
    selected_user = User.objects.get(pk=user_id)
    if request.method == 'POST':
        form = DepositByHandForm(request.POST)
        if form.is_valid():
            amount = form.cleaned_data['amount']
            user_deposit_by_hand(selected_user, amount)
            # TODO: dont hardcode this
            return redirect('/admin/csa/consumer/')
    else:
        form = DepositByHandForm()

    return render(request, 'admin/user/deposit_by_hand.html', {
        'form': form,
        'selected_user': selected_user
    })
