from rest_framework import serializers
from trade.models import (
    User,
    Item,
    Price,
    WatchList,
    Inventory,
    Offer,
    Trade,
)


class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username',
                  'password',
                  'balance',
                  )


class ListUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id',
                  'username',
                  'first_name',
                  'last_name',
                  'balance',
                  )


class UpdateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username',
                  'password',
                  'email',
                  'first_name',
                  'last_name',
                  'balance',
                  )


class ListItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('id',
                  'code',
                  'name',
                  'price',
                  'price_currency',
                  )


class UpdateItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('code',
                  'name',
                  'price',
                  )


class CreateItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('code',
                  'name',
                  'price',
                  'price_currency',
                  )


class PriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Price
        fields = ('id',
                  'item',
                  'actual_price',
                  'actual_date',
                  )


class WatchlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = WatchList
        fields = ('id',
                  'user',
                  'item',
                  )


class UpdateWatchlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = WatchList
        fields = ('item',
                  )


class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = ('id',
                  'user',
                  'item',
                  'quantity',
                  )


class UpdateInventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = ('quantity',
                  )


class CreateTradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trade
        fields = ('item',
                  'quantity',
                  'unit_price',
                  'seller',
                  'buyer',
                  'seller_offer',
                  'buyer_offer',
                  )


class ListTradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trade
        fields = ('id',
                  'item',
                  'quantity',
                  'unit_price',
                  'seller',
                  'buyer',
                  'description',
                  'date_and_time',
                  )


class UpdateTradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trade
        fields = ('description',
                  )


class CreateOfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offer
        fields = ('user',
                  'item',
                  'order_type',
                  'entry_quantity',
                  'quantity',
                  'price',
                  )


class ListOfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offer
        fields = ('id',
                  'item',
                  'order_type',
                  'entry_quantity',
                  'price',
                  'is_active',
                  'date_and_time',
                  )


class UpdateOfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offer
        fields = ('entry_quantity',
                  'quantity',
                  'price',
                  'is_active',
                  )
