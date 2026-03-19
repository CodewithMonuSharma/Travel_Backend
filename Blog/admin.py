from django.contrib import admin
from .models import Blog

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'read_time', 'created_at')
    search_fields = ('title',)
