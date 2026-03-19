from django.contrib import admin
from .models import TourPackage, TourInclusion, TourExclusion, TourItinerary, AvailableTravelDate

class TourInclusionInline(admin.TabularInline):
    model = TourInclusion
    extra = 1

class TourExclusionInline(admin.TabularInline):
    model = TourExclusion
    extra = 1

class TourItineraryInline(admin.StackedInline):
    model = TourItinerary
    extra = 1

class AvailableTravelDateInline(admin.TabularInline):
    model = AvailableTravelDate
    extra = 1

@admin.register(TourPackage)
class TourPackageAdmin(admin.ModelAdmin):
    list_display = ('title', 'location', 'starting_price', 'rating', 'is_active', 'created_at')
    list_filter = ('is_active', 'location')
    search_fields = ('title', 'location')
    prepopulated_fields = {'slug': ('title',)}
    inlines = [TourInclusionInline, TourExclusionInline, TourItineraryInline, AvailableTravelDateInline]
