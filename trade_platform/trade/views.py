from django.shortcuts import render
from rest_framework.viewsets import GenericViewSet
from trade.serializers import ListUserSerializer, CreateUserSerializer, UpdateUserSerializer, DeleteUserSerializer
from trade.models import User
from rest_framework.mixins import DestroyModelMixin, UpdateModelMixin, ListModelMixin, CreateModelMixin


class UserView(CreateModelMixin, ListModelMixin, UpdateModelMixin, DestroyModelMixin, GenericViewSet):
    queryset = User.objects.all()
    serializer_classes = {
        'list': ListUserSerializer,
        'create': CreateUserSerializer,
        'update': UpdateUserSerializer,
        'delete': DeleteUserSerializer,
    }

    http_method_names = ('get', 'post', 'put', 'delete')

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action)
