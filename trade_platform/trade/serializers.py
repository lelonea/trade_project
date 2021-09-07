from rest_framework import serializers
from trade.models import User, Item, WatchList, Offer, Trade, Inventory, Price


class UserSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = User
        fields = '__all__'


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = "__all__"
        read_only_fields = ('id', )


class WatchListSerializer(serializers.ModelSerializer):
    class Meta:
        model = WatchList
        fields = "__all__"
        read_only_fields = ('id', )


class OfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offer
        fields = "__all__"
        read_only_fields = ('id', )


class TradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trade
        fields = "__all__"
        read_only_fields = ('id',)


class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = "__all__"
        read_only_fields = ('id', )


class PriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Price
        fields = "__all__"
        read_only_fields = ('id', )
