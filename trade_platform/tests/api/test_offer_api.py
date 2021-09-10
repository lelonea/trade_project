import pytest
from rest_framework import status
from rest_framework.reverse import reverse
from trade.serializers import ListOfferSerializer, UpdateOfferSerializer, CreateOfferSerializer
from trade.models import Offer


@pytest.mark.django_db
def test_get_offer_list_request(client, offer_obj):
    url = reverse('trade:offer-list')
    response = client.get(url, format='json')
    data = [ListOfferSerializer(offer_obj).data]
    assert response.status_code == status.HTTP_200_OK
    assert response.data == data


@pytest.mark.django_db
def test_post_inventory_request(client, offer_data):
    url = reverse('trade:offer-list')
    response = client.post(url, CreateOfferSerializer(offer_data).data, format='json')
    assert response.status_code == status.HTTP_201_CREATED


@pytest.mark.django_db
def test_delete_offer_request(client, offer_obj):
    obj_count_after_create = Offer.objects.count()
    url = reverse('trade:offer-detail', kwargs={'pk': offer_obj.pk})
    response = client.delete(url, format='json')
    obj_count_after_delete = Offer.objects.count()
    assert response.status_code == 204
    assert obj_count_after_create - 1 == obj_count_after_delete


@pytest.mark.django_db
def test_put_offer_request(client, offer_obj, offer_data):
    url = reverse('trade:offer-detail', kwargs={'pk': offer_obj.pk})
    response = client.put(url, UpdateOfferSerializer(offer_data).data, format='json')
    assert response.status_code == 200

