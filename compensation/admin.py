from django.contrib import admin

# Register your models here.
from compensation.models import CompensationModel


class CompensationModelAdmin(admin.ModelAdmin):
    list_display = ('cpns_id', 'cpns_title', 'cpns_category', 'activated', 'create_at', 'update_at')
    search_fields = ['cpns_category', ]
    fields = ('cpns_title', 'cpns_category', 'cpns_content', 'activated')
    date_hierarchy = 'update_at'


admin.site.register(CompensationModel, CompensationModelAdmin)
