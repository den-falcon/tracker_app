from django.contrib import admin

from .models import Task, Type, Status, TaskType


class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'summary', 'created_at']
    list_filter = ['summary']
    search_fields = ['summary']
    fields = ['summary', 'description', 'status', 'created_at', 'updated_at']
    readonly_fields = ['created_at', 'updated_at']


class TypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_filter = ['name']
    search_fields = ['name']
    fields = ['name']


class StatusAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_filter = ['name']
    search_fields = ['name']
    fields = ['name']


class TaskTypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'task', 'type']
    list_filter = ['task', 'type']
    search_fields = ['task', 'type']
    fields = ['task', 'type']


admin.site.register(Task, TaskAdmin)
admin.site.register(Type, TypeAdmin)
admin.site.register(Status, StatusAdmin)
admin.site.register(TaskType, TaskTypeAdmin)
