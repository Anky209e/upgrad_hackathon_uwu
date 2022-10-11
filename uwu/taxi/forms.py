from attr import fields
from django import forms
from django import forms
from matplotlib import widgets
from . import models

class TaxiForm(forms.ModelForm):
    class Meta:
        model = models.Taxi
        fields='__all__'

        widgets ={
            'date': forms.DateTimeInput(attrs={'type':'datetime'})
        }