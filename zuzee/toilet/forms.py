from django import forms
from toilet.models import Toilet

class ToiletForm(forms.ModelForm):
    class Meta:
        model = Toilet
