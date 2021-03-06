"""ShopStory URL Configuration

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
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url, patterns
from django.contrib import admin

urlpatterns = patterns('',
      ('^$', 'portal.views.homepage'),
      ('^home/$', 'portal.views.homepage'),
      ('^register/$','portal.views.register'), 
      ('^login/$', 'portal.views.user_login'),
      ('^navbar/$', 'portal.views.navbar'),
      ('^mystories/$', 'portal.views.mystories'),
      ('^friends/$', 'portal.views.friends'),
      ('^feed/$', 'portal.views.feed'),
      ('^AddStory/$', 'portal.views.AddStory'),    
      ('^AddProduct/$', 'portal.views.AddStory'),
)
