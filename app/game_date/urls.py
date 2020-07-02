from rest_framework import routers

from app.game_date.views import *

router = routers.SimpleRouter()
router.register('signozodiacal', SignoZodiacoView)
router.register('juegofecha', SignoCombNumView)

urlpatterns = []
urlpatterns += router.urls
