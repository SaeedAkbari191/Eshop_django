from django.core import validators

from django import forms
from .models import ContactUS


class ContactUsModelForm(forms.ModelForm):
    class Meta:
        model = ContactUS
        fields = ['full_name', 'email', 'title', 'message']

        widgets = {
            'full_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Full Name'

            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Email'
            }),

            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Subject'
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Message',
                'rows': '5',
                'cols': '7',
                'id': 'message',

            })
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
