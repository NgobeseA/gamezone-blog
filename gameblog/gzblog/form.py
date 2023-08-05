from django import forms
from .models import Article

class NewArticle(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'author', 'title_tag', 'description', 'body',]

        widgets = {
            'author': forms.Select(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class' : 'form-control'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }