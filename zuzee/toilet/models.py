from django.db import models
from toilet.validators import validate_latitude, validate_longitude

class Toilet(models.Model):
    latitude = models.FloatField(validators=[validate_latitude,])
    longitude = models.FloatField(validators=[validate_longitude,])
    rating = models.PositiveSmallIntegerField(null=True, blank=True)
    public = models.NullBooleanField(null=True, blank=True)
    for_men = models.NullBooleanField(null=True, blank=True)
    for_women = models.NullBooleanField(null=True, blank=True)
    for_handicapped = models.NullBooleanField(null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
    created_by = models.CharField(max_length=128, null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
