from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('registrar/', views.usuario_view, name='registrar'),
    path('listar/', views.usuario_list, name='listar'),
    path('editar/<int:id_usuario>/' , views.usuario_edit, name='editar'),
    path('eliminar/<int:id_usuario>/' , views.usuario_delete, name='eliminar'),
]
