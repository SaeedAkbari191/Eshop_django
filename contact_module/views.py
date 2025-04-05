from django.views.generic.edit import CreateView
from contact_module.forms import ContactUsModelForm


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


