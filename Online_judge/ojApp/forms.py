from django import forms
from .models import submissions

class submission_form(forms.Form):
    submitted_code = forms.FileField()

        
