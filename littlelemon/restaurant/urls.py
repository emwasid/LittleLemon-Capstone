from django.contrib import admin
from django.urls import path
from . import views

from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('', views.home, name='home'),
    path('hello', views.sayHello, name='sayHello'),
    path('menu-items', views.MenuItemView.as_view(), name ='menuItemView'),
    path('menu-items/<int:pk>', views.SingleMenuItemView.as_view(), name='singleMenuItemView'),
    path('message', views.msg, name='msg'),
    
    path('api-token-auth', obtain_auth_token), #pass username and password in a post method in insomnia to get token
]