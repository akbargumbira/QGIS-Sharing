"""django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.views import login, logout

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    # Authentication
    url(r'^accounts/login/$', login, {}, name='user_login'),
    url(r'^accounts/logout/$', logout, {}, name='user_logout'),

    url(r'^', include('symbols.urls', namespace='symbols')),
    # Symbols
    url(r'^symbols/', include('symbols.urls', namespace='symbols')),
    # Styles
    url(r'^styles/', include('styles.urls', namespace='styles')),
]
