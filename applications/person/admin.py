from django.contrib import admin
from .models import Ability, Employee

# Register your models here.

class AdminAbility(admin.ModelAdmin):
    search_fields = ('Abilities',)
    list_display = (
        'id',
        'ability',
    )

admin.site.register(Ability, AdminAbility)


class AdminEmployee(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'last_name',
        'department',
        'position',
        'full_name'
    )
    # def full_name(self, obj):
    #     return obj.name + ' ' +obj.last_name

    search_fields = ('name',)
    list_filter = ('position', 'ability')
    filter_horizontal = ('ability',)

admin.site.register(Employee, AdminEmployee)

