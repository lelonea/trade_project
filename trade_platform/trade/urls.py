from django.contrib import admin
from trade.views import UserView
from rest_framework import routers


app_name = 'trade'

router = routers.SimpleRouter()
router.register('users', UserView)

urlpatterns = router.urls
