# coding=utf-8
__author__ = 'dmitrij'
from django.conf.urls import patterns, include, url

urlpatterns = patterns('web.views',
    # Examples:
    # url(r'^$', 'jmd.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'home', name='home'),
    #url(r'^frsq/$', 'frsq', name='frsq'),
    #url(r'^venues/$', 'venues', name='venues'),
    #url(r'^venues/(?P<id>[\w-]+)$', 'detail', name='detail'),
)
