# coding=utf-8
__author__ = 'dmitrij'

from tastypie.resources import ModelResource

from places.models import Place

class PlaceResource(ModelResource):
    class Meta:
        queryset = Place.objects.all()
        resource_name = 'places'