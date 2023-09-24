from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator
from user_accounts.models import UserAccount

def validate_image_extension(value):
    valid_extensions = ['.jpg', '.jpeg', '.png']
    ext = str(value).lower()
    if not ext.endswith(tuple(valid_extensions)):
        raise ValidationError('Not allowed format of image. Allowed formats: JPG, JPEG, PNG')

class UserImage(models.Model):
    user = models.ForeignKey(
        UserAccount,
        on_delete=models.CASCADE,
        related_name='images'
    )
    image = models.ImageField(upload_to='images/', validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])])
    format = models.CharField(max_length=10, blank=True)
    width = models.PositiveIntegerField(blank=True, null=True)
    height = models.PositiveIntegerField(blank=True, null=True)

    def save(self, *args, **kwargs):
        self.format = self.image.name.split('.')[-1].lower()
        super().save(*args, **kwargs)

    def __str__(self):
        image_name = self.image.name
        return image_name.replace("images/", "")
