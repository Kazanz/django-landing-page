from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', 'liloli.views.landing', name='landing'),
    url(r'^admin/', include(admin.site.urls)),
)
