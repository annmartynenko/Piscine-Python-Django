from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'populate/', views.insert_data, name='insert_data'),
    url(r'display/', views.display, name='display'),
]