from django.contrib import admin
from .models import Todo


class TodoAdmin(admin.ModelAdmin):
    readonly_fields = ('data',)


admin.site.register(Todo, TodoAdmin)
