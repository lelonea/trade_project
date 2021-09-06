from django.contrib import admin
from .models import *


admin.site.register(User)
admin.site.register(Inventory)
admin.site.register(WatchList)
admin.site.register(Item)
admin.site.register(Price)
admin.site.register(Offer)
admin.site.register(Trade)
