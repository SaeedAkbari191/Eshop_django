# Create your models here.
from django.db import models


# Create your models here.
class SiteSetting(models.Model):
    site_name = models.CharField(max_length=100, verbose_name="Site Name")
    url_name = models.CharField(max_length=100, verbose_name="Site Domain Name")
    address = models.CharField(max_length=100, verbose_name="Address")
    phone = models.CharField(max_length=100, null=True, blank=True, verbose_name="Phone Number")
    fax = models.CharField(max_length=100, null=True, blank=True, verbose_name="Fax")
    email = models.CharField(max_length=100, null=True, blank=True, verbose_name="Email")
    copy_right = models.CharField(max_length=100, verbose_name="Copyright")
    about_us_text = models.TextField(verbose_name="About Us")
    site_logo = models.ImageField(verbose_name="Site Logo", upload_to="images/site_setting/")
    is_main_setting = models.BooleanField(default=False, verbose_name="Main Setting")

    def __str__(self):
        return self.site_name

    class Meta:
        verbose_name = "Site Setting"
        verbose_name_plural = "Site Settings"


class FooterLinkBox(models.Model):
    title = models.CharField(max_length=100, verbose_name="Title")

    class Meta:
        verbose_name = "Footer Link Box"
        verbose_name_plural = "Footer Links Box"

    def __str__(self):
        return self.title


class FooterLink(models.Model):
    title = models.CharField(max_length=100, verbose_name="Title")
    url = models.URLField(verbose_name="URL", max_length=400)
    footer_link_box = models.ForeignKey(FooterLinkBox, verbose_name="Footer Link Box", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Footer Link"
        verbose_name_plural = "Footer Links"

    def __str__(self):
        return self.title


class Sliders(models.Model):
    title = models.CharField(max_length=200, verbose_name="Title")
    url = models.URLField(max_length=400, verbose_name='link')
    url_title = models.CharField(max_length=100, verbose_name="URL Title")
    description = models.TextField(verbose_name="Description")
    is_active = models.BooleanField(default=True, verbose_name="Active")
    image = models.ImageField(verbose_name="Image", upload_to="images/sliders")

    class Meta:
        verbose_name = "Slider"
        verbose_name_plural = "Sliders"

    def __str__(self):
        return self.title


class SiteBanner(models.Model):
    class SiteBannerPosition(models.TextChoices):
        home = 'home', 'Home page',
        product_list = 'product_list', 'Product List page',
        product_details = 'product_details', 'Product Details Page'

    title = models.CharField(max_length=200, verbose_name="Banner Title")
    url_title = models.URLField(max_length=400, verbose_name='Banner URL')
    image = models.ImageField(verbose_name="Banner Image", upload_to="images/site_banner")
    is_active = models.BooleanField(default=True, verbose_name="Active")
    position = models.CharField(max_length=200, choices=SiteBannerPosition.choices, verbose_name="Display Position")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Site Banner"
        verbose_name_plural = "Site Banners"
