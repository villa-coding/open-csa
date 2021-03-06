from django.db import models
from csa.models.user import User


class Account(models.Model):
    class Meta:
        unique_together = (('type', 'user'),)

    # TODO: change this to "POCKET" account or something
    TYPE_ASSET_BANK_ACCOUNT = 1
    TYPE_LIABILITY_USER_BALANCE = 2

    TYPES = (
        (TYPE_ASSET_BANK_ACCOUNT, 'Asset Bank Account'),
        (TYPE_LIABILITY_USER_BALANCE, 'Liability User Balance'),
    )

    type = models.IntegerField(choices=TYPES)
    user = models.ForeignKey(User)


class Transaction(models.Model):
    TYPE_CONSUMER_PURCHASE = 1
    TYPE_PRODUCER_PAYMENT = 2

    TYPES = (
        (TYPE_CONSUMER_PURCHASE, 'Consumer Purchase'),
        (TYPE_PRODUCER_PAYMENT, 'Producer Payment')
    )

    type = models.IntegerField(choices=TYPES)
    description = models.TextField()
    amount = models.PositiveIntegerField()


class LedgerEntry(models.Model):
    class Meta:
        unique_together = (('transaction', 'account'))

    TYPE_DEBIT = 1
    TYPE_CREDIT = 2
    TYPES = (
        (TYPE_DEBIT, 'Debit'),
        (TYPE_CREDIT, 'Credit')
    )

    type = models.IntegerField(choices=TYPES)
    account = models.ForeignKey(Account)
    transaction = models.ForeignKey(Transaction)
    amount = models.PositiveIntegerField()
