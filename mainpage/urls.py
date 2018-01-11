from django.conf.urls import url
from . import views

urlpatterns = [

	#/mainpage/
    url(r'^$', views.index,name = 'main'),

    #/mainpage/contact/
    url(r'^contact/',views.contact, name = 'contact'),

    #/mainpage/search/
    # url(r'^search/', views.search, name = 'search'),
	
	#/mainpage/bar/
	url(r'^bar', views.bar, name = 'bar'),

	#/mainpage/wordCloud/
	url(r'^wordCloud/',views.summary, name = 'summary'),

	#/mainpage/evaluation/
	url(r'^evaluation/',views.evaluation, name = 'evaluation'),
]