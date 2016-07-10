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
from django.conf.urls import url
from django.contrib import admin

import csa.views
import csa.views.access

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', csa.views.index, name='index'),
    url(r'^user/login/', csa.views.access.user_login, name='user-login'),
    url(r'^user/logout/', csa.views.access.user_logout, name='user-logout')
]