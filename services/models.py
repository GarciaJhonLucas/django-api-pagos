from django.db import models

# Create your models here.

class Services(models.Model):
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=150)
    logo = models.CharField(max_length=150)
    
    def __str__(self):
        return self.name
    
    class Meta:
        db_table="services"