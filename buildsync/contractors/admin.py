from django.contrib import admin
from .models import Contractor

@admin.register(Contractor)
class ContractorAdmin(admin.ModelAdmin):
    list_display = ('name', 'trade', 'company', 'phone_number', 'email')
    search_fields = ('name', 'trade', 'company', 'email')