import pytest
from rest_framework import status
from rest_framework.reverse import reverse
from trade.serializers import ListPriceSerializer, CreateUpdatePriceSerializer
from trade.models import Price


@pytest.mark.django_db
def test_get_price_list_request(client, price_obj):
    url = reverse('trade:price-list')
    response = client.get(url, format='json')
    data = [ListPriceSerializer(price_obj).data]
    assert response.status_code == status.HTTP_200_OK
    assert response.data == data


@pytest.mark.django_db
def test_post_inventory_request(client, price_data):
    url = reverse('trade:price-list')
    response = client.post(url, CreateUpdatePriceSerializer(price_data).data, format='json')
    assert response.status_code == status.HTTP_201_CREATED


@pytest.mark.django_db
def test_delete_price_request(client, price_obj):
    obj_count_after_create = Price.objects.count()
    url = reverse('trade:price-detail', kwargs={'pk': price_obj.pk})
    response = client.delete(url, format='json')
    obj_count_after_delete = Price.objects.count()
    assert response.status_code == 204
    assert obj_count_after_create - 1 == obj_count_after_delete


@pytest.mark.django_db
def test_put_price_request(client, price_obj, price_data):
    url = reverse('trade:price-detail', kwargs={'pk': price_obj.pk})
    response = client.put(url, CreateUpdatePriceSerializer(price_data).data, format='json')
    assert response.status_code == 200

