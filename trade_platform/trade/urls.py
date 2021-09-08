from django.contrib import admin
from trade.views import (UserView,
                         ItemView,
                         PriceView,
                         WatchlistView,
                         InventoryView,
                         TradeView,
                         OfferView,
                         )
from rest_framework import routers


app_name = 'trade'

router = routers.SimpleRouter()
router.register('users', UserView)
router.register('items', ItemView)
router.register('prices', PriceView)
router.register('watchlists', WatchlistView)
router.register('inventorys', InventoryView)
router.register('trades', TradeView)
router.register('offers', OfferView)

urlpatterns = router.urls
