from django.conf.urls import patterns, include, url
from toilet.views import AddView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^toilet/add/$', AddView.as_view(), name='add')
)
