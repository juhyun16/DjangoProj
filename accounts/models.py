from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from .choices import BLOODTYPE_CHOICES
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

# Create your models here.

def user_path(instance, filename):
    from uuid import uuid4
    pid = uuid4().hex[:10]
    extension = filename.split('.')[-1]
    return '{}/{}.{}'.format(instance.user.username, pid, extension)


class Profile(models.Model):
    #   user=models.OneToOneField(User)       #   FIXME : BAD CASE!!
    user=models.OneToOneField(settings.AUTH_USER_MODEL)

    phone_number = models.CharField(max_length=15, unique=True)
    nickname = models.CharField(max_length=20, unique=True)
    address = models.CharField(max_length=50, blank=True, default='-')
    email = models.EmailField(max_length=30, blank=True, default='-')
    blood_type=models.IntegerField(choices=BLOODTYPE_CHOICES, default=0)

    picture=ProcessedImageField(processors=[ResizeToFill(150, 150)],
                                format='JPEG',
                                options={'quality':90},
                                upload_to='avatar',
                                default='/media/default-picture.jpg'
                                )


    def __str__(self):
        return self.nickname

