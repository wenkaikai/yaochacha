# coding=utf-8
from django.conf.urls import patterns, url
from website.urls.biz_urls import urlpatterns as biz_urlpatterns

urlpatterns = patterns('website.views.views',
    url(r'^$', 'index', name='index'),
    url(r'^index$', 'index', name='index'),
    url(r'^product_introduction$', 'product_introduction', name='product_introduction'),
    url(r'^news_information$', 'news_information', name='news_information'),
    url(r'^about_us$', 'about_us', name='about_us'),

) + biz_urlpatterns
