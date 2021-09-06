from django.contrib.auth.models import AbstractUser
from django.db import models
from djmoney.models.fields import MoneyField


class User(AbstractUser):
    """Current user"""
    balance = MoneyField(max_digits=14, decimal_places=2, default=0, default_currency='USD')


class Item(models.Model):
    """Particular stock"""
    code = models.CharField(max_length=8, unique=True)
    name = models.CharField(max_length=125, unique=True)
    price = MoneyField(max_digits=14, decimal_places=2, default_currency='USD', blank=True, null=True)

    def __str__(self):
        return self.name


class Price(models.Model):
    """An actual price on item due to date"""
    actual_price = MoneyField(max_digits=14, decimal_places=2, default_currency='USD', blank=True, null=True)
    actual_date = models.DateTimeField(auto_now=True)
    item = models.ForeignKey(Item, blank=True, null=True, on_delete=models.SET_NULL,
                             related_name='prices', related_query_name='prices')


class WatchList(models.Model):
    """Favorite list of stocks belongs to user"""
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL,
                             related_name='user_watchlist', related_query_name='user_watchlist')
    item = models.ForeignKey(Item, blank=True, null=True, on_delete=models.SET_NULL,
                             related_name='item_watchlist', related_query_name='item_watchlist')


class Offer(models.Model):
    """request to buy or sell specific stocks"""
    ORDER_TYPE = (
        (1, 'Sell'),
        (2, 'Buy'),
    )

    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL,
                             related_name='user_offer', related_query_name='user_offer')
    item = models.ForeignKey(Item, blank=True, null=True, on_delete=models.SET_NULL,
                             related_name='item_offer', related_query_name='item_offer')
    order_type = models.PositiveSmallIntegerField(choices=ORDER_TYPE)
    entry_quantity = models.IntegerField('Requested quantity')
    quantity = models.IntegerField('Current quantity')
    price = MoneyField(max_digits=14, decimal_places=2, default_currency='USD')
    is_active = models.BooleanField(default=True)
    date_and_time = models.DateTimeField(auto_now_add=True)


class Trade(models.Model):
    """Information about a certain transaction"""
    item = models.ForeignKey(Item, blank=True, null=True, on_delete=models.SET_NULL)
    quantity = models.IntegerField(default=0)
    unit_price = MoneyField(max_digits=14, decimal_places=2, default_currency='USD', blank=True, null=True)
    seller = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL,
                               related_name='seller_trade', related_query_name='seller_trade')
    buyer = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL,
                              related_name='buyer_trade', related_query_name='buyer_trade')
    seller_offer = models.ForeignKey(Offer, blank=True, null=True, on_delete=models.SET_NULL,
                                     related_name='seller_trade', related_query_name='seller_trade')
    buyer_offer = models.ForeignKey(Offer, blank=True, null=True, on_delete=models.SET_NULL,
                                    related_name='buyer_trade', related_query_name='buyer_trade')
    description = models.TextField(blank=True, null=True)
    date_and_time = models.DateTimeField(auto_now_add=True)


class Inventory(models.Model):
    """The number of stocks a particular user has"""
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
    item = models.ForeignKey(Item, blank=True, null=True, on_delete=models.SET_NULL)
    quantity = models.IntegerField("Stock quantity", default=0)
