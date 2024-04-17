from django.contrib import admin
from django.urls import path, include
from .views import user_login, menu, cerrar_sesion

urlpatterns = [
    path('login/', user_login,name='login'),
    path('menu/',menu,name='menu'),
    path('cerrar_sesion',cerrar_sesion,name='cerrar_sesion')

]
