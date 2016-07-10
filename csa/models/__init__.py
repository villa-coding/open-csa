# import models to get them registered
import csa.models.core

from django.contrib import admin
from django.apps import apps

app = apps.get_app_config('csa')
for model_name, model in app.models.items():
    admin.site.register(model)
