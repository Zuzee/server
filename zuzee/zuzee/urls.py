from django.conf.urls import patterns, include, url
from django.views.decorators.csrf import csrf_exempt
#from toilet.views import AddView
from tastypie.api import Api
from toilet.api import UserResource, ToiletResource

from django.contrib import admin
admin.autodiscover()

v1_api = Api(api_name='v1')
v1_api.register(UserResource())
v1_api.register(ToiletResource())

urlpatterns = patterns('',
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^toilet/add/$', csrf_exempt(AddView.as_view()), name='add'),
    url(r'^api/', include(v1_api.urls)),
)
