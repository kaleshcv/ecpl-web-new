from django import forms
from . import models


class Candidate(forms.ModelForm):
    class Meta:
        model=models.Candidate
        fields=['name','email','phone','resume']
