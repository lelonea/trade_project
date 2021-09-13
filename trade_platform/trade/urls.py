from django.contrib import admin
from trade.views import (
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
router.register('items', ItemView)
router.register('prices', PriceView)
router.register('watchlists', WatchlistView)
router.register('inventories', InventoryView)
router.register('trades', TradeView)
router.register('offers', OfferView)

urlpatterns = router.urls
