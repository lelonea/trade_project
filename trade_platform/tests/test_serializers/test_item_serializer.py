import pytest
from trade.serializers import ListItemSerializer, CreateItemSerializer, UpdateItemSerializer


@pytest.mark.django_db
def test_list_item_serializer(item_obj):
    fields = (
        'id',
        'code',
        'name',
        'price',
        'price_currency',
    )
    serializer = ListItemSerializer(item_obj)
    assert all([field in serializer.data for field in fields])
    assert serializer.data['name'] == item_obj.name


@pytest.mark.django_db
def test_update_item_serializer(item_data):
    fields = (
        'code',
        'name',
        'price',
    )

    serializer = UpdateItemSerializer(data=item_data)
    assert all([field in serializer.validated_data for field in fields])
    assert serializer.data['name'] == item_data.get('name')


@pytest.mark.django_db
def test_create_item_serializer(item_obj):
    fields = (
        'code',
        'name',
        'price',
        'price_currency',
    )
    serializer = CreateItemSerializer(item_obj)
    assert all([field in serializer.data for field in fields])
    assert serializer.data['name'] == item_obj.name

