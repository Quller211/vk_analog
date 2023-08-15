from django import forms
from .models import MainPage, Login, News

class MainPageForm(forms.ModelForm):
    class Meta:
        model = MainPage
        fields = ['name', 'city', 'date_of_birth', 'email']

class MainLoginForm(forms.ModelForm):
    class Meta:
        model = Login
        fields = ['user_login']

class AddNewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = {'topic_news', 'post_news', 'topic_images'}