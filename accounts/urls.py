from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from .forms import LoginForm

urlpatterns = [
    #       login한 유저의 프로필을 보여준다.
    url(r'^profile/$', views.profile, name="profile"),

    #       회원가입하는 주소
    url(r'^signup/$', views.signup, name="signup"),

    #       로그인하는 주소
    url(r'^login/$', auth_views.login, name="login",
        kwargs={
            "authentication_form":LoginForm,
            "template_name":"accounts/login_form.html"
        }
    ),

    url(r'^logout/$', auth_views.logout, name="logout",
        kwargs={
            "next_page":settings.LOGIN_URL
        }
    ),

]