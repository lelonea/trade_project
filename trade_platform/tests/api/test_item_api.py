import pytest
from rest_framework import status
from rest_framework.reverse import reverse
from trade.serializers import ListItemSerializer, UpdateItemSerializer
from trade.models import Item


@pytest.mark.django_db
def test_get_item_list_request(client, item_obj):
    url = reverse('trade:item-list')
    response = client.get(url, format='json')
    data = [ListItemSerializer(item_obj).data]
    assert response.status_code == status.HTTP_200_OK
    assert response.data == data


@pytest.mark.django_db
def test_post_item_request(client, item_data):
    url = reverse('trade:item-list')
    response = client.post(url, data=item_data, format='json')
    assert response.status_code == status.HTTP_201_CREATED


@pytest.mark.django_db
def test_delete_item_request(client, item_obj):
    obj_count_after_create = Item.objects.count()
    url = reverse('trade:item-detail', kwargs={'pk': item_obj.pk})
    response = client.delete(url, format='json')
    obj_count_after_delete = Item.objects.count()
    assert response.status_code == 204
    assert obj_count_after_create-1 == obj_count_after_delete


@pytest.mark.django_db
def test_put_item_request(client, item_obj, item_data):
    url = reverse('trade:item-detail', kwargs={'pk': item_obj.pk})
    response = client.put(url, UpdateItemSerializer(item_data).data, format='json')
    assert response.status_code == 200

