from django.db import models
from django.utils.translation import gettext_lazy as _
from users.models import User
from services.models import Services

# Create your models here.
class Pagos(models.Model):
    class Servicios(models.TextChoices):
        NETFLIX = 'NF', _('Netflix')
        AMAZON = 'AP', _('Amazon Video')
        START = 'ST', _('Start+')
        PARAMOUNT = 'PM', _('Paramount+')

    servicio = models.CharField(
        max_length=2,
        choices=Servicios.choices,
        default=Servicios.NETFLIX,
    )
    fecha_pago = models.DateField(auto_now_add=True)
    usuario = models.ForeignKey(User, on_delete =models.CASCADE, related_name='users')
    monto = models.FloatField(default=0.0)



class Payment(models.Model):
    payment_date = models.DateField(auto_now_add=True)
    usuario = models.ForeignKey(User, on_delete =models.CASCADE, related_name='users')
    amount = models.FloatField(default=0.0)
    
    def __str__(self) -> str:
        return self.services


class Payment_user(models.Model):
    user_id = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="client")
    service_id = models.ForeignKey(
        Services, on_delete=models.CASCADE, related_name="service")
    amount = models.FloatField(default=0.0)
    paymentDate = models.DateField(auto_now_add=True)
    expirationDate = models.DateField()

    class Meta:
        db_table = "payments"


class Expired_payments(models.Model):
    pay_user_id = models.CharField(max_length=150)
    penalty_fee_amount = models.CharField(max_length=150)