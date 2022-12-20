from django.shortcuts import render

from rest_framework.views import APIView
from .pagination import StandardResultsSetPagination
from rest_framework.permissions import IsAuthenticated

from rest_framework import viewsets
from .models import Payment
from .serializer import PaymentSerializer
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated


# Create your views here.
class PaymentsViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = [filters.SearchFilter]
    permission_classes = [IsAuthenticated]
    search_fields = ['user', 'payment_date', 'services']
    throttle_classes = 'payments'


class PagoViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.get_queryset().order_by('id')
    serializer_class = PaymentSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = [filters.SearchFilter]
    permission_classes = [IsAuthenticated]
    search_fields = ['user', 'payment_date', 'services']
    throttle_classes = 'payments'
    
    
class ExpiredPaymentsViewSet(APIView):
    queryset = Payment.objects.get_queryset().order_by('id')
    serializer_class = PaymentSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = [filters.SearchFilter]
    permission_classes = [IsAuthenticated]
    
    search_fields = ['pay_user_id']
    throttle_classes = 'Expired_payments'