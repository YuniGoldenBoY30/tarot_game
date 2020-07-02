from rest_framework import routers

from app.game_tarot.views import *

router = routers.SimpleRouter()
router.register('carta', CartaView)
router.register('categoriabasica', CategoriaBasicaView)
router.register('color', ColorView)
router.register('numero', NumeroView)
router.register('descripciones', DescripcionView)
router.register('tipoarcano', TipoArcanoView)

urlpatterns = []
urlpatterns += router.urls
