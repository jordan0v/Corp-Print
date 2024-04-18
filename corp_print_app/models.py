from django.db import models
from django.conf import settings


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True)

    def __str__(self):
        return 'Profile for user {}'.format(self.user.username)
    

class PrintTemplate(models.Model):
    name = models.CharField(max_length=100)
    size = models.CharField(max_length=50)
    background_image = models.ImageField(upload_to='corp_print_app/media/')
    logo = models.ImageField(upload_to='corp_print_app/media/', blank=True, null=True)
    text = models.TextField(blank=True, null=True)
    font = models.CharField(max_length=50, blank=True, null=True)
    # Другие поля по вашему усмотрению

    def __str__(self):
        return self.name
