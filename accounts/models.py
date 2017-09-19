from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
# Create your models here.




class Profile(models.Model):
    #   user=models.OneToOneField(User)       #   FIXME : BAD CASE!!
    user=models.OneToOneField(settings.AUTH_USER_MODEL)

    phone_number = models.CharField(max_length=15, unique=True)
    nickname = models.CharField(max_length=20, unique=True)
    address = models.CharField(max_length=50, blank=True, default='-')
    email = models.EmailField(max_length=30, blank=True, default='-')

    def __str__(self):
        return self.nickname

