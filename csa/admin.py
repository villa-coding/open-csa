from django.contrib import admin
from django.apps import apps
from django.contrib.auth.admin import UserAdmin
from csa.models.user import User, UserProfile


# register all models
app = apps.get_app_config('csa')
for model_name, model in app.models.items():
    admin.site.register(model)


class UserProfileInline(admin.StackedInline):
    model = UserProfile


class UserProfileAdmin(UserAdmin):
    inlines = [UserProfileInline]

admin.site.unregister(User)
admin.site.register(User, UserProfileAdmin)
