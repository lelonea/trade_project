from django.shortcuts import render
from rest_framework.viewsets import GenericViewSet
from trade.serializers import ListUserSerializer, CreateUserSerializer, UpdateUserSerializer, ItemSerializer
from trade.models import User, Item
from rest_framework import mixins


class UserView(mixins.CreateModelMixin, mixins.ListModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, GenericViewSet):
    queryset = User.objects.all()
    serializer_classes = {
        'list': ListUserSerializer,
        'create': CreateUserSerializer,
        'update': UpdateUserSerializer,
    }

    http_method_names = ('get', 'post', 'put', 'delete')

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action)


class ItemView(mixins.CreateModelMixin, mixins.ListModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, GenericViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    http_method_names = ('get', 'post', 'put', 'delete')
