# coding=utf-8
__author__ = 'dmitrij'

from django import forms

class LocationForm(forms.Form):
    lat = forms.FloatField(widget=forms.HiddenInput())
    lng = forms.FloatField(widget=forms.HiddenInput())
    radius = forms.IntegerField(initial=500)


from .models import Comment
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)