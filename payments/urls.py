from rest_framework import routers
from .api import PaymentsViewSet

router = routers.DefaultRouter()
router.register('payments', PaymentsViewSet, 'payments')

# Services
urlpatterns = router.urls
