from django import forms
from django.contrib.auth.forms import UserCreationForm as BaseUserCreationForm
from django.contrib.auth import authenticate
from .models import User, Discussion


class UserCreationForm(BaseUserCreationForm):
    email = forms.EmailField(required=True)
    mobile_no = forms.CharField(max_length=15, required=True)

    class Meta(BaseUserCreationForm.Meta):
        model = User
        fields = ('username', 'email', 'mobile_no', 'password1', 'password2')


class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if user is None:
            raise forms.ValidationError('Invalid username or password')
        return cleaned_data


class DiscussionForm(forms.ModelForm):
    class Meta:
        model = Discussion
        fields = ['text', 'image', 'hashtags']
