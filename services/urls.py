from django.urls import re_path
from rest_framework import routers
from .views import GetAllServiceView,ServiceViewSet_v1, ServiceViewSet
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions


router=routers.DefaultRouter()
router.register(r'v1/service', ServiceViewSet_v1)
router.register(r'v2/service', ServiceViewSet)


schema_view = get_schema_view(
    openapi.Info(
        title="API Pagos de Servicios Streaming",
        default_version="v2",
        description="Servicios",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns=[
    re_path(r'v2/services',GetAllServiceView.as_view()),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

urlpatterns += router.urls