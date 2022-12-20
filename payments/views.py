from django.shortcuts import render

from .models import Services
from rest_framework import viewsets
from rest_framework.views import APIView
from .serializer import ServiceSerializer
from rest_framework.response import Response
from .pagination import StandardResultsSetPagination
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from rest_framework import viewsets, permissions
from .models import Payment
from .serializer import PaymentSerializer
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class ServiceViewSetAdmin(viewsets.ModelViewSet):
    queryset = Services.objects.all()
    serializer_class = ServiceSerializer
    pagination_class = StandardResultsSetPagination
    permission_classes = [IsAdminUser]


class GetAllServiceView(APIView):

    permission_classes = [IsAuthenticated]
    pagination_class = StandardResultsSetPagination

    def get(self, request):
        services = Services.objects.all()
        serializer = ServiceSerializer(services, many=True)
        return Response(serializer.data)


class PaymentsViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    filter_backends = [filters.SearchFilter]
    permission_classes = [IsAuthenticated]
    search_fields = ['user', 'payment_date', 'services']
    throttle_classes = 'payments'