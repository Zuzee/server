from django.contrib.auth.models import User
from tastypie import fields
from tastypie.resources import ModelResource
from toilet.models import Toilet


class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        resource_name = 'user'

class ToiletResource(ModelResource):
    user = fields.ForeignKey(UserResource, 'user')
    
    class Meta:
        queryset = Toilet.objects.all()
        resource_name = 'toilet'

