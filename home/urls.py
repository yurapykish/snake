from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.main, name='home'),
    url(r'^feedback/$', views.feedback, name='feedback'),
]
