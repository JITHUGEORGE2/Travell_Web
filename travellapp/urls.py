from django.urls import path
from . import views
app_name = 'travellapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('index.html', views.index, name='index'),
    path('news.html', views.news, name='news'),
    path('elements.html', views.elements, name='elements'),
    path('destinations.html', views.destinations, name='destinations'),
    path('contact.html', views.contract, name='contact'),
    
]
