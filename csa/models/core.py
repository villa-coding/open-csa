from django.db import models
from csa.models.user import Producer, Consumer, User
from csa.models.utils import CSACharField


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

    def __str__(self):
        return self.name


# TODO: how to handle container size?
class Product(models.Model):
    categories = models.ManyToManyField(ProductCategory)
    name = CSACharField(unique=True)
    description = models.TextField()
    unit = models.ForeignKey(ProductMeasureUnit)

    def __str__(self):
        return self.name


# TODO: keep log of these for stats of price changes
class ProductStock(models.Model):
    product = models.ForeignKey(
        Product,
        related_name='stocks',
        on_delete=models.CASCADE)

    producer = models.OneToOneField(User, on_delete=models.CASCADE)
    variety = CSACharField()
    quantity = models.PositiveIntegerField()
    price = models.PositiveIntegerField()
    # extra description for specific product from producer
    description = models.TextField()


class Order(models.Model):
    # TODO: on_delete what?
    consumer = models.OneToOneField(Consumer)
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class OrderItem(models.Model):
    # TODO: on_delete what?
    # TODO: product or product stock? crutial logic decision
    product = models.ForeignKey(Product)
    quantity = models.FloatField()
    order = models.ForeignKey(Order, related_name='items')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
