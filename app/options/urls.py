from rest_framework import routers

from app.options.views import *

router = routers.SimpleRouter()
router.register('configuraciones', ConfiguracionTiradaView)
router.register('paquetes', PaqueteCartaView)

urlpatterns = []
urlpatterns += router.urls
