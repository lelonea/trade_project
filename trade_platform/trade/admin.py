from django.contrib import admin
from trade.models import Inventory, WatchList, Item, Price, Offer, Trade


admin.site.register(Inventory)
admin.site.register(WatchList)
admin.site.register(Item)
admin.site.register(Price)
admin.site.register(Offer)
admin.site.register(Trade)
