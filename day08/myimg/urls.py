from django.urls import path, include
from myimg.views import LoadImage


urlpatterns = [
    path('', LoadImage.as_view(), name='home'),
]