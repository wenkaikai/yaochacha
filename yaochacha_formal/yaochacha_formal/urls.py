from django.conf.urls import patterns, include, url
from django.contrib import admin
from website.urls import web_urls as website_urls

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'yaochacha_formal.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'', include(website_urls)),
)
