# coding=utf-8
__author__ = 'dmitrij'

from django import forms

class LocationForm(forms.Form):
    lat = forms.FloatField()
    lng = forms.FloatField()
    radius = forms.IntegerField(initial=500)