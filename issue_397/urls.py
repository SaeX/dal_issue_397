# -*- encoding: utf-8 -*-

from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns('',
    url(r'^book_create/$', views.CreateBookView.as_view(), name='book_create'),
)