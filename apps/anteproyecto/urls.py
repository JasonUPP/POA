from django.urls import path, include
from . import views

urlpatterns = [
        path('', views.inicio, name='AnteProyecto'),
        path('crearap/', views.crearap, name='CrearAp'),
        path('insertarap/', views.insertarap, name='InsertarAp'),
        path('fd/', views.fd, name='fd'),
]
