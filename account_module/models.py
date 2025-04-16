from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    avatar = models.ImageField(upload_to="images/Profile", null=True, blank=True, verbose_name="Avatar Picture")
    email_active_code = models.CharField(max_length=100, verbose_name="Email Active Code")
    about_user = models.TextField(verbose_name="About User", max_length=500, null=True, blank=True)
    address = models.TextField(verbose_name="Address", max_length=500, null=True, blank=True)
    mobile = models.CharField(max_length=15, verbose_name="Mobile Number", null=True, blank=True)

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        if self.first_name and self.last_name:
            return self.get_full_name()
        return self.email
