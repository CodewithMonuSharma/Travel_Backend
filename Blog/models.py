from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=200)
    date = models.CharField(max_length=50) # e.g. "March 10, 2026"
    read_time = models.CharField(max_length=50) # e.g. "5 min read"
    link = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
