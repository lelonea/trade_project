from rest_framework import serializers
from trade.models import User, Item


class CreateUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'password', 'balance')


class ListUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'balance')


class UpdateUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'first_name', 'last_name', 'balance')


class DeleteUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'
