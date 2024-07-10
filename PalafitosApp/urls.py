from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('registrarCliente/', views.registrarCliente, name='registrarCliente'),
    path('inicio/', views.inicio, name='inicio'),
    path('viajar/', views.viajar, name="viajar"),
    path('galeria', views.galeria, name="galeria"),
    path('RegistrarDonacion/', views.RegistrarDonacion, name="RegistrarDonacion"),
    path('donaciones', views.donaciones, name="donaciones"),
    path('cuidadosRiesgos', views.cuidadosRiesgos, name="cuidadosRiesgos"),
] 