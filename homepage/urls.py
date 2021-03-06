from django.conf.urls import url
from . import views

urlpatterns = [
        url(r'^$', views.index, name='index'),
        url(r'^about/introduce/$', views.introduce, name='introduce'),
        url(r'^about/trends/$', views.trends, name='trends'),
        url(r'^about/contactus/$', views.contactus, name='contactus'),
        url(r'^about/declaration/$', views.declaration, name='declaration'),
        url(r'^about/mobile/$', views.mobile, name='mobile'),
        ]

