from django.urls import re_path
from rest_framework import routers
from .views import GetAllServiceView,ServiceViewSetAdmin

router=routers.DefaultRouter()
router.register(r'api/v2/services',ServiceViewSetAdmin,'services-admin')

urlpatterns=[
    re_path(r'^api/v2/services',GetAllServiceView.as_view())
]

urlpatterns += router.urls