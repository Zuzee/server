from django.conf.urls import patterns, include, url
from django.views.decorators.csrf import csrf_exempt
from toilet.views import AddView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^toilet/add/$', csrf_exempt(AddView.as_view()), name='add')
)
