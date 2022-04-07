from calendar import c
from django import forms
from articles.models import Article

class ArticleForm(forms.ModelForm):
    title = forms.CharField(
        label='제목',
        widget=forms.TextInput(
            attrs={
                'class': 'my-title',
                'placeholder': 'Enter the title',
            }
        )
    )
    class Meta:
        model = Article
        fields = '__all__'