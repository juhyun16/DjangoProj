from django.conf.urls import url, include
from django.contrib import admin
from .views import HomeView
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^$', HomeView.as_view(), name="home"),

    #       회원가입 앱
    url(r'^accounts/', include('accounts.urls')),

    #       친구추가 앱
    url(r'^friend/', include('friend.urls', namespace='friend')),

    #       본격 채팅 앱
    url(r'^chat/', include('chat.urls', namespace='chat')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

