from django.contrib import admin
from .models import Offer

@admin.register(Offer)
class OfferAdmin(admin.ModelAdmin):
    list_display = ('title', 'tag', 'category', 'is_active', 'created_at')
    list_filter = ('is_active', 'category', 'tag')
    search_fields = ('title', 'description')
