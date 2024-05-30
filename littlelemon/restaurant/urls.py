from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('hello', views.sayHello, name='sayHello'),
    path('menu', views.MenuItemView.as_view(), name ='menuItemView'),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view(), name='singleMenuItemView'),
]