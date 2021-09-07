from rest_framework import serializers
from trade.models import User, Item, Price, WatchList


class CreateUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username',
                  'password',
                  'balance')


class ListUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id',
                  'username',
                  'first_name',
                  'last_name',
                  'balance')


class UpdateUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username',
                  'password',
                  'email',
                  'first_name',
                  'last_name',
                  'balance')


class ItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = Item
        fields = '__all__'


class PriceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Price
        fields = '__all__'


class WatchlistSerializer(serializers.ModelSerializer):

    class Meta:
        model = WatchList
        fields = '__all__'


class UpdateWatchlistSerializer(serializers.ModelSerializer):

    class Meta:
        model = WatchList
        fields = ('item',)
