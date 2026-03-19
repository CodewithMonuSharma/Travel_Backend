from django.db import models

class TourPackage(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, max_length=200)
    location = models.CharField(max_length=100)
    rating = models.DecimalField(max_digits=3, decimal_places=1, default=5.0)
    duration = models.CharField(max_length=50, help_text="e.g., '3 Days / 2 Nights'")
    short_description = models.TextField()
    starting_price = models.DecimalField(max_digits=10, decimal_places=2)
    hero_image = models.ImageField(upload_to='tours/', null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class TourInclusion(models.Model):
    tour = models.ForeignKey(TourPackage, related_name='inclusions', on_delete=models.CASCADE)
    text = models.CharField(max_length=200)

    def __str__(self):
        return self.text

class TourExclusion(models.Model):
    tour = models.ForeignKey(TourPackage, related_name='exclusions', on_delete=models.CASCADE)
    text = models.CharField(max_length=200)

    def __str__(self):
        return self.text

class TourItinerary(models.Model):
    tour = models.ForeignKey(TourPackage, related_name='itinerary_days', on_delete=models.CASCADE)
    day_number = models.PositiveIntegerField()
    title = models.CharField(max_length=200)
    description = models.TextField()

    class Meta:
        ordering = ['day_number']
        unique_together = ('tour', 'day_number')

    def __str__(self):
        return f"Day {self.day_number}: {self.title}"

class AvailableTravelDate(models.Model):
    tour = models.ForeignKey(TourPackage, related_name='travel_dates', on_delete=models.CASCADE)
    date = models.DateField()

    class Meta:
        ordering = ['date']
        unique_together = ('tour', 'date')

    def __str__(self):
        return f"{self.tour.title} on {self.date}"
