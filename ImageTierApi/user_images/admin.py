from django.contrib import admin
from .models import UserImage, ThumbnailImage, ExpireLink

class ExpireLinkInline(admin.TabularInline):
    model = ExpireLink
    extra = 1

class ThumbnailImageInline(admin.TabularInline):
    model = ThumbnailImage
    extra = 1

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
    inlines = [ThumbnailImageInline, ExpireLinkInline]
