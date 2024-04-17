from django.contrib import admin
from django.urls import path, include
from .views import menu_data, cargar_horas_extras,cargar_provisiones, visualizar_provisiones,visualizar_horas_extras,visualizar_horas_compensadas,visualizar_disponibilidad,visualizar

urlpatterns = [
    path('menu_data/', menu_data,name='menu_data'),
    path('cargar_horas_extras',cargar_horas_extras,name='cargar_horas_extras'),
    path('visualizar_provisiones',visualizar_provisiones,name='visualizar_provisiones'),
    path('visualizar_horas_extras',visualizar_horas_extras,name='visualizar_horas_extras'),
    path('cargar_provisiones',cargar_provisiones,name='cargar_provisiones'),
    path('visualizar_horas_compensadas',visualizar_horas_compensadas,name='visualizar_horas_compensadas'),
    path('visualizar_disponibilidad',visualizar_disponibilidad,name='visualizar_disponibilidad'),
    path('visualizar', visualizar, name='visualizar')
]