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

class PostForm(forms.ModelForm):
    
    class Meta:
        model = Post
        #fields="__all__"
        fields = ('title','thumnail_image','main_img','content')
       
