from django.db import models
from django.conf import settings
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
        related_name=settings.USER_IMAGE_USER_RELATED_NAME
    )
    image = models.ImageField(
        upload_to=settings.USER_IMAGE_IMAGE_UPLOAD_TO,
        validators=[
            FileExtensionValidator(
                allowed_extensions=[
                    'jpg',
                    'jpeg',
                    'png'
                ]
            )
        ]
    )
    format = models.CharField(
        max_length=settings.USER_IMAGE_FORMAT_MAX_LENGTH,
        blank=settings.USER_IMAGE_FORMAT_BLANK
    )
    width = models.PositiveIntegerField(
        blank=settings.USER_IMAGE_WIDTH_BLANK,
        null=settings.USER_IMAGE_WIDTH_NULL
    )
    height = models.PositiveIntegerField(
        blank=settings.USER_IMAGE_HEIGHT_BLANK,
        null=settings.USER_IMAGE_HEIGHT_NULL
    )
    expire_link = models.CharField(
        max_length=settings.USER_IMAGE_EXPIRE_LINK_MAX_LENGTH,
        blank=settings.USER_IMAGE_EXPIRE_LINK_BLANK,
    )

    def save(self, *args, **kwargs):
        self.format = self.image.name.split('.')[-1].lower()
        super().save(*args, **kwargs)

    def __str__(self):
        image_name = self.image.name
        return image_name.replace("images/", "")
