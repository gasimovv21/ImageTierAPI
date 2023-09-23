from django.contrib import admin

from .models import UserAccount



@admin.register(UserAccount)
class UserAccountAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'surname',
        'username',
        'tier',
    )
    search_fields = (
        'id',
        'name',
        'surname',
        'username',
        'tier',
    )
    list_filter = (
        'id',
        'name',
        'surname',
        'username',
        'tier',
    )
    empty_value_display = '-empty-'