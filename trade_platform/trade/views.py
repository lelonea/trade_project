from rest_framework.viewsets import GenericViewSet
from trade.serializers import (
    ListUserSerializer,
    CreateUserSerializer,
    UpdateUserSerializer,
    ListItemSerializer,
    UpdateItemSerializer,
    CreateItemSerializer,
    ListPriceSerializer,
    CreateUpdatePriceSerializer,
    ListWatchlistSerializer,
    CreateWatchlistSerializer,
    UpdateWatchlistSerializer,
    ListInventorySerializer,
    CreateInventorySerializer,
    UpdateInventorySerializer,
    UpdateTradeSerializer,
    ListTradeSerializer,
    CreateTradeSerializer,
    ListOfferSerializer,
    CreateOfferSerializer,
    UpdateOfferSerializer,
)
from trade.models import (
    User,
    Item,
    Price,
    WatchList,
    Inventory,
    Trade,
    Offer,
)
from rest_framework import mixins
from django_filters import rest_framework as filters


class UserView(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    GenericViewSet):
    """
    General User ViewSet description

    list: List id, username, first_name, last_name, balance

    update: Update username, password, email, first_name, last_name, balance

    create: Create record using username, password, balance

    destroy: Delete record by id
    """
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
    """
    General Item ViewSet description

    list: List id, code, name, price, price_currency

    update: Update code, name, price

    create: Create record using code, name, price

    destroy: Delete record by id
    """
    queryset = Item.objects.all()
    serializer_classes = {
        'list': ListItemSerializer,
        'create': CreateItemSerializer,
        'update': UpdateItemSerializer,
    }
    http_method_names = ('get',
                         'post',
                         'put',
                         'patch',
                         'delete',
                         )

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action)


class PriceView(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    GenericViewSet
):
    """
    General Price ViewSet description

    list: List id, item, actual_price, actual_date

    update: Update item, actual_price

    create: Create record using item, actual_price

    destroy: Delete record by id
    """
    queryset = Price.objects.all()
    serializer_classes = {
        'list': ListPriceSerializer,
        'create': CreateUpdatePriceSerializer,
        'update': CreateUpdatePriceSerializer,
    }
    serializer_class_default = ListPriceSerializer
    http_method_names = ('get',
                         'post',
                         'put',
                         'delete',
                         )

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action)


class WatchlistView(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    GenericViewSet
):
    """
    General WatchList ViewSet description

    list: List id, user, item

    update: Update item

    create: Create record using user_id and item_id

    destroy: Delete record by id
    """
    queryset = WatchList.objects.all()
    serializer_classes = {
        'list': ListWatchlistSerializer,
        'create': CreateWatchlistSerializer,
        'update': UpdateWatchlistSerializer,
    }
    serializer_class_default = ListWatchlistSerializer
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


class InventoryView(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    GenericViewSet):
    """
    General Inventory ViewSet description

    list: List id, user, item, quantity

    update: Update quantity

    create: Create record using user, item, quantity

    destroy: Delete record by id
    """
    queryset = Inventory.objects.all()
    serializer_classes = {
        'list': ListInventorySerializer,
        'create': CreateInventorySerializer,
        'update': UpdateInventorySerializer,
    }
    serializer_class_default = ListInventorySerializer
    http_method_names = ('get',
                         'post',
                         'put',
                         'delete',
                         )

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action)

    def get_queryset(self):
        """
        This view should return a list of all the items and quantities
        for the currently authenticated user.
        """
        user = self.request.user
        return Inventory.objects.filter(user=user)


class TradeView(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    GenericViewSet):
    """
    General Trade ViewSet description

    list: List id, item, quantity, unit_price, seller, buyer, description, date_and_time

    update: Update description

    create: Create record using item, quantity, unit_price, seller, buyer, seller_offer, buyer_offer
    """
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


class OfferView(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    GenericViewSet):
    """
    General Offer ViewSet description

    list: List  id, item, order_type, entry_quantity, price, is_active, date_and_time

    update: Update entry_quantity, price, quantity, is_active

    create: Create record using user, item, order_type, entry_quantity, quantity, price

    destroy: Delete record by id
    """
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
