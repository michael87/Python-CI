from django.conf.urls.defaults import *

urlpatterns = patterns('projects.views',
    url(r'^create/$',  'create'),
    url(r'^statistics/$',  'create'),
    url(r'^advanced/settings/$',  'create'),
    url(r'^advanced/build/$',  'create'),
    url(r'^remove/(?P<project_id>.+)$',  'remove'),
)