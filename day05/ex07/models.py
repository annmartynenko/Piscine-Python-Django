from django.db import models

# Create your models here.
class Movies(models.Model):
    episode_nb = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=64, unique=True)
    opening_crawl = models.TextField(blank=True)
    director = models.CharField(max_length=32)
    producer = models.CharField(max_length=128)
    release_date = models.DateField()
    created = models.TimeField(auto_now=True)
    updated = models.TimeField(auto_now_add=True)

    def __str__(self):
        return self.title
