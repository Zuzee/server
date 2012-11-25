from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from tastypie import fields
from tastypie.resources import ModelResource
from tastypie.authentication import Authentication
from tastypie.authorization import Authorization
from toilet.models import Toilet


class ZuzeeAuthentication(Authentication):
    def is_authenticated(self, request, **kwargs):
        # if token found in request.POST / GET matchesa user
        # then authenticate user and return True
        if request and request.GET.has_key('login_username') and request.GET.has_key('login_password'):
            username = request.GET['login_username']
            password = request.GET['login_password']
            user = authenticate(username=username, password=password)
            if user is not None and user.is_active:
                login(request, user)
                return True

            return False

    def get_identifier(self, request):
        return request.user.username

class ZuzeeAuthorization(Authorization):
    def is_authorized(self, request, object=None):
        return True

    #def apply_limits(self, request, object_list):
    #    if request and hasattr(request, 'user'):
    #        return object_list.filter(user__username=request.user.username)
    #
    #    return object_list.none()

class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        resource_name = 'user'
        fields = ['username', 'first_name', 'last_name', 'last_login']
        allowed_methods = ['get']
        authentication = ZuzeeAuthentication()
        authorization = ZuzeeAuthorization()


class ToiletResource(ModelResource):
    user = fields.ForeignKey(UserResource, 'user')

    class Meta:
        queryset = Toilet.objects.all()
        resource_name = 'toilet'

