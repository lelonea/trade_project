from django.shortcuts import render
from rest_framework.viewsets import GenericViewSet
from trade.serializers import ListUserSerializer, CreateUserSerializer, UpdateUserSerializer, \
    ItemSerializer, PriceSerializer, WatchlistSerializer, UpdateWatchlistSerializer
from trade.models import User, Item, Price, WatchList
from rest_framework import mixins


class UserView(mixins.CreateModelMixin,
               mixins.ListModelMixin,
               mixins.UpdateModelMixin,
               mixins.DestroyModelMixin,
               GenericViewSet):
    queryset = User.objects.all()
    serializer_classes = {
        'list': ListUserSerializer,
        'create': CreateUserSerializer,
        'update': UpdateUserSerializer,
    }

    http_method_names = ('get', 'post', 'put', 'delete')

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action)


class ItemView(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    GenericViewSet,
):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    http_method_names = ('get', 'post', 'put', 'delete')


class PriceView(mixins.CreateModelMixin,
                mixins.ListModelMixin,
                mixins.UpdateModelMixin,
                mixins.DestroyModelMixin,
                GenericViewSet):
    queryset = Price.objects.all()
    serializer_class = PriceSerializer
    http_method_names = ('get', 'post', 'put', 'delete')


class WatchlistView(mixins.CreateModelMixin,
                    mixins.ListModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    GenericViewSet):
    queryset = WatchList.objects.all()
    serializer_classes = {
        'list': WatchlistSerializer,
        'create': WatchlistSerializer,
        'update': UpdateWatchlistSerializer,
    }
    serializer_class_default = WatchlistSerializer
    http_method_names = ('get', 'post', 'put', 'delete')

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action)
