from .models import Users
from rest_framework import viewsets, permissions


# Creacion de la viewset API
class UserViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    permission_classes = [permissions.AllowAny]