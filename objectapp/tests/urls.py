"""Test urls for the objectapp project"""
from django.contrib import admin
from django.conf.urls.defaults import url
from django.conf.urls.defaults import include
from django.conf.urls.defaults import patterns

from objectapp.urls import urlpatterns

admin.autodiscover()

handler500 = 'django.views.defaults.server_error'
handler404 = 'django.views.defaults.page_not_found'

urlpatterns += patterns(
    '',
    url(r'^channel-test/$', 'objectapp.views.channels.gbobject_channel',
        {'query': 'test'}),
    url(r'^comments/', include('django.contrib.comments.urls')),
    url(r'^xmlrpc/$', 'django_xmlrpc.views.handle_xmlrpc'),
    url(r'^admin/', include(admin.site.urls)),
    )
