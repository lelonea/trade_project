from django.contrib.auth.models import AbstractUser
from django.db import models
from djmoney.models.fields import MoneyField


class User(AbstractUser):
    balance = MoneyField(max_digits=14, decimal_places=2, default=0, default_currency='USD', blank=True, null=True)


class Item(models.Model):
    code = models.CharField(max_length=8, unique=True)
    name = models.CharField(max_length=125, unique=True)

    def __str__(self):
        return self.name


class Price(models.Model):
    """An actual price on item due to date"""
    actual_price = MoneyField(max_digits=14, decimal_places=2, default_currency='USD', blank=True, null=True)
    actual_date = models.DateTimeField(unique=True, blank=True, null=True)
    item = models.ForeignKey(Item, blank=True, null=True, on_delete=models.SET_NULL,
                             related_name='prices', related_query_name='prices')


class WatchList(models.Model):
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
    item = models.ForeignKey(Item, blank=True, null=True, on_delete=models.SET_NULL)



