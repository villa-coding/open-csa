"""csa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from registration.backends.hmac.views import RegistrationView

import csa.views
import csa.forms.access
import csa.views.admin.user
import csa.views.products
import csa.views.cart


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^admin/users/(?P<user_id>\d+)/deposit_by_hand',
        csa.views.admin.user.deposit_by_hand,
        name='admin-user-deposit-by-hand'),
    url(r'^user/register/$',
        RegistrationView.as_view(
            form_class=csa.forms.access.RegistrationForm
        ),
        name='user-register',
    ),
    url(r'^user/', include('registration.backends.hmac.urls')),

    url(r'^$', csa.views.index, name='index'),
    url(r'^products/$', csa.views.products.index, name='products-index'),
    url(r'^user/cart/$', csa.views.cart.index, name='cart-index'),
    url(r'^user/cart/add', csa.views.cart.add, name='cart-add')
]
