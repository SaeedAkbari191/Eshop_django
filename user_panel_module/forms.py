from django.core import validators

from django import forms
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

