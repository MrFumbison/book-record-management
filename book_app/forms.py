from django import forms
from .models import book

class bookcreate(forms.ModelForm):
    
    class Meta:
        model = book
        fields = '__all__'