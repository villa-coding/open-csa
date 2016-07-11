from functools import partial
from django.db import models
from django.contrib.auth.models import User


# wrap CharField to our own class that defaults to max_length 512
# for ease of use and consistency
CSACharField = partial(models.CharField, max_length=512)


class ProductCategory(models.Model):
    # set proper plural name
    class Meta:
        verbose_name_plural = "product categories"

    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    name = CSACharField(unique=True)
    description = CSACharField(blank=True)

    def __str__(self):
        return self.name


class ProductMeasureUnit(models.Model):
    name = CSACharField()


# TODO: how to handle varieties in terms of container size?
class Product(models.Model):
    categories = models.ManyToManyField(ProductCategory)
    name = CSACharField()
    description = models.TextField()
    unit = models.ForeignKey(ProductMeasureUnit)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # add more fields here


class Producer(models.Model):
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE)


# TODO: keep log of these for stats of price changes
class ProductStock(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    producer = models.OneToOneField(Producer, on_delete=models.CASCADE)
    # TODO: add non-negative validator
    quantity = models.IntegerField()
    price = models.IntegerField()
    # extra description for specific product from producer
    description = models.TextField()


class Order(models.Model):
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class OrderItem(models.Model):
    # TODO: on_delete what?
    product = models.ForeignKey(Product)
    quantity = models.FloatField()
    order = models.ForeignKey(Order, related_name='items')



class Consumer(models.Model):
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    # TODO: on_delete what?
    order = models.OneToOneField(Order)
