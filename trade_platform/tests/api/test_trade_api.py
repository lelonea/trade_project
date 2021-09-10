import pytest
from rest_framework import status
from rest_framework.reverse import reverse
from trade.serializers import ListTradeSerializer, CreateTradeSerializer, UpdateTradeSerializer
from trade.models import Trade


@pytest.mark.django_db
def test_get_trade_list_request(client, trade_obj):
    url = reverse('trade:trade-list')
    response = client.get(url, format='json')
    data = [ListTradeSerializer(trade_obj).data]
    assert response.status_code == status.HTTP_200_OK
    assert response.data == data


@pytest.mark.django_db
def test_post_inventory_request(client, trade_data):
    url = reverse('trade:trade-list')
    response = client.post(url, CreateTradeSerializer(trade_data).data, format='json')
    assert response.status_code == status.HTTP_201_CREATED


@pytest.mark.django_db
def test_delete_trade_request_not_allowed(client, trade_obj):
    obj_count_after_create = Trade.objects.count()
    url = reverse('trade:trade-detail', kwargs={'pk': trade_obj.pk})
    response = client.delete(url, format='json')
    obj_count_after_failed_delete = Trade.objects.count()
    assert response.status_code == 405
    assert obj_count_after_create == obj_count_after_failed_delete


@pytest.mark.django_db
def test_put_trade_request(client, trade_obj, trade_data):
    url = reverse('trade:trade-detail', kwargs={'pk': trade_obj.pk})
    response = client.put(url, UpdateTradeSerializer(trade_data).data, format='json')
    assert response.status_code == 200

