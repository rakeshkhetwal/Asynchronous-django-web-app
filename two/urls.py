from django.conf.urls import url
#default login setting


from . import views
from django.contrib.auth.views import login

urlpatterns=[
    url(r'^$',views.index),
    url(r'^create/$',views.x),


]