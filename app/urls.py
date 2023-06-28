from django.urls import path 
from . import views 

urlpatterns =[
    path('', views.index, name='index'),
    path('catalogo', views.catalogo, name='catalogo'),
    path('valorant',views.valorant, name='valorant'), 
    path('registro', views.registro, name ="registro"),
    path('agregar', views.ProductoCreate.as_view(), name ="agregar"),
    path('listarproducto', views.ProductoList.as_view(), name='listarproducto'),
    path('editar/<int:pk>', views.ProductoUpdate.as_view(), name='editarP'),
    path('borrar/<int:pk>', views.ProductoDelete.as_view(), name='borrarP'),
    path('nosotros', views.nosotros, name= 'nosotros'),
    path('rickandmorty', views.rickandmorty, name= 'rickandmorty'),
    path('pruebaCarrito',views.cargarCarrito, name= 'pruebaCarrito'),


 
]