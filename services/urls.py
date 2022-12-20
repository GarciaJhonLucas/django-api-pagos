from rest_framework import routers
from .views import GetAllServiceView,ServiceViewSetAdmin
from django.urls import path

router_service=routers.DefaultRouter()
router_service.register(r'api/v2/services/admin',ServiceViewSetAdmin,'services-admin')

urlpatterns=[
    path(r'api/v2/services',GetAllServiceView.as_view(),name="services")
]

urlpatterns += router_service.urls