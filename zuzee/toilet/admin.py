from django.contrib import admin
from toilet.models import Toilet

class ToiletAdmin(admin.ModelAdmin):
    pass
admin.site.register(Toilet, ToiletAdmin)
