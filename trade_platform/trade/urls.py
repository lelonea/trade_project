from django.contrib import admin
from django.urls import path, include
from trade.views import ItemListView, ItemView


app_name = 'trade'

urlpatterns = [

    path('item/', include([
            path('all/', ItemListView.as_view(), name='Item_list'),
            path('detail/<int:pk>', ItemView.as_view(), name='Item_detail'),
    ])),
]
