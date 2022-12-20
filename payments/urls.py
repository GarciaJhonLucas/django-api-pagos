from rest_framework import routers
from .api import PaymentsViewSet

router = routers.DefaultRouter()

router.register('api/payments', PaymentsViewSet, 'payments')

urlpatterns = router.urls
