from rest_framework import routers
from .api import *

router = routers.DefaultRouter()

router.register('api/monitoring', ParametersViewSet)

urlpatterns = router.urls