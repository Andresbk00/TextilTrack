from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_inventario, name='inventario_lista'),
]
