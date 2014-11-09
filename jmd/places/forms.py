# coding=utf-8
__author__ = 'dmitrij'

from django import forms


class RangeInput(forms.NumberInput):
    input_type = 'range'


class LocationForm(forms.Form):
    lat = forms.FloatField(widget=forms.HiddenInput())
    lng = forms.FloatField(widget=forms.HiddenInput())
    radius = forms.IntegerField(initial=500)

    def __init__(self, *args, **kwargs):
        super(LocationForm, self).__init__(*args, **kwargs)
        self.fields['radius'].widget = RangeInput(
            attrs={'value': "500", 'min': "0", 'max': "1000", 'step': '25'})
        self.fields["radius"].label=False


from .models import Comment


class CommentForm(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        super(CommentForm,self).__init__(*args,**kwargs)
        self.fields["text"].widget=forms.TextInput(attrs={"placeHolder":"Your comment ..."})
        self.fields["text"].label=False

    class Meta:
        model = Comment
        fields = ('text',)