from django.contrib import admin
from .models import Home

# Register your models here.
class AdminHome(admin.ModelAdmin):
    list_display = (
        'title',
        'subtitle',
        'quantity',
    )


admin.site.register(Home, AdminHome)