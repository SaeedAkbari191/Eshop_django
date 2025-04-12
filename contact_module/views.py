from django.views.generic.edit import CreateView
from contact_module.forms import ContactUsModelForm
from site_module.models import SiteSetting


# Create your views here.

# def contact(request):
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             return redirect(reverse('home_page'))
#     contact_form = ContactForm()
#     return render(request, 'contact_module/contact_us_page.html', {'contact_form': contact_form})

class ContactUsView(CreateView):
    template_name = 'contact_module/contact_us_page.html'
    form_class = ContactUsModelForm
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super(ContactUsView, self).get_context_data(**kwargs)
        site_setting:SiteSetting = SiteSetting.objects.filter(is_main_setting=True).first()
        context['site_setting'] = site_setting
        return context
