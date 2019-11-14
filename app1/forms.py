from django import forms
from .models import author,book

class bookform(forms.ModelForm):
    class Meta:
        model='author'
        fields='__all__'

class authorform(forms.ModelForm):
    class Meta:
        model='book'
        fields='__all__'