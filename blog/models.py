from django.db import models
from django.core.urlresolvers import reverse
from django.conf import settings
from .choices import POSTTYPE_CHOICES, BLOODTYPE_CHOICES
# Create your models here.

class Post(models.Model):
    author=models.ForeignKey(settings.AUTH_USER_MODEL)
    title=models.CharField(verbose_name='TITLE', max_length=50)
    post_type=models.CharField(max_length=1, choices=POSTTYPE_CHOICES)
    blood_type=models.IntegerField(blank=True, choices=BLOODTYPE_CHOICES)
    content=models.TextField(verbose_name='본문')
    create_date=models.DateTimeField(verbose_name='생성날짜', auto_now_add=True)
    modify_date=models.DateTimeField(verbose_name='수정날짜', auto_now=True)


    class Meta:
        verbose_name='post'
        verbose_name_plural='posts'
        ordering=('-modify_date', )


    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse('blog:post_detail', args=(self.id, ))


    def get_previous_post(self):
        return self.get_previous_by_modify_date()


    def get_next_post(self):
        return self.get_next_by_modify_date()

