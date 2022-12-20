from django.urls import re_path
from rest_framework import routers
from .views import PagoViewSet,PaymentsViewSet, ExpiredPaymentsViewSet

router=routers.DefaultRouter()
router.register(r'v1/payments',PagoViewSet)
router.register(r'v2/payments',PaymentsViewSet)

urlpatterns=[
    re_path(r'v2/expired-payments',ExpiredPaymentsViewSet.as_view())
]

urlpatterns += router.urls