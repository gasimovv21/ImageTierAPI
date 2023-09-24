from django.db import models
from django.conf import settings

class UserAccount(models.Model):
    name = models.CharField(max_length=settings.USER_ACCOUNT_NAME_MAX_LENGTH)
    surname = models.CharField(max_length=settings.USER_ACCOUNT_SURNAME_MAX_LENGTH)
    username = models.CharField(
        max_length=settings.USER_ACCOUNT_USERNAME_MAX_LENGTH,
        unique=settings.USER_ACCOUNT_USERNAME_UNIQUE
        )

    tier = models.CharField(
        max_length=settings.USER_ACCOUNT_TIER_MAX_LENGTH,
        choices=settings.TIER_CHOICES
    )

    def __str__(self) -> str:
        return f'@{self.username}'
