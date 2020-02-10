from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^', views.ex02, name='ex02'),
]