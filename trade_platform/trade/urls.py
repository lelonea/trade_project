from django.contrib import admin
from trade.views import UserView, ItemView, PriceView, WatchlistView
from rest_framework import routers


app_name = 'trade'

router = routers.SimpleRouter()
router.register('users', UserView)
router.register('items', ItemView)
router.register('prices', PriceView)
router.register('watchlist', WatchlistView)

urlpatterns = router.urls
