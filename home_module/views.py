from django.shortcuts import render
from django.views.generic import View, TemplateView


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
    return render(request, 'shared/site_header_components.html')


def site_footer_components(request):
    return render(request, 'shared/site_footer_components.html')
