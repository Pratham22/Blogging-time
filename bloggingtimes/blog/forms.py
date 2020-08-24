from .models import Post,comment
from django import forms

class cmtform(forms.Form):
    name= forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':'name',
         'class':'form-control',
    }))
    email=forms.EmailField(required=True,widget=forms.TextInput(attrs={
        'placeholder':'Email',
        'class':'form-control',
    }))
    body=forms.CharField(widget=forms.TextInput(attrs={
         'placeholder':'Comment',
         'class':'form-control',
    }))
   
