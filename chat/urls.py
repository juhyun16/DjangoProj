from django.conf.urls import url
from . import views
urlpatterns = [

    url(r'^roomlist/$', views.showroomList, name='list'),

]