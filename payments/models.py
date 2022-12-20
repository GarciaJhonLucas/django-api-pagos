from django.db import models
from django.utils.translation import gettext_lazy as _
from users.models import User
from services.models import Services

# Create your models here.
class Payment(models.Model):
    payment_date = models.DateField(auto_now_add=True)
    users = models.ForeignKey(User, on_delete =models.CASCADE, related_name='users')
    amount = models.FloatField(default=0.0)
    

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