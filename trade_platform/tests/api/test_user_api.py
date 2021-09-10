import pytest
from rest_framework import status
from rest_framework.reverse import reverse
from trade.serializers import ListUserSerializer, UpdateUserSerializer
from trade.models import User


@pytest.mark.django_db
def test_get_user_list_request(client, user_obj):
    url = reverse('trade:user-list')
    response = client.get(url, format='json')
    data = [ListUserSerializer(user_obj).data]
    assert response.status_code == status.HTTP_200_OK
    assert response.data == data


@pytest.mark.django_db
def test_post_user_request(client, fake_user_data):
    url = reverse('trade:user-list')
    response = client.post(url, fake_user_data, format='json')
    assert response.status_code == status.HTTP_201_CREATED


@pytest.mark.django_db
def test_delete_user_request(client, user_obj):
    obj_count_after_create = User.objects.count()
    url = reverse('trade:user-detail', kwargs={'pk': user_obj.pk})
    response = client.delete(url, format='json')
    obj_count_after_delete = User.objects.count()
    assert response.status_code == 204
    assert obj_count_after_create - 1 == obj_count_after_delete


@pytest.mark.django_db
def test_put_user_request(client, user_obj, user_data):
    url = reverse('trade:user-detail', kwargs={'pk': user_obj.pk})
    response = client.put(url, UpdateUserSerializer(user_data).data, format='json')
    assert response.status_code == 200
