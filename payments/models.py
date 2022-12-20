from django.db import models

# Create your models here.
class Payment(models.Model):
    services = models.CharField(max_length=20)
    amount = models.FloatField()
    payment_date = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return self.services
    

class Services(models.Model):
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=150)
    logo = models.CharField(max_length=150)


class Payment_user(models.Model):
    user_id = models.CharField(max_length=150)
    service_id = models.CharField(max_length=150)
    amount = models.CharField(max_length=150)
    paymentDate = models.CharField(max_length=150)
    expirationDate = models.CharField(max_length=150)


class Expired_payments(models.Model):
    pay_user_id = models.CharField(max_length=150)
    penalty_fee_amount = models.CharField(max_length=150)