from django.db import models
from django.conf import settings

class UserAccount(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    username = models.CharField(
        max_length=50,
        unique=True
        )

    tier = models.CharField(
        max_length=20,
        choices=settings.TIER_CHOICES
    )

    def __str__(self) -> str:
        return f'@{self.username}'
