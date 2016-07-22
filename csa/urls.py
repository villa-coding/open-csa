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
import csa.views.access
import csa.forms.access
import csa.views.admin.user

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^admin/users/(?P<user_id>\d+)/deposit_by_hand',
        csa.views.admin.user.deposit_by_hand,
        name='admin-user-deposit-by-hand'),
    url(r'^$', csa.views.index, name='index'),
    url(r'^user/logout/', csa.views.access.user_logout, name='user-logout'),
    url(r'^user/register/$',
        RegistrationView.as_view(
            form_class=csa.forms.access.RegistrationForm
        ),
        name='user-register',
    ),
    url(r'^user/', include('registration.backends.hmac.urls'))
]
