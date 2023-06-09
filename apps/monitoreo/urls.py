from rest_framework import routers
from .api import ParametrosViewSet

router = routers.DefaultRouter()

router.register('parametros', ParametrosViewSet, 'parametros')

urlpatterns = router.urls