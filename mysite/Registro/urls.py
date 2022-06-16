from django.urls import path, include
from . import views
from django.contrib.auth.views import login_required

urlpatterns = [

    # listar las carreras de la bd
    path('listarMascotas', views.listar_mascotas, name="listar_mascotas"),
    
        
    # agregar una carrera    
    path('agregar_mascota', views.agregar_mascota, name="agregar_mascota"),
    
    # editar una carrera
    path('editar_mascota/<int:mascota_id>', login_required(views.editar_mascota), name="editar_mascota"),

    # borrar una carrera
    path('borrar_mascota/<int:mascota_id>', login_required(views.borrar_mascota), name="borrar_mascota"),


    # # editar una carrera
    # path('editar_mascota/<int:mascota_id>', views.editar_mascota ,name="editar_mascota"),

    # # borrar una carrera
    # path('borrar_mascota/<int:mascota_id>', views.borrar_mascota, name="borrar_mascota"),
    
    
    # LLAMAMOS A LOS GENERICS
    # path('add_mascota', views.MascotaCreate.as_view(), name="add_mascota"), 
    # path('list_mascotas/', views.MascotaList.as_view(), name='list_mascotas'),

    # path('edit_mascota/<int:pk>', views.MascotaUpdate.as_view(), name='edit_mascota'),

    # path('del_mascota/<int:pk>', views.MascotaDelete.as_view(), name='del_mascota'),
    
    # llamando a la clases
    
    path('add_mascota', views.MascotaCreate.as_view(), name="add_mascota"),

    path('list_mascotas/', views.MascotaList.as_view(), name='list_mascotas'),

    path('edit_mascota/<int:pk>', views.MascotaUpdate.as_view(), name='edit_mascota'),

    path('del_mascota/<int:pk>', views.MascotaDelete.as_view(), name='del_mascota'),



]

