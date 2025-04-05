from django.db import models


# Create your models here.

class ContactUS(models.Model):
    title = models.CharField(max_length=200, verbose_name="Title")
    email = models.EmailField(max_length=300, verbose_name="Email")
    full_name = models.CharField(max_length=200, verbose_name="Name and last name")
    message = models.TextField(max_length=400, verbose_name="Users Comments")
    response = models.TextField(blank=True, null=True, verbose_name="Replay to Users")
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="Created Date")
    is_read_by_admin = models.BooleanField(default=False, verbose_name="Read by Admin")

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'

    def __str__(self):
        return self.title


class UserProfile(models.Model):
    image = models.ImageField(upload_to="images")
