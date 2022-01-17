from typing_extensions import Required
from django import forms

class SearchForm(forms.Form):
    label = forms.CharField(required=True)
