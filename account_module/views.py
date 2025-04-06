from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils.crypto import get_random_string
from django.views.generic import View

from .forms import RegisterForm
from .models import User


# Create your views here.

class RegisterView(View):
    def get(self, request):
        register_form = RegisterForm()

        context = {
            'register_form': register_form
        }
        return render(request, 'account_module/register_page.html', context)

    def post(self, request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            username = register_form.cleaned_data.get('username')
            user_email = register_form.cleaned_data.get('email')
            user_password = register_form.cleaned_data.get('password')
            user: bool = User.objects.filter(username__iexact=username).exists()
            if user:
                register_form.add_error('username', 'Username already exists')

            email_user: bool = User.objects.filter(email__iexact=user_email).exists()
            if email_user:
                register_form.add_error('email', 'Email already exists')
            else:
                new_user = User(
                    email=user_email,
                    email_active_code=get_random_string(72),
                    is_active=False,
                    username=username
                )
                new_user.set_password(user_password)
                new_user.save()
                # todo: send email active code
                # send_email('فعالسازی حساب کاربری', new_user.email, {'user': new_user}, 'emails/activate_account.html')
                return redirect(reverse('home_page'))

            context = {
                'register_form': register_form
            }
            return render(request, 'account_module/register_page.html', context)
