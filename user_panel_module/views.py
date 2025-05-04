from lib2to3.fixes.fix_input import context

from django.contrib.auth.hashers import check_password
from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import TemplateView
from django.views.generic import View
from django.contrib.auth import login, logout

from account_module.models import User
from order_module.models import Order
from user_panel_module.forms import EditProfileModelForm, ChangePasswordForm


# Create your views here.


class UserPanelDashboardView(TemplateView):
    template_name = 'user_panel_module/user_panel_dashboard_page.html'


class EditProfilePageView(View):
    def get(self, request):
        current_user = User.objects.filter(id=request.user.id).first()
        edit_profile_form = EditProfileModelForm(instance=current_user)
        context = {
            'edit_profile_form': edit_profile_form,
            'current_user': current_user,
        }
        return render(request, 'user_panel_module/edit_profile_page.html', context)

    def post(self, request: HttpRequest):
        current_user = User.objects.filter(id=request.user.id).first()
        edit_profile_form = EditProfileModelForm(request.POST, request.FILES, instance=current_user)
        if edit_profile_form.is_valid():
            edit_profile_form.save(commit=True)
        context = {
            'edit_profile_form': edit_profile_form,
            'current_user': current_user,
        }
        return render(request, 'user_panel_module/edit_profile_page.html', context)


def setting(request):
    return render(request, 'user_panel_module/settings.html')


class ChangePasswordPageView(View):
    def get(self, request: HttpRequest):
        form = ChangePasswordForm()
        context = {
            'change_password_form': form
        }
        return render(request, 'user_panel_module/settings.html', context)

    def post(self, request: HttpRequest):
        form = ChangePasswordForm(request.POST)
        if form.is_valid():
            current_user: User = User.objects.filter(id=request.user.id).first()
            current_password = form.cleaned_data.get('current_password')

            if current_user.check_password(current_password):
                password = form.cleaned_data.get('password')
                current_user.set_password(password)
                current_user.save()
                logout(request)
                return redirect(reverse('login_page'))

            else:
                form.add_error('current_password', 'Current password is incorrect.')

        context = {
            'change_password_form': form
        }
        return render(request, 'user_panel_module/settings.html', context)


def user_panel_menu_components(request):
    current_user: User = User.objects.filter(id=request.user.id).first()
    context = {
        'current_user': current_user,
    }
    return render(request, 'user_panel_module/includes/user_panel_menu_components.html', context)


def user_basket(request: HttpRequest):
    current_order, created = Order.objects.get_or_create(is_paid=False, user=request.user)
    total = 0

    for detail in current_order.orderdetail_set.all():
        print(detail.product.price * detail.count)
        total += detail.product.price * detail.count

    context = {
        'order': current_order,
        'sum': total
    }
    return render(request, 'user_panel_module/user_basket.html', context)
