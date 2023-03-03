from django import forms
from .models import Adil
class Updateform(forms.ModelForm):
    class Meta:
        model=Adil
        fields='__all__'
        exclude = ['user']

        

