# coding=utf-8
__author__ = 'dmitrij'
from django.conf.urls import patterns, include, url

urlpatterns = patterns('places.views',
                       # Examples:
                       # url(r'^$', 'jmd.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),

                       url(r'^$', 'home', name='places_home'),
                       url(r'^around/$', 'around', name='places_around'),
                       url(r'^(?P<uid>[\w-]+)$', 'detail', name='place_detail'),
)
