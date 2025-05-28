from django import forms
from django.core import validators
from django.core.exceptions import ValidationError
from account_module.models import User


class EditProfileModelForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'avatar', 'address', 'about_user']

        widgets = {
            'first_name': forms.TextInput(attrs={
                'placeholder': 'First Name',
                'id': 'first_name'

            }),
            'last_name': forms.TextInput(attrs={
                'placeholder': 'Last Name',
                'id': 'last_name'

            }),

            'avatar': forms.FileInput(attrs={
                'id': 'imageUpload',
                'style': 'display: none'
            }),

            'address': forms.Textarea(attrs={
                'placeholder': 'Address',
                'rows': 3,
                'id': 'address',

            }),

            'about_user': forms.Textarea(attrs={
                'placeholder': 'About User',
                'rows': 5,
                'id': 'about_user',

            })
        }

        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'avatar': 'Change Photo',
            'address': 'Address',
            'about_user': 'About User'
        }


class ChangePasswordForm(forms.Form):
    current_password = forms.CharField(
        label='Current Password',
        widget=forms.PasswordInput(
            attrs={
                'id': 'current_password',
                'placeholder': '',
            }
        ),
        validators=[
            validators.MaxLengthValidator(100),
        ]
    )
    password = forms.CharField(
        label='New Password',
        widget=forms.PasswordInput(
            attrs={
                'id': 'new_password',
                'placeholder': '',
            }
        )
    )

    confirm_password = forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput(
            attrs={
                'id': 'confirm_password',
                'placeholder': '',
            }
        )
    )

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if password == confirm_password:
            return confirm_password

        raise ValidationError('Passwords do not match')
