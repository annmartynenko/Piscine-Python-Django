from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'init/', views.create_sql, name='create_sql'),
]