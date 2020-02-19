from django import forms

class Sdata(forms.Form):
    id = forms.IntegerField()
    name = forms.CharField(max_length = 50)
    location = forms.CharField(max_length = 50)
    dob = forms.DateField()

  