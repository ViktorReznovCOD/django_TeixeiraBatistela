from django.urls import path

from . import views

urlpatterns  = [
    path('',  views.home, name='home'),#pagina principal
    
    path('<int:noticia_id>/', views.view, name='visualizacao'),
    path('novousuario', views.novousuario, name='novousuario'),
    path('sobrenos', views.sobrenos, name='sobrenos'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('equipamentos',views.equipamentos, name='equipamentos'),
    path('endereço',views.endereço, name='endereço'),
    path('logout',views.logout, name='logout')
    ]