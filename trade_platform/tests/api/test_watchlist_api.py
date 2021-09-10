import pytest
from rest_framework import status
from rest_framework.reverse import reverse
from trade.serializers import ListWatchlistSerializer, CreateWatchlistSerializer, UpdateWatchlistSerializer
from trade.models import WatchList


@pytest.mark.django_db
def test_get_watchlist_list_request(client, watchlist_obj):
    url = reverse('trade:watchlist-list')
    response = client.get(url, format='json')
    data = [ListWatchlistSerializer(watchlist_obj).data]
    assert response.status_code == status.HTTP_200_OK
    assert response.data == data


@pytest.mark.django_db
def test_post_inventory_request(client, watchlist_data):
    url = reverse('trade:watchlist-list')
    response = client.post(url, CreateWatchlistSerializer(watchlist_data).data, format='json')
    assert response.status_code == status.HTTP_201_CREATED


@pytest.mark.django_db
def test_delete_watchlist_request(client, watchlist_obj):
    obj_count_after_create = WatchList.objects.count()
    url = reverse('trade:watchlist-detail', kwargs={'pk': watchlist_obj.pk})
    response = client.delete(url, format='json')
    obj_count_after_delete = WatchList.objects.count()
    assert response.status_code == 204
    assert obj_count_after_create - 1 == obj_count_after_delete


@pytest.mark.django_db
def test_put_watchlist_request(client, watchlist_obj, watchlist_data):
    url = reverse('trade:watchlist-detail', kwargs={'pk': watchlist_obj.pk})
    response = client.put(url, UpdateWatchlistSerializer(watchlist_data).data, format='json')
    assert response.status_code == 200

