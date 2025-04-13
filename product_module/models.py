from django.urls import reverse
from django.db import models
from django.utils.text import slugify


# Create your models here.
class ProductCategory(models.Model):
    parent = models.ForeignKey('ProductCategory', on_delete=models.CASCADE, null=True, blank=True,
                               verbose_name='Parent Category')
    title = models.CharField(max_length=300, db_index=True, verbose_name="Title")
    url_title = models.CharField(max_length=300, db_index=True, verbose_name="url-title")
    is_active = models.BooleanField(default=True, verbose_name="Active / Passive")
    is_deleted = models.BooleanField(default=False, verbose_name="Deleted")

    def __str__(self):
        return f'({self.title} , {self.url_title})'

    class Meta:
        verbose_name = 'Product Category'
        verbose_name_plural = 'Category Products'


class ProductBrand(models.Model):
    title = models.CharField(max_length=300, db_index=True, verbose_name="Brand name")
    url_title = models.CharField(max_length=300, db_index=True, verbose_name="url-title")
    is_active = models.BooleanField(verbose_name="Active / Passive")

    class Meta:
        verbose_name = 'Product Brand'
        verbose_name_plural = 'Product Brands'

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=300)
    category = models.ManyToManyField(ProductCategory,
                                      verbose_name="Category",
                                      related_name="product_category")
    image = models.ImageField(upload_to='product', verbose_name='Product Image', blank=True, null=True)
    brand = models.ForeignKey(ProductBrand, verbose_name="Brand", on_delete=models.CASCADE, null=True, blank=True)
    quantity = models.PositiveIntegerField(verbose_name="Quantity")
    price = models.IntegerField(verbose_name="Price")
    old_price = models.IntegerField(verbose_name="Old Price")
    short_description = models.CharField(max_length=300, null=True, verbose_name="Short Description")
    description = models.TextField(verbose_name="Description")
    is_active = models.BooleanField(default=False, verbose_name="Active / passive")
    slug = models.SlugField(default="", null=False, blank=True, max_length=200, unique=True, db_index=True)
    is_deleted = models.BooleanField(default=False, verbose_name="Deleted")

    def __str__(self):
        return f"{self.title} ({self.price})"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("product_detail", args=[self.slug])

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'


class ProductTag(models.Model):
    caption = models.CharField(max_length=50, db_index=True, verbose_name="Title")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='product_tags',
                                related_name='product_tags')

    def __str__(self):
        return self.caption

    class Meta:
        verbose_name = 'Product Tag'
        verbose_name_plural = 'Product Tags'
