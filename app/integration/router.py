from rest_framework import routers

from . import api

router = routers.DefaultRouter()
router.register(r'integration', api.IntegrationViewSet)
