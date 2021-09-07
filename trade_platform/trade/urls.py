from django.contrib import admin
from trade.views import UserView, ItemView
from rest_framework import routers


app_name = 'trade'

router = routers.SimpleRouter()
router.register('users', UserView)
router.register('items', ItemView)

urlpatterns = router.urls
