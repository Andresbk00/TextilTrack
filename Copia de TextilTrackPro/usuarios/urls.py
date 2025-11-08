from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('login/', views.web_login, name='login'),
    path('registro/', views.web_register, name='registro'),
    path('logout/', views.logout_view, name='logout'),
    path('panel_admin/', views.panel_admin, name='panel_admin'),
    path('panel_vendedor/', views.panel_vendedor, name='panel_vendedor'),
    path('panel_aux/', views.panel_aux, name='panel_aux'),
    path('aprobar_usuario/<int:user_id>/', views.aprobar_usuario, name='aprobar_usuario'),
    path('eliminar_usuario/<int:user_id>/', views.eliminar_usuario, name='eliminar_usuario'),
]
