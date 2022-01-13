from django.contrib import admin

from .models import Task, Type, Status


class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'summary', 'created_at']
    list_filter = ['summary']
    search_fields = ['summary']
    fields = ['summary', 'description', 'type', 'status', 'created_at', 'updated_at']
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


admin.site.register(Task, TaskAdmin)
admin.site.register(Type, TypeAdmin)
admin.site.register(Status, StatusAdmin)
