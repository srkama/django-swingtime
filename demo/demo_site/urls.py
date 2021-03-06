import os
from django.conf import settings
from django.contrib import admin
from django.views.static import serve
from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView, RedirectView

admin.autodiscover()
site_dir = os.path.dirname(settings.PROJECT_DIR)
doc_root = os.path.join(os.path.dirname(site_dir), 'docs/build/html')

urlpatterns = patterns('',
    url(r'^$',               TemplateView.as_view(template_name='intro.html'), name='demo-home'),
    (r'^karate/',            include('karate.urls')),
    (r'^admin/docs/',        include('django.contrib.admindocs.urls')),
    (r'^admin/',             include(admin.site.urls)),
    (r'^docs/?$',            RedirectView.as_view(url='/docs/index.html')),
    (r'^docs/(?P<path>.*)$', serve, dict(document_root=doc_root, show_indexes=False))
)

if settings.DEBUG:
    data = dict(document_root=settings.MEDIA_ROOT, show_indexes=True)
    urlpatterns += patterns ('',
        (r'^media/(?P<path>.*)$', serve, data),
    )
