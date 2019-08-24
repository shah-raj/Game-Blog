from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.main, name='main',),
    url(r'^index/$', views.index, name='index',),
    url(r'^contact/$', views.contact, name='contact', ),
    url(r'^about/$', views.about, name='about', ),
]