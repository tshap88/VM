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
  #  url(r'^elfinder/', include('VM.connector.urls')),
    url(r'^$', views.index, name = 'index'),
    url(r'^support/$', views.support, name = 'support'),
    url(r'^about_us/$', views.about, name = 'about'),
    url(r'^blog/$', views.blog, name = 'blog'),
    url(r'^contact/$', views.contact, name = 'contact'),
    url(r'^news/', include('news.urls', namespace = 'news')),

)

from django.conf import settings
if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT}),
    )