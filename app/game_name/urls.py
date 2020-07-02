from rest_framework import routers

from app.game_name.views import *

router = routers.SimpleRouter()
router.register('juegonombre', NombreDescripcionView)
router.register('descripciones', DescripcionNombreView)

urlpatterns = []
urlpatterns += router.urls
