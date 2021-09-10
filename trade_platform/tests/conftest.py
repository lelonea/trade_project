import random
import pytest
from faker import Faker
from mixer.backend.django import mixer
from trade.models import Item, Inventory, User, Offer, Price, Trade, WatchList
from rest_framework.test import APIClient


@pytest.fixture(autouse=True)
def access_db(db):
    pass


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def item_data():
    faker = Faker()
    data = {
        'code': faker.text()[:6],
        'name': faker.name(),
        'price': random.randint(0, 1_000_000),
        'price_currency': random.choice(('XUA', 'USD')),
    }
    return data


@pytest.fixture
def item_obj(item_data):
    return Item.objects.create(**item_data)


@pytest.fixture
def inventory_obj(client):
    user = mixer.blend(User)
    client.force_authenticate(user=user)
    obj = mixer.blend(Inventory, user=user)
    return obj


@pytest.fixture
def inventory_data(inventory_obj):
    data = {
        'user': inventory_obj.user,
        'item': inventory_obj.item,
        'quantity': inventory_obj.quantity,
    }
    return data


@pytest.fixture
def offer_obj(client):
    user = mixer.blend(User)
    client.force_authenticate(user=user)
    obj = mixer.blend(Offer, user=user)
    return obj


@pytest.fixture
def offer_data(offer_obj):
    data = {
        'user': offer_obj.user,
        'item': offer_obj.item,
        'order_type': offer_obj.order_type,
        'entry_quantity': offer_obj.entry_quantity,
        'quantity': offer_obj.quantity,
        'price': offer_obj.price,
    }
    return data


@pytest.fixture
def price_obj(client):
    user = mixer.blend(User)
    client.force_authenticate(user=user)
    obj = mixer.blend(Price, user=user)
    return obj


@pytest.fixture
def price_data(price_obj):
    data = {
        'item': price_obj.item,
        'actual_price': price_obj.actual_price,
        'actual_date': price_obj.actual_date,
    }
    return data

@pytest.fixture
def trade_obj(client):
    user = mixer.blend(User)
    client.force_authenticate(user=user)
    obj = mixer.blend(Trade, user=user)
    return obj


@pytest.fixture
def trade_data(trade_obj):
    data = {
        'item': trade_obj.item,
        'quantity': trade_obj.quantity,
        'unit_trade': trade_obj.unit_price,
        'seller': trade_obj.seller,
        'buyer': trade_obj.buyer,
        'description': trade_obj.description,
        'date_and_time': trade_obj.date_and_time,
    }
    return data

@pytest.fixture
def watchlist_obj(client):
    user = mixer.blend(User)
    client.force_authenticate(user=user)
    obj = mixer.blend(WatchList, user=user)
    return obj


@pytest.fixture
def watchlist_data(watchlist_obj):
    data = {
        'user': watchlist_obj.user,
        'item': watchlist_obj.item,
    }
    return data


@pytest.fixture
def user_obj(client):
    obj = mixer.blend(User)
    client.force_authenticate(user=obj)
    return obj


@pytest.fixture
def user_data(user_obj):
    data = {
        'username': user_obj.username,
        'first_name': user_obj.first_name,
        'last_name': user_obj.last_name,
        'balance': user_obj.balance,
        'password': user_obj.password,
        'email': user_obj.email,
    }
    return data


@pytest.fixture
def fake_user_data():
    faker = Faker()
    data = {'username': faker.text().replace(' ', '')[:10],
            'password': faker.text().replace(' ', '')[:10],
            'balance': random.randint(0, 10_000_000)}
    return data
