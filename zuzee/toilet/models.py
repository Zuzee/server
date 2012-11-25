from django.db import models
from django.contrib.auth.models import User
from toilet.validators import validate_latitude, validate_longitude


class Toilet(models.Model):
    user = models.ForeignKey(User)

    RATING_CHOICES = ((1, 'Unhygenic'),
                      (2, 'Poor'),
                      (3, 'Decent'),
                      (4, 'Good'),
                      (5, 'Excellent'),
                     )
    latitude = models.FloatField(validators=[validate_latitude,])
    longitude = models.FloatField(validators=[validate_longitude,])
    rating = models.PositiveSmallIntegerField(null=True, blank=True,
                                              choices=RATING_CHOICES)
    public = models.NullBooleanField(null=True, blank=True,
                        help_text='Is the toilet on public'
                        ' property? Mark NO if it is on private property'
                        ' such as in a restaurant.')
    for_men = models.NullBooleanField(null=True, blank=True)
    for_women = models.NullBooleanField(null=True, blank=True)
    for_handicapped = models.NullBooleanField(null=True, blank=True,
                        help_text='Are specialized facilities available '
                        'for handicapped people?')
    notes = models.TextField(null=True, blank=True, help_text='Address,'
                             ' condition, timing.')
    created_on = models.DateTimeField(auto_now_add=True)


class SessionToken(models.Model):
    user = models.ForeignKey(User)
    token = models.CharField(max_length=40, unique=True)
    created_on = models.DateTimeField(auto_now_add=True)
