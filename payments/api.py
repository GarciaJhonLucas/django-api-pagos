from rest_framework import viewsets, permissions
from .models import Payment
from .serializer import PaymentSerializer
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated

class PaymentsViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    filter_backends = [filters.SearchFilter]
    permission_classes = [IsAuthenticated]
    search_fields = ['user', 'payment_date', 'services']
    throttle_classes = 'payments'