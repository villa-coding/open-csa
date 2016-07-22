from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib import messages


def user_logout(request):
    logout(request)
    messages.success(request, 'Επιτυχής αποσύνδεση')
    return redirect('index')
