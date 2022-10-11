
from django import forms


from . import models

class TaxiForm(forms.ModelForm):
    class Meta:
        model = models.Taxi
        fields='__all__'

        widgets ={
            'date': forms.DateTimeInput(attrs={'type':'date'}),
            'time': forms.TimeInput(attrs={'type':'time'})
        }   