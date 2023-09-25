from django.db import models
from django.conf import settings
from django.core.validators import FileExtensionValidator, MaxValueValidator, MinValueValidator
from user_accounts.models import UserAccount


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
        ],
    )
    format = models.CharField(
        max_length=settings.USER_IMAGE_FORMAT_MAX_LENGTH,
        blank=settings.USER_IMAGE_FORMAT_BLANK,
        editable=False
    )
    width = models.PositiveIntegerField(
        blank=settings.USER_IMAGE_WIDTH_BLANK,
        null=settings.USER_IMAGE_WIDTH_NULL,
        editable=False
    )
    height = models.PositiveIntegerField(
        blank=settings.USER_IMAGE_HEIGHT_BLANK,
        null=settings.USER_IMAGE_HEIGHT_NULL,
        editable=False
    )

    def save(self, *args, **kwargs):
        self.format = self.image.name.split('.')[-1].lower()
        super().save(*args, **kwargs)

    def __str__(self):
        image_name = self.image.name
        return image_name.replace("images/", "")



class ThumbnailImage(models.Model):
    user_image = models.ForeignKey(
        UserImage,
        on_delete=models.CASCADE,
        related_name='thumbnails'
    )
    thumbnail = models.ImageField(
        upload_to=settings.USER_IMAGE_IMAGE_THUMBNAIL_UPLOAD_TO,
        blank=True,
        null=True,
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
    width = models.PositiveIntegerField(blank=True, null=True)
    height = models.PositiveIntegerField(blank=True, null=True)


    def __str__(self):
        return f"{self.user_image}"


class ExpireLink(models.Model):
    user_image = models.ForeignKey(
        UserImage,
        on_delete=models.CASCADE,
        related_name='expire_links'
    )
    expire_link_duration = models.PositiveIntegerField(
        validators=[
            MinValueValidator(300),
            MaxValueValidator(30000),
        ]
    )
    expire_link = models.CharField(
        max_length=settings.USER_IMAGE_EXPIRE_LINK_MAX_LENGTH,
        blank=True,
        )