from django.conf.urls import url
from blog.views import *

urlpatterns = [
    #       example : /
    url(r'^$', PostLV.as_view(), name='index'),

    #       example : /7/
    url(r'^(?P<pk>\d+)/$', PostDV.as_view(), name='post_detail'),

    #       example : /add/
    url(r'^add/$', PostCreateView.as_view(), name='add'),

    #       example : /change/
    url(r'^change/$', PostChangeLV.as_view(), name='change'),

    #       example : /7/update/
    url(r'^(?P<pk>\d+)/update/$', PostUpdateView.as_view(), name='update'),

    #       example : /7/delete/
    url(r'^(?P<pk>\d+)/delete/$', PostDeleteView.as_view(), name='delete'),

]