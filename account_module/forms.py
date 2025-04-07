from django import forms
from django.core import validators
from django.core.exceptions import ValidationError


class RegisterForm(forms.Form):
    username = forms.CharField(
        label='',
        widget=forms.TextInput(
            attrs={
                'class': 'form input',
                'placeholder': 'Username',
            }
        ),
    )
    email = forms.EmailField(
        label='',
        widget=forms.EmailInput(
            attrs={
                'class': 'form input',
                'placeholder': 'Email',
            }
        ),
        validators=[
            validators.MaxLengthValidator(100),
            validators.EmailValidator,
        ]
    )
    password = forms.CharField(
        label='',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form input',
                'placeholder': 'Password',
            }
        ),
        validators=[
            validators.MaxLengthValidator(100),
        ]
    )
    confirm_password = forms.CharField(
        label='',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form input',
                'placeholder': 'Confirm Password',
            }
        )
    )

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if password == confirm_password:
            return confirm_password

        raise ValidationError('Passwords do not match')


class LoginForm(forms.Form):
    email = forms.EmailField(
        label='',
        widget=forms.EmailInput(
            attrs={
                'class': 'form input',
                'placeholder': 'Email',
            }
        ),
        validators=[
            validators.MaxLengthValidator(100),
            validators.EmailValidator,
        ]
    )
    password = forms.CharField(
        label='',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form input',
                'placeholder': 'Password',
            }
        ),
        validators=[
            validators.MaxLengthValidator(100),
        ]
    )
