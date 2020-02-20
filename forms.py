from django import forms
from .models import Edata

class Edatass(forms.ModelForm):
    class Meta:
        model = Edata
        fields = "__all__"
    
   