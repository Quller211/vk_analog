from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import News, UserDescripe

class AddNewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = {'topic_news', 'post_news', 'topic_images'}

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = UserDescripe
        fields = ['date_of_birth']