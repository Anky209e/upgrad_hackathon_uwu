from django import forms
from . import models

class FakeNewsForm(forms.ModelForm):
    class Meta:
        model = models.fakenews
        fields ="__all__"
        