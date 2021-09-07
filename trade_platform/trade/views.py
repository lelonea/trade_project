from django.shortcuts import render
from rest_framework.generics import GenericAPIView, ListAPIView
from trade.serializers import ItemSerializer
from trade.models import Item
from rest_framework import mixins


class ItemListView(ListAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    fields = ('id',)


class ItemView(mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, GenericAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
