from django.contrib import admin

from .models import Task, Type, Status, TaskType, Project


class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'summary', 'created_at']
    list_filter = ['summary']
    search_fields = ['summary']
    fields = ['summary', 'description', 'status', 'created_at', 'updated_at']
    readonly_fields = ['created_at', 'updated_at']


admin.site.register(Task, TaskAdmin)
admin.site.register(Type)
admin.site.register(Status)
admin.site.register(TaskType)
admin.site.register(Project)
