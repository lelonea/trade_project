import random
import pytest
from faker import Faker
from mixer.backend.django import mixer
from trade.models import Item, Inventory, User
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
