from django.contrib import admin
from .models import UserImage

@admin.register(UserImage)
class UserImageAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'image',
        'format',
        'width',
        'height',
    )
    search_fields = (
        'id',
        'image',
        'format',
        'width',
        'height',
    )
    list_filter = (
        'id',
        'image',
        'format',
        'width',
        'height',
    )
    empty_value_display = '-empty-'
