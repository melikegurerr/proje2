
from django import forms # Django'nun forms modülünü içe aktarır,form tanımlayabilmek için gereklidir.

# Arama motoru formunu tanımlayan sınıf
class SearchForm(forms.Form):
    kitap_adi= forms.CharField(max_length=100,required=True) # Önceden models.py'de tanımladığımız kitap_adi fonksiyonu çağırılır.
