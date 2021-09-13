from rest_framework import serializers
from trade.models import (
    # User,
    Item,
    Price,
    WatchList,
    Inventory,
    Offer,
    Trade,
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


class ListPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Price
        fields = ('id',
                  'item',
                  'actual_price',
                  'actual_date',
                  )


class CreateUpdatePriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Price
        fields = ('item',
                  'actual_price',
                  )


class ListWatchlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = WatchList
        fields = ('id',
                  'user',
                  'item',
                  )


class CreateWatchlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = WatchList
        fields = ('user',
                  'item',
                  )


class UpdateWatchlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = WatchList
        fields = ('item',
                  )


class ListInventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = ('id',
                  'user',
                  'item',
                  'quantity',
                  )


class CreateInventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = ('user',
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
