from django.db import models

class Toilet(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    rating = models.PositiveSmallIntegerField()
    public = models.BooleanField()
    for_men = models.BooleanField()
    for_women = models.BooleanField()
    for_handicapped = models.BooleanField()
    notes = models.TextField()
    created_by = models.CharField(max_length=128)
    created_on = models.DateTimeField(auto_now_add=True)
