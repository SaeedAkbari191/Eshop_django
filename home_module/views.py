from django.shortcuts import render
from django.views.generic import View, TemplateView
from site_module.models import SiteSetting, FooterLinkBox
from product_module.models import Product


# Create your views here.

# class HomeView(View):
#     def get(self, request):
#         return render(request, 'home_module/index_page.html')

class HomeView(TemplateView):
    template_name = 'home_module/index_page.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context = {
            'title': 'Home Page',
            'data': 'this is test'
        }
        return context


def site_header_components(request):
    setting = SiteSetting.objects.filter(is_main_setting=True).first()
    context = {
        'site_setting': setting
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
