# coding=utf-8
from django.http import HttpResponseRedirect
from django.shortcuts import render


def index(request):
    """
    药查查首页
    :param request:
    :return:
    """
    try:

        return render(request, 'website/index.html')
    except Exception, e:
        return HttpResponseRedirect('/')


def product_introduction(request):
    """
    产品介绍
    :param request:
    :return:
    """
    try:
        return render(request, 'website/product_introduction.html')
    except Exception, e:
        return HttpResponseRedirect('/')


def news_information(request):
    """
    新闻资讯
    :param request:
    :return:
    """
    try:
        return render(request, 'website/news.html')
    except Exception, e:
        return HttpResponseRedirect('/')


def about_us(request):
    """
    关于我们
    :param request:
    :return:
    """
    try:

        return render(request, 'website/aboutUs.html')
    except Exception, e:
        return HttpResponseRedirect('/')
