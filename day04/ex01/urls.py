from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^django/', views.dg, name='dg'),
    url(r'^affichage/', views.aff, name='aff'),
    url(r'^templates/', views.temp, name='temp'),
]