from rest_framework import serializers
from .models import TourPackage, TourInclusion, TourExclusion, TourItinerary, AvailableTravelDate

class TourInclusionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TourInclusion
        fields = ['id', 'text']

class TourExclusionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TourExclusion
        fields = ['id', 'text']

class TourItinerarySerializer(serializers.ModelSerializer):
    class Meta:
        model = TourItinerary
        fields = ['id', 'day_number', 'title', 'description']

class AvailableTravelDateSerializer(serializers.ModelSerializer):
    class Meta:
        model = AvailableTravelDate
        fields = ['id', 'date']

class TourPackageListSerializer(serializers.ModelSerializer):
    class Meta:
        model = TourPackage
        fields = ['id', 'title', 'slug', 'location', 'rating', 'duration', 'short_description', 'starting_price', 'hero_image']

class TourPackageDetailSerializer(serializers.ModelSerializer):
    inclusions = TourInclusionSerializer(many=True, read_only=True)
    exclusions = TourExclusionSerializer(many=True, read_only=True)
    itinerary_days = TourItinerarySerializer(many=True, read_only=True)
    travel_dates = AvailableTravelDateSerializer(many=True, read_only=True)

    class Meta:
        model = TourPackage
        fields = '__all__'
