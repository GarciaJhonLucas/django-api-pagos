from rest_framework import serializers
from payments.models import Pagos

class PagoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pagos
        fields = '__all__'
        read_only_fields = '__all__',