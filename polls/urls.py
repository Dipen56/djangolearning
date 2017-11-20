from django.conf.urls import url
#this will import everything from the view
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]