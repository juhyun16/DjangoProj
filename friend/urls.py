from django.conf.urls import url
from . import views

urlpatterns=[
    #       ID로 친구(user)를 검색한다.
    url(r'^search/', views.search, name='search'),

    #       나의 친구 목록을 보여준다.
    url(r'^list/$', views.myList, name='list'),

    #       선택된 친구 한 명을 내 친구로 추가한다.
    url(r'^add/$', views.add, name='add')
]