from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^create/$', views.create, name='new_room'),
    url(r'^roomlist/$', views.showroomList, name='list'),
    url(r'^enter/$', views.enter, name='enter'),

]