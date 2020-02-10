from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^', views.ex03, name='ex03'),
]