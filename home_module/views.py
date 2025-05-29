from django.db.models import Count, Sum
from django.http import HttpRequest
from django.shortcuts import render
from django.views.generic import View, TemplateView
from urllib3 import request

from site_module.models import SiteSetting, FooterLinkBox, Sliders, SiteBanner
from product_module.models import Product, ProductCategory
from utils.convertor import group_list
from utils.http_service import get_client_ip
from order_module.models import Order


# Create your views here.

# class HomeView(View):
#     def get(self, request):
#         return render(request, 'home_module/index_page.html')

class HomeView(TemplateView):
    template_name = 'home_module/index_page.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)

        sliders = Sliders.objects.filter(is_active=True)
        banners = SiteBanner.objects.filter(is_active=True, position__iexact=SiteBanner.SiteBannerPosition.home)
        latest_product = Product.objects.filter(is_active=True, is_deleted=False).order_by('-id')[:5]
        most_visit_product = Product.objects.filter(is_active=True, is_deleted=False).annotate(
            visit_count=Count('productvisit')).order_by('-visit_count')[:12]
        product_main_category = ProductCategory.objects.prefetch_related('productcategory_set').filter(is_active=True,
                                                                                                       parent_id=None)

        most_bought_products = Product.objects.filter(orderdetail__order__is_paid=True).annotate(order_count=Sum(
            'orderdetail__count')).order_by('order_count')[:12]

        context = {
            'sliders': sliders,
            'main_categories': product_main_category,
            'top_banners': banners[:3],
            'middle_banners': banners[3:5],
            'bottom_banners': banners[5:8],
            'latest_product': latest_product,
            'most_visit_product': most_visit_product,
            'most_bought_products': most_bought_products,
        }

        return context


def site_header_components(request):
    setting = SiteSetting.objects.filter(is_main_setting=True).first()
    current_order, created = Order.objects.prefetch_related('orderdetail_set').get_or_create(is_paid=False,
                                                                                             user=request.user)
    order_detail = current_order.orderdetail_set.all()[:2]
    count_item = current_order.orderdetail_set.aggregate(total=Sum('count'))['total'] or 0
    total_amount = current_order.calculate_total_price()
    context = {
        'site_setting': setting,
        'order': order_detail,
        'sum': total_amount,
        'count_item': count_item,
    }
    return render(request, 'shared/site_header_components.html', context)


def site_footer_components(request):
    setting = SiteSetting.objects.filter(is_main_setting=True).first()
    footer_link_boxes: FooterLinkBox = FooterLinkBox.objects.all()
    context = {
        'site_setting': setting,
        'footer_link_boxes': footer_link_boxes
    }
    return render(request, 'shared/site_footer_components.html', context)


class AboutView(TemplateView):
    template_name = 'home_module/AboutUs.html'

    def get_context_data(self, **kwargs):
        context = super(AboutView, self).get_context_data(**kwargs)
        site_setting: SiteSetting = SiteSetting.objects.filter(is_main_setting=True).first()
        context = {
            'site_setting': site_setting
        }
        return context
