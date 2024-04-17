from django.contrib import admin
from django.urls import path, include
from .views import crear_usuario, editar_usuario, lista_usuario

urlpatterns = [
    path('crear_usuario/', crear_usuario,name='crear_usuario'),
    path('lista_usuario/',lista_usuario,name='lista_usuario'),
    path('editar_usuario/<int:usuario_id>/', editar_usuario, name='editar_usuario'),
]
