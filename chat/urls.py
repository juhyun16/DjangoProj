from django.conf.urls import url
from . import views
urlpatterns = [
    #       login한 유저의 프로필을 보여준다.
    url(r'^roomlist/$', views.showroomList, name='list'),

]