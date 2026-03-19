from django.db import models

class Offer(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    tag = models.CharField(max_length=50) # e.g. "SUMMER SPECIAL"
    category = models.CharField(max_length=100) # e.g. "Bank Promos"
    image = models.ImageField(upload_to='offers/')
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
