from django.db import models

class UserAccount(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    username = models.CharField(
        max_length=50,
        unique=True
        )

    TIER_CHOICES = [
        ('Basic', 'Basic'),
        ('Premium', 'Premium'),
        ('Enterprise', 'Enterprise'),
    ]

    tier = models.CharField(
        max_length=20,
        choices=TIER_CHOICES
    )
