from django.conf.urls import url
from scansion import views

urlpatterns =  [
    url(r'^$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),
    url(r'^analyse/$', views.analyse, name='analyse'),

]
