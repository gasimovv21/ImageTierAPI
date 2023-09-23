from django.db import models
from PIL import Image as PILImage


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

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        image = PILImage.open(self.image.path)
        self.format = image.format.lower() if image.format else ''
        self.width, self.height = image.size
        super().save(*args, **kwargs)

    def __str__(self):
        image_name = self.image.name
        return image_name.replace("images/", "")
