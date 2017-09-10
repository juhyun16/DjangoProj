from django.conf.urls import url, include
from django.contrib import admin
from .views import HomeView
from chat.views import index


urlpatterns = [
    url(r'^admin/', admin.site.urls),

    #url(r'^$', HomeView.as_view(), name="home"),

    #       회원가입 앱
    url(r'^accounts/', include('accounts.urls')),

    #       친구추가 앱
    url(r'^friend/', include('friend.urls', namespace='friend')),

    #       채팅 테스트 url  ->  추후 삭제
    url(r'^$', index),

    #       본격 채팅 앱
    url(r'^chat/', include('chat.urls', namespace='chat')),

]
