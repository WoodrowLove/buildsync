from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'project', 'status', 'assigned_to', 'due_date')
    list_filter = ('status', 'project')
    search_fields = ('title', 'project__name', 'assigned_to__username')

