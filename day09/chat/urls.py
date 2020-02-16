from django.urls import path
from chat.views import LoginPage, ChatList, Logout
from . import views

urlpatterns = [
    path('list/', ChatList.as_view(), name='list'),
    path('login/', LoginPage.as_view(), name='login'),
    path('', views.index, name='index'),
    path('<str:room_name>/', views.room, name='room-detail'),
    path('logout/', Logout.as_view(), name='logout'),
]