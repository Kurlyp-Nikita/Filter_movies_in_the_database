from django import forms
from django.core.validators import RegexValidator
from .models import *
from django.forms import ModelForm




class FilmForm(ModelForm):

    class Meta:
        model = Film
        fields = ['country', 'title', 'year']


class FilmPoisk(forms.Form):
    country = forms.CharField(max_length=30, required=False)
    title = forms.ModelChoiceField(Film.objects.all(), required=False)
    year = forms.FloatField(required=False)
    ex = forms.BooleanField(required=False, label='Исключение года')


