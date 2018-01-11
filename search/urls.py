from django.conf.urls import url
from . import views

urlpatterns = [

	#/search/
    url(r'^$', views.search,name = 'search'),

    #/search/bar/
    url(r'^bar/', views.bar,name = 'bar'),

    #/search/wordCloud/
    url(r'^wordCloud/', views.wordCloud,name = 'wordCloud'),

    ]