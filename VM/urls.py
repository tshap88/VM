from django.conf.urls import patterns, include, url
import views
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'VM.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
#    url(r'^app/', include('app.urls', namespace='app')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^vm4game.com/$', views.index, name = 'index'),
    url(r'^vm4game.com/support/$', views.support, name = 'support'),
    url(r'^vm4game.com/about_us/$', views.about, name = 'about'),
    url(r'^vm4game.com/blog/$', views.blog, name = 'blog'),
    url(r'^vm4game.com/contact/$', views.contact, name = 'contact'),
    url(r'^vm4game.com/news/$', include('news.urls', namespace = 'news')),

)
