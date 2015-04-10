from django.conf.urls import include, url
# from django.contrib import admin

urlpatterns = [
    url(r'^autocomplete/', include('autocomplete_light.urls')),
    url(r'^397/', include('issue_397.urls')),

]
