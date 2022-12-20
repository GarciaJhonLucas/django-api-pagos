from django.contrib import admin
from .models import Payment, Services, Payment_user


# Register your models here.
admin.site.register(Payment)
admin.site.register(Payment_user)
