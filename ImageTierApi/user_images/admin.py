from django.contrib import admin
from .models import UserImage, ThumbnailImage, ExpireLink
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.contrib.admin.widgets import AdminTextInputWidget
from django.utils.html import format_html

@admin.register(UserImage)
class UserImageAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'image',
        'format',
        'width',
        'height',
    )
    search_fields = (
        'id',
        'user__username',
        'image',
        'format',
        'width',
        'height',
    )
    list_filter = (
        'id',
        'user',
        'image',
        'format',
        'width',
        'height',
    )
    empty_value_display = '-empty-'


@admin.register(ThumbnailImage)
class ThumbnailImageAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user_image',
        'thumbnail',
        'width',
        'height',
    )

    search_fields = (
        'id',
        'user_image',
        'thumbnail',
        'width',
        'height',
    )
    list_filter = (
        'id',
        'user_image',
        'thumbnail',
        'width',
        'height',
    )
    empty_value_display = '-empty-'

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        if obj.user_image and obj.width and obj.height:
            original_image = Image.open(obj.user_image.image)
            thumbnail = original_image.resize((obj.width, obj.height))
            thumbnail_io = BytesIO()
            thumbnail.save(thumbnail_io, format=original_image.format)
            thumbnail_file = InMemoryUploadedFile(
                thumbnail_io,
                None,
                f"{obj.user_image}_thumbnail.{original_image.format.lower()}",
                f"image/{original_image.format.lower()}",
                thumbnail_io.tell,
                None
            )
            obj.thumbnail.save(thumbnail_file.name, thumbnail_file, save=True)


@admin.register(ExpireLink)
class ExpireLinkAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user_image',
        'expire_link_duration',
        'expire_link_token',
        'created_at',
        'updated_at',
    )
    search_fields = (
        'id',
        'user_image__image',
        'expire_link_duration',
        'expire_link_token',
        'created_at',
        'updated_at',
    )
    list_filter = (
        'id',
        'user_image__image',
        'expire_link_duration',
        'expire_link_token',
        'created_at',
        'updated_at',
    )
    empty_value_display = '-empty-'