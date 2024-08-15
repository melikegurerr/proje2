
from django import forms

class SearchForm(forms.Form):
    kitap_adi= forms.CharField(max_length=100,required=True)
