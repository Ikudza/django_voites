from django.conf.urls import include, url, patterns
from django.conf import settings
from django.contrib import admin
from clients import views
admin.autodiscover()

urlpatterns = [
    url(r'^$', views.index),
    url(r'^voite', views.view_photo),
    url(r'^report', views.return_clients_xlsx),
    url(r'^admin/', include(admin.site.urls)),
]

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
         'document_root': settings.MEDIA_ROOT}))
