from django.conf.urls import patterns, include, url
from django.contrib import admin

from tastypie.api import Api

from .api import PlaceResource

v1_api = Api(api_name='v1')
v1_api.register(PlaceResource())


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'jmd.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^api/', include(v1_api.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^places/', include('places.urls')),
    url(r'^', include('web.urls')),
)
