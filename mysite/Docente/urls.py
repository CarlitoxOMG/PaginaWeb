from django.urls import path
# from django.conf.urls import url
from django.urls import include, re_path
from django.conf import settings
from django.conf.urls.static import static
from .views import DocenteList, DocenteCreate, DocenteUpdate , DocenteDelete
from rest_framework.urlpatterns import format_suffix_patterns
from .views import API_objects, API_objects_details

urlpatterns = [
    path('api/', API_objects.as_view()),
    path('api/<int:pk>/', API_objects_details.as_view()),
]

urlpatterns += [
    re_path('listar/', DocenteList.as_view(), name="docente_list"),

    re_path('crear/', DocenteCreate.as_view(), name="docente_form"),
    re_path('editar/<int:pk>', DocenteUpdate.as_view(), name="docente_update"),
    re_path('borrar/<int:pk>', DocenteDelete.as_view(), name="docente_borrar"),
    
]
