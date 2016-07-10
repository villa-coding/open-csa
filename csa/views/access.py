from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.contrib import messages


def user_login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            messages.success(request, 'Επιτυχής σύνδεση')
        else:
            # TODO: how to handle this?
            raise Exception()

        return redirect('index')
    else:
        messages.warning(
            request,
            'Λάθος στοιχεία.')
        return redirect('index')


def user_logout(request):
    logout(request)
    messages.success(request, 'Επιτυχής αποσύνδεση')
    return redirect('index')
