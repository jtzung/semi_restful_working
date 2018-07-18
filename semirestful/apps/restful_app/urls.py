from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^$', views.index),
    url(r'^new$', views.new),
    url(r'^users/create$', views.create),
    url(r'^users/(?P<user_id>\d+)$', views.show),
    url(r'^destroy/(?P<user_id>\d+)$', views.destroy),
    url(r'^users/(?P<user_id>\d+)/edit$', views.edit),
    url(r'^update/(?P<user_id>\d+)$', views.update)
]   