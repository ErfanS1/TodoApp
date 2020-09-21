from django.contrib import admin
from .models import Task
from tinymce.widgets import TinyMCE
from django.db import models

# Register your models here.

class TaskAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Content', {'fields': ['text']}),
        ('Date/Status', {'fields': ['added_time', 'status']})
    ]

    #formfield_overrides = {
    #    models.CharField: {'widget': TinyMCE()},
    #}

admin.site.register(Task, TaskAdmin)