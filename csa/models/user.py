from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from csa.models.utils import CSACharField
from registration.signals import user_registered


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = CSACharField()
    last_name = CSACharField()
    phone_number = PhoneNumberField()


class Producer(models.Model):
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE)


class Consumer(models.Model):
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE)


def user_registered_callback(sender, user, request, **kwargs):
    profile = UserProfile(user=user)
    for attr in ['first_name', 'last_name', 'phone_number']:
        setattr(profile, attr, request.POST[attr])

    profile.save()

user_registered.connect(user_registered_callback)
