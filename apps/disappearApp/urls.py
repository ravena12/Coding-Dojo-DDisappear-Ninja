from django.conf.urls import url 
from . import views 

urlpatterns = [
	url(r'^$', views.index),
	url(r'^(\bninjas\b)$', views.showNinjas),
	url(r'(?P<color>\w+)$', views.ninja),
	
]


