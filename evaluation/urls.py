from django.conf.urls import url
from . import views

urlpatterns = [

	#/evaluation/
    url(r'^$', views.eval,name = 'eval'),

 ]