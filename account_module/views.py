from django.http import Http404
from django.contrib.auth import login
from django.http import Http404
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils.crypto import get_random_string
from django.views.generic import View

from .forms import RegisterForm, LoginForm
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
                return redirect(reverse('login_page'))

            context = {
                'register_form': register_form
            }
            return render(request, 'account_module/register_page.html', context)


class LoginView(View):
    def get(self, request):
        login_form = LoginForm()
        context = {
            'login_form': login_form
        }
        return render(request, 'account_module/login_page.html', context)

    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user_email = login_form.cleaned_data.get('email')
            user_password = login_form.cleaned_data.get('password')
            user: User = User.objects.filter(email__iexact=user_email).first()
            if user is not None:
                if not user.is_active:
                    login_form.add_error('email', 'User is not active')
                else:
                    correct_password = user.check_password(user_password)
                    if correct_password:
                        login(request, user)
                        return redirect(reverse('home_page'))
                    else:
                        login_form.add_error('email', 'Incorrect email or password')
            else:
                login_form.add_error('email', 'Email does not exist')

        context = {
            'login_form': login_form
        }
        return render(request, 'account_module/login_page.html', context)


class ActivateAccountView(View):
    def get(self, request, email_active_code):
        user: User = User.objects.filter(email_active_code__iexact=email_active_code).first()
        if user is not None:
            if not user.is_active:
                user.is_active = True
                user.email_active_code = get_random_string(72)
                user.save()
                # todo show successful messafe
                return redirect(reverse('login_page'))
            else:
                pass
                # todo your account was activate
        raise Http404
