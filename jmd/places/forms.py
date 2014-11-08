# coding=utf-8
__author__ = 'dmitrij'

from django import forms


class LocationForm(forms.Form):
    lat = forms.FloatField(widget=forms.HiddenInput())
    lng = forms.FloatField(widget=forms.HiddenInput())
    radius = forms.IntegerField(initial=500)

    def __init__(self, *args, **kwargs):
        super(LocationForm, self).__init__(*args, **kwargs)
        self.fields['radius'].widget.attrs = {'data-slider': True, 'data-slider-range': "100,1000",
                                              'data-slider-step': 100}


from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)