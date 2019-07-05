from django.conf.urls import url
from scansion import views

urlpatterns =  [
    url(r'^$', views.index, name='index'),
    # url(r'^index/$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),
    url(r'^howto/$', views.how_to, name='how_to'),
    url(r'^analyse/$', views.analyse, name='analyse'),
    url(r'^analyse/howto/$', views.analyse_how_to, name='analyse_how_to'),
    url(r'^analyse/writing/$', views.writing, name='writing'),
    url(r'^analyse/writing/howto/$', views.writing_how_to, name='writing_how_to'),
]
