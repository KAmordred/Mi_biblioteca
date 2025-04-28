from django.urls import path
from . import views  # Importa las vistas desde el archivo views.py

urlpatterns = [
    path('agregar_libro/', views.agregar_libro, name='agregar_libro'),
]
