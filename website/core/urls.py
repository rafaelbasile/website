from django.conf.urls import include, url

from . import views as core_views

urlpatterns=[
    url(r'^$', core_views.home, name='home'),
]
