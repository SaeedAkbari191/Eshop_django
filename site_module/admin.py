from django.contrib import admin
from .models import SiteSetting, FooterLink, FooterLinkBox, Sliders, SiteBanner

# Register your models here.


admin.site.register(SiteSetting)
admin.site.register(FooterLink)
admin.site.register(FooterLinkBox)
admin.site.register(Sliders)
admin.site.register(SiteBanner)
