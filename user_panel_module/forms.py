from django.core import validators

from django import forms
from account_module.models import User


class EditProfileModelForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'avatar', 'address']

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

            })
        }

        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'avatar': 'Change Photo',
            'address': 'Address',
        }
        error_messages = {
            'full_name': {
                'required': 'Please enter your Full Name.',
                'max_length': 'Full Name cannot be more than 200 characters.',
            },
            'email': {
                'required': 'Please enter your Email.',
                'max_length': 'Email cannot be more than 100 characters.',
            },
            'title': {
                'required': 'Please enter your Title.',
            },
            'message': {
                'required': 'Please enter your message.',
                'max_length': 'message cannot be more than 200 characters.',
            }

        }
