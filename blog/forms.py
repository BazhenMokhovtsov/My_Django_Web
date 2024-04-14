from django import forms
from .models import Comments

class CreateCommendForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['text']
        widgets = {'text': forms.Textarea(attrs={'cols':50, 'rows': 1})}
       