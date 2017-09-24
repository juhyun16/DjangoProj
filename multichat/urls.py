from django.conf.urls import url, include
from django.contrib import admin
from .views import HomeView
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    url(r'^admin/', admin.site.urls),

    #       root url '/'에 대한 처리.
    url(r'^$', HomeView.as_view(), name="home"),

    #       회원가입 앱
    url(r'^accounts/', include('accounts.urls')),

    #       친구추가 앱
    url(r'^friend/', include('friend.urls', namespace='friend')),

    #       본격 채팅 앱
    url(r'^chat/', include('chat.urls', namespace='chat')),

    #       게시판 글 쓰기 앱
    url(r'^blog/', include('blog.urls', namespace='blog')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

