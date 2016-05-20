"""Sholegram URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from authsystem.views import MyUserCreate, AuthUserCreate, index_page, logout_user, login_user
from content.views import main_page

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',  index_page),
    url(r'^auth$',  AuthUserCreate.as_view(template_name="user_form.html", success_url="/user_signup")),
    url(r'^auth/logout$',  logout_user),
    url(r'^auth/login$',  login_user),
    url(r'^user_signup$',  MyUserCreate.as_view(template_name="user_form.html", success_url="/main")),
    url(r'^main$', main_page),
]
