from django.db import models
from django.utils.translation import gettext_lazy as _

from accounts.models import User


class Listing(models.Model):
    creator = models.ForeignKey(
        User, models.CASCADE, related_name="listings"
    )
    price = models.DecimalField(max_digits=1000000, decimal_places=2)
    venue = models.CharField(max_length=256)
    description = models.CharField(max_length=256)

    def __str__(self):
        return f"{self.user}"
