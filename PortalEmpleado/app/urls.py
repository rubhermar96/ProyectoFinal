from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio_portal, name='inicio_portal'),
    path('/login/', views.login_usuario, name='login_usuario'),
    path('/registro/', views.registro_usuario, name='registro_usuario')
]