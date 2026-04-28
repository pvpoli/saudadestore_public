from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('quemsomos/', views.quemsomos, name='quemsomos'),
    path('galeria/', views.galeria, name='galeria'),
    path('alforreca/', views.alforreca, name='alforreca'),
    path('comochegar/', views.comoChegar, name='comoChegar'),
]


