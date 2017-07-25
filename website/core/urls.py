from django.conf.urls import url
from django.contrib import admin


urlpatterns=[
    url(r'^$', core_views.home, name='home'),
]
