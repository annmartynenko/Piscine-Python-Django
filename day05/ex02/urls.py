from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'init/', views.create_sql, name='create_sql'),
    url(r'populate/', views.insert_data, name='insert_data'),
    url(r'display/', views.display, name='display'),
]