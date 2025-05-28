import uuid
from msilib.schema import ListView

from django.conf import settings
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, JsonResponse, Http404
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView, ListView
from django.views.generic import View
from paypal.standard.forms import PayPalPaymentsForm

from account_module.models import User
from order_module.models import Order, OrderDetail
from user_panel_module.forms import EditProfileModelForm, ChangePasswordForm


# Create your views here.

@method_decorator(login_required, name='dispatch')
class UserPanelDashboardView(TemplateView):
    template_name = 'user_panel_module/user_panel_dashboard_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        request: HttpRequest = self.request
        current_user = User.objects.filter(id=request.user.id).first()
        order_detail = Order.objects.filter(user_id=request.user.id, is_paid=True)

        context = {
            'current_user': current_user,
            'order_detail': order_detail,
        }
        return context


@method_decorator(login_required, name='dispatch')
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


@method_decorator(login_required, name='dispatch')
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


def setting(request):
    return render(request, 'user_panel_module/settings.html')


def user_panel_menu_components(request):
    current_user: User = User.objects.filter(id=request.user.id).first()
    context = {
        'current_user': current_user,
    }
    return render(request, 'user_panel_module/includes/user_panel_menu_components.html', context)


@method_decorator(login_required, name='dispatch')
class UserBasket(View):
    def get(self, request: HttpRequest):
        current_order, created = Order.objects.prefetch_related('orderdetail_set').get_or_create(is_paid=False,
                                                                                                 user=request.user)
        total_amount = current_order.calculate_total_price()
        host = request.get_host()
        # PAYPAL

        paypal_dict = {
            "business": settings.PAYPAL_RECEIVER_EMAIL,
            "amount": total_amount,
            "item_name": ' test',
            'no_shipping': '2',
            "invoice": str(uuid.uuid4()),
            'currency_code': 'USD',
            "notify_url": request.build_absolute_uri(reverse('paypal-ipn')),
            "return_url": request.build_absolute_uri(reverse('payment_success_page')),  # SUCCESS
            "cancel_url": request.build_absolute_uri(reverse('payment_failure_page')),  # CANCEL
            "custom": "premium_plan",  # Custom command to correlate to some function later (optional)
        }
        payment_form = PayPalPaymentsForm(initial=paypal_dict)

        context = {
            'order': current_order,
            'sum': total_amount,
            'payment_form': payment_form,
        }
        return render(request, 'user_panel_module/user_basket.html', context)

    def post(self, request: HttpRequest):
        current_order, created = Order.objects.prefetch_related('orderdetail_set').get_or_create(is_paid=False,
                                                                                                 user=request.user)
        total_amount = current_order.calculate_total_price()
        host = request.get_host()
        # PAYPAL

        paypal_dict = {
            "business": settings.PAYPAL_RECEIVER_EMAIL,
            "amount": total_amount,
            "item_name": ' test',
            'no_shipping': '2',
            "invoice": str(uuid.uuid4()),
            'currency_code': 'USD',
            "notify_url": request.build_absolute_uri(reverse('paypal-ipn')),
            "return_url": request.build_absolute_uri(reverse('payment_success_page')),  # SUCCESS
            "cancel_url": request.build_absolute_uri(reverse('payment_failure_page')),  # CANCEL
            "custom": "premium_plan",  # Custom command to correlate to some function later (optional)
        }
        payment_form = PayPalPaymentsForm(initial=paypal_dict)

        context = {
            'order': current_order,
            'sum': total_amount,
            'payment_form': payment_form,
        }
        return render(request, 'user_panel_module/user_basket.html', context)


@login_required
def remove_order_detail(request: HttpRequest):
    detail_id = request.GET.get('detail_id')
    if detail_id is None:
        return JsonResponse({
            'status': 'not_found_detail_id',
        })

    delete_count, delete_dict = OrderDetail.objects.filter(id=detail_id, order__is_paid=False,
                                                           order__user_id=request.user).delete()
    if delete_count == 0:
        return JsonResponse({
            'status': 'detail_not_found',
        })

    current_order, created = Order.objects.prefetch_related('orderdetail_set').get_or_create(
        is_paid=False, user=request.user)
    total_amount = current_order.calculate_total_price()

    context = {
        'order': current_order,
        'sum': total_amount
    }

    return JsonResponse({
        'status': 'success',
        'body': render_to_string('user_panel_module/user_basket_content.html', context)
    })


@login_required
def changeOrderDetailCount(request: HttpRequest):
    detail_id = request.GET.get('detail_id')
    state = request.GET.get('state')

    if detail_id is None or state is None:
        return JsonResponse({
            'status': 'not_found_detail_id_or_state',
        })
    order_detail: OrderDetail = OrderDetail.objects.filter(id=detail_id, order__user_id=request.user,
                                                           order__is_paid=False).first()
    if order_detail is None:
        return JsonResponse({
            'status': 'detail_not_found',
        })

    if state == 'increase':
        order_detail.count += 1
        order_detail.save()
    elif state == 'decrease':
        if order_detail.count == 1:
            order_detail.delete()
        else:
            order_detail.count -= 1
            order_detail.save()
    else:
        return JsonResponse({
            'status': 'state_invalid',
        })

    current_order, created = Order.objects.prefetch_related('orderdetail_set').get_or_create(
        is_paid=False, user=request.user)
    total_amount = current_order.calculate_total_price()

    context = {
        'order': current_order,
        'sum': total_amount
    }

    return JsonResponse({
        'status': 'success',
        'body': render_to_string('user_panel_module/user_basket_content.html', context)
    })


def payment_success(request: HttpRequest):
    print(request.user.id)
    print(request.user)
    return render(request, 'user_panel_module/payment_success.html')


def payment_failure(request: HttpRequest):
    return render(request, 'user_panel_module/payment_failure.html')


@method_decorator(login_required, name='dispatch')
class MyShoppingPage(ListView):
    template_name = 'user_panel_module/user_shopping.html'
    model = Order

    def get_queryset(self):
        queryset = super().get_queryset()
        request = self.request
        queryset = queryset.filter(user_id=request.user.id, is_paid=True)
        return queryset


def my_shopping_details(request: HttpRequest, order_id):
    order = Order.objects.filter(id=order_id, user_id=request.user).first()
    if order is None:
        raise Http404('Not Fount')
    return render(request, 'user_panel_module/user_shopping_details.html', context={'orders': order})
