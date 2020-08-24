from .models import Post,comment
from django import forms
class commentform(forms.ModelForm):
    class Meta:
        model=comment
        fields=('name','email','body')