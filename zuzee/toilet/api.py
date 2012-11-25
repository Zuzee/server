from tastypie.resources import ModelResource
from toilet.models import Toilet

class ToiletResource(ModelResource):
    class Meta:
        queryset = Toilet.objects.all()
        resource_name = 'toilet'
