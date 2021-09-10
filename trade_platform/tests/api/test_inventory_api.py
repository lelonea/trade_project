import pytest
from rest_framework import status
from rest_framework.reverse import reverse
from trade.serializers import ListInventorySerializer, UpdateInventorySerializer, CreateInventorySerializer
from trade.models import Inventory


@pytest.mark.django_db
def test_get_inventory_list_request(client, inventory_obj):
    url = reverse('trade:inventory-list')
    response = client.get(url, format='json')
    data = [ListInventorySerializer(inventory_obj).data]
    assert response.status_code == status.HTTP_200_OK
    assert response.data == data


@pytest.mark.django_db
def test_post_inventory_request(client, inventory_data):
    url = reverse('trade:inventory-list')
    response = client.post(url, CreateInventorySerializer(inventory_data).data, format='json')
    assert response.status_code == status.HTTP_201_CREATED


@pytest.mark.django_db
def test_delete_inventory_request(client, inventory_obj):
    obj_count_after_create = Inventory.objects.count()
    url = reverse('trade:inventory-detail', kwargs={'pk': inventory_obj.pk})
    response = client.delete(url, format='json')
    obj_count_after_delete = Inventory.objects.count()
    assert response.status_code == 204
    assert obj_count_after_create-1 == obj_count_after_delete


@pytest.mark.django_db
def test_put_inventory_request(client, inventory_obj, inventory_data):
    url = reverse('trade:inventory-detail', kwargs={'pk': inventory_obj.pk})
    response = client.put(url, UpdateInventorySerializer(inventory_data).data, format='json')
    assert response.status_code == 200

