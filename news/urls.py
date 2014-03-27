from django.conf.urls import patterns, url

from news import views

urlpatterns = patterns('',
    url(r'^$', views.NewsAll, name='NewsAll'),
    url(r'^(?P<new_id>.*)/$', views.SingleNews, name='SingleNews'),
#    url(r'^(?P<new_id>.*)/$', views.SingleNews, name='SingleNews'),
    
)
