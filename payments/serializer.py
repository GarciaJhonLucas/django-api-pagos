from rest_framework import serializers
from .models import Payment
from users.models import Users

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'
        read_only_fields = 'payment_date'