from django.core.exceptions import ValidationError

def validate_latitude(value): 
    if not -90 < value < 90:
        raise ValidationError("This is not a valid latitude")

def validate_longitude(value):
    if not -180 < value < 180: 
        raise ValidationError("This is not a valid longitude")

