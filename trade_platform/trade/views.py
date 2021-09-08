from django.shortcuts import render
from rest_framework.viewsets import GenericViewSet
from trade.serializers import (ListUserSerializer,
                               CreateUserSerializer,
                               UpdateUserSerializer,
                               ItemSerializer,
                               PriceSerializer,
                               WatchlistSerializer,
                               UpdateWatchlistSerializer,
                               InventorySerializer,
                               UpdateInventorySerializer,
                               UpdateTradeSerializer,
                               ListTradeSerializer,
                               CreateTradeSerializer,
                               ListOfferSerializer,
                               CreateOfferSerializer,
                               UpdateOfferSerializer,
                               )
from trade.models import (User,
                          Item,
                          Price,
                          WatchList,
                          Inventory,
                          Trade,
                          Offer,
                          )
from rest_framework import mixins
from django_filters import rest_framework as filters


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

    http_method_names = ('get',
                         'post',
                         'put',
                         'delete',
                         )

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
    http_method_names = ('get',
                         'post',
                         'put',
                         'delete',
                         )


class PriceView(mixins.CreateModelMixin,
                mixins.ListModelMixin,
                mixins.UpdateModelMixin,
                mixins.DestroyModelMixin,
                GenericViewSet):
    queryset = Price.objects.all()
    serializer_class = PriceSerializer
    http_method_names = ('get',
                         'post',
                         'put',
                         'delete',
                         )


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
    http_method_names = ('get',
                         'post',
                         'put',
                         'delete',
                         )
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('user',
                     )

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action)


class InventoryView(mixins.CreateModelMixin,
                    mixins.ListModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    GenericViewSet):
    queryset = Inventory.objects.all()
    serializer_classes = {
        'list': InventorySerializer,
        'create': InventorySerializer,
        'update': UpdateInventorySerializer,
    }
    serializer_class_default = InventorySerializer
    http_method_names = ('get',
                         'post',
                         'put',
                         'delete',
                         )
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('user',
                     )

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action)

    def get_queryset(self):
        """
        This view should return a list of all the purchases
        for the currently authenticated user.
        """
        user = self.request.user
        return Inventory.objects.filter(user=user)


class TradeView(mixins.CreateModelMixin,
                mixins.ListModelMixin,
                mixins.UpdateModelMixin,
                mixins.DestroyModelMixin,
                GenericViewSet):
    queryset = Trade.objects.all()
    serializer_classes = {
        'list': ListTradeSerializer,
        'create': CreateTradeSerializer,
        'update': UpdateTradeSerializer,
    }

    http_method_names = ('get',
                         'post',
                         'put',
                         )
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('item',
                     'seller',
                     'buyer',
                     'seller_offer',
                     'buyer_offer',
                     )

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action)


class OfferView(mixins.CreateModelMixin,
                mixins.ListModelMixin,
                mixins.UpdateModelMixin,
                mixins.DestroyModelMixin,
                GenericViewSet):
    queryset = Offer.objects.all()
    serializer_classes = {
        'list': ListOfferSerializer,
        'create': CreateOfferSerializer,
        'update': UpdateOfferSerializer,
    }

    http_method_names = ('get',
                         'post',
                         'put',
                         'delete'
                         )
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('item',
                     'order_type',
                     'is_active',
                     )

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action)
