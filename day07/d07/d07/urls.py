"""d07 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from my_app.views import Home, LoginPage, Articles, Publications, Detail, Logout, Favourites

urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/', Articles.as_view(), name='articles'),
    path('login/', LoginPage.as_view(), name='login'),
    path('', Home.as_view(), name='home'),
    path('publications/', Publications.as_view(), name='publications'),
    path('article/<int:pk>/', Detail.as_view(), name='article-detail'),
    path('favourites/', Favourites.as_view(), name='favourites'),
    path('logout/', Logout.as_view(), name='logout'),
]
