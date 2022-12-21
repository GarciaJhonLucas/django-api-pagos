from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Services(models.Model):

    class Services(models.TextChoices):
        YOUTUBE = 'YT', _('Youtube')
        SPOTIFY = 'SP', _('Spotify')
        NETFLIX = 'NF', _('Netflix')
        AMAZON = 'AP', _('Amazon Video')
        START = 'ST', _('Start+')
        PARAMOUNT = 'PM', _('Paramount+')

    name = models.CharField(
        max_length=2,
        choices=Services.choices,
        default=Services.NETFLIX,
    )
    
    description = models.CharField(max_length=300)
    logo = models.CharField(max_length=100)

    class Meta:
        ordering = ["-id"]

    def __str__(self) -> str:
        return self.name