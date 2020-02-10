from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'init/', views.create_table, name='create_table'),
    url(r'populate/', views.insert_data, name='insert_data'),
    url(r'display/', views.display, name='display'),
    url(r'remove/', views.remove, name='remove'),
]