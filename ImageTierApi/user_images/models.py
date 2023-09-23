from django.db import models
from user_accounts.models import UserAccount

class UserImage(models.Model):
    user = models.ForeignKey(
        UserAccount,
        on_delete=models.CASCADE,
        related_name='images'
    )
    image = models.ImageField(upload_to='images/')
    format = models.CharField(max_length=10, blank=True)
    width = models.PositiveIntegerField(blank=True, null=True)
    height = models.PositiveIntegerField(blank=True, null=True)

    def __str__(self):
        image_name = self.image.name
        return image_name.replace("images/", "")

