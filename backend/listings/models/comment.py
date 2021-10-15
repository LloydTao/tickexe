from django.db import models
from django.utils.translation import gettext_lazy as _

from accounts.models.user import User
from .listing import Listing


class Comment(models.Model):
    author = models.ForeignKey(User, models.CASCADE, related_name="comments")
    listing = models.ForeignKey(Listing, models.CASCADE, related_name="comments")
    message = models.CharField(max_length=256)

    def __str__(self):
        return f"{self.user}"
