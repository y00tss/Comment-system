"""
User forms for SignUp and ProfileEdit
"""

from django import forms
from django.contrib.auth.forms import UserCreationForm
from user.models import CustomUser


class LoginForm(forms.Form):
    """Form to provide user login"""
    username = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(label='Password', widget=forms.PasswordInput())


class SignUpForm(UserCreationForm):
    """Form to provide user registration"""

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2')


class ProfileEditForm(forms.ModelForm):
    """Form to provide user profile editing"""

    class Meta:
        model = CustomUser
        fields = ('avatar', 'first_name', 'last_name', 'email', 'sex')
