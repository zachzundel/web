from rest_framework import routers

from . import api

router = routers.DefaultRouter()
router.register(r'organization', api.OrganizationViewSet)
