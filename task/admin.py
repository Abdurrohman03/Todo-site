from django.contrib import admin
from .models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'title', 'status', 'priority', 'created_date']
    search_fields = ['title']
    list_filter = ['status', 'priority']
    date_hierarchy = 'created_date'
