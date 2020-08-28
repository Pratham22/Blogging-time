from .models import Post,comment
from django import forms

class cmtform(forms.Form):
    name= forms.CharField(required=True,widget=forms.TextInput(attrs={
        'placeholder':'name',
         'class':'form-control',
    }))
    email=forms.EmailField(required=True,widget=forms.TextInput(attrs={
        'placeholder':'Email',
        'class':'form-control',
    }))
    body=forms.CharField(required=True,widget=forms.TextInput(attrs={
         'placeholder':'Comment',
         'class':'form-control',
    }))
   
class blogform(forms.Form):
    title= forms.CharField(required=True,widget=forms.TextInput(attrs={
        'placeholder':'Title',
         'class':'form-control',
         'id':'title',
         'data-rule':'minlen:2',
        'data-msg':'Please enter at least 2 chars'
    }))
    thum_img=forms.ImageField(required=True)
    cover_img=forms.ImageField(required=True)
    content=forms.CharField(required=True,widget=forms.Textarea(attrs={
         'placeholder':'blog content',
         'class':'form-control',
         'rows':'10',
    }))