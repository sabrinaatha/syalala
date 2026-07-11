from django.contrib import admin
from .models import GetInTouch


@admin.register(GetInTouch)
class GetInTouchAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email_address', 'subject', 'created_at')
    readonly_fields = ('created_at',)