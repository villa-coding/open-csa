from functools import partial
from django.db import models
from django.contrib.auth.models import User


# wrap CharField to our own class that defaults to max_length 512
# for ease of use and consistency
CSACharField = partial(models.CharField, max_length=512)


class Product(models.Model):
    pass


class ProductCategory(models.Model):
    # set proper plural name
    class Meta:
        verbose_name_plural = "product categories"

    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    name = CSACharField(unique=True)
    description = CSACharField(blank=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    pass


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # add more fields here


class Producer(models.Model):
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE)


class Consumer(models.Model):
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
