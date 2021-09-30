from django.contrib import admin

from .models import Contact


@admin.register(Contact)
class DefaultAdmin(admin.ModelAdmin):
    pass
# Register your models here.
