from django.contrib import admin

from .models import Task, Type, Status, Project


class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'created_at']
    list_filter = ['name']
    search_fields = ['name']
    fields = ['name', 'description', 'status', 'created_at', 'updated_at']
    readonly_fields = ['created_at', 'updated_at']


admin.site.register(Task, TaskAdmin)
admin.site.register(Type)
admin.site.register(Status)
admin.site.register(Project)
