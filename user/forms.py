from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField

class UserRegistrationForm(UserCreationForm):
    
    email = forms.EmailField(
                    max_length=100,
                    required=True,
                    help_text='Enter Email Address',
                    widget=forms.TextInput(attrs={'class': 'form-control shadow-none', 'placeholder': 'Email'}),
                    )

    first_name = forms.CharField(
                    max_length=100,
                    required=True,
                    help_text='Enter First Name',
                    widget=forms.TextInput(attrs={'class': 'form-control shadow-none', 'placeholder': 'First Name'}),
                    )

    last_name = forms.CharField(
                    max_length=100,
                    required=True,
                    help_text='Enter Last Name',
                    widget=forms.TextInput(attrs={'class': 'form-control shadow-none', 'placeholder': 'Last Name'}),
                    )

    username = forms.CharField(
                    max_length=100,
                    required=True,
                    help_text='Enter Username',
                    widget=forms.TextInput(attrs={'class': 'form-control shadow-none', 'placeholder': 'Username'}),
                    )

    password1 = forms.CharField(
                    required=True,
                    help_text='Enter Password',
                    widget=forms.PasswordInput(attrs={'class': 'form-control shadow-none', 'placeholder': 'Password'}),
                    )

    password2 = forms.CharField(
                    required=True,
                    help_text='Enter Password Again',
                    widget=forms.PasswordInput(attrs={'class': 'form-control shadow-none', 'placeholder': 'Password Again'}),
                    )
    class Meta:
        model = User
        fields = [
            'username', 'email', 'first_name', 'last_name', 'password1' ,'password2',
        ]


class UserLoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={"autofocus": True, 'class': 'form-control shadow-none', 'placeholder': 'Username'}))
    password = forms.CharField(
                label=("Password"),
                strip=False,
                widget=forms.PasswordInput(attrs={'autocomplete': 'current-password', 'class': 'form-control shadow-none', 'placeholder': 'Password'}),
                )