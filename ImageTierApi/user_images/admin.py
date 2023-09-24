from django.contrib import admin
from django.utils.html import format_html
from .models import UserImage

@admin.register(UserImage)
class UserImageAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'image',
        'format',
        'width',
        'height',
        'expire_link_status',
    )
    search_fields = (
        'id',
        'user',
        'image',
        'format',
        'width',
        'height',
        'expire_link',
    )
    list_filter = (
        'id',
        'user',
        'image',
        'format',
        'width',
        'height',
        'expire_link',
    )
    empty_value_display = '-empty-'

    def expire_link_status(self, obj):
        if obj.expire_link:
            return format_html('<img src="/static/admin/img/icon-yes.svg" alt="True">')
        else:
            return format_html('<img src="/static/admin/img/icon-no.svg" alt="False">')

    expire_link_status.short_description = 'Expire Link Status'
