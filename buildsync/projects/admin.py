from django.contrib import admin
from .models import Project

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'status', 'budget', 'manager', 'start_date', 'end_date')
    list_filter = ('status', 'manager')
    search_fields = ('name', 'location')
