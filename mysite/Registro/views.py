from django.shortcuts import render, redirect
from .models import Mascota
from .forms import MascotaForm
# las clases genericas
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
# esta libreria nos permitira redireccionamiento
from django.urls import reverse_lazy
#------------- importacines API ---------------------
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import MascotaSerializer
from django.shortcuts import render, redirect, get_object_or_404
from rest_framework import status

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 



def listar_mascotas(request):
    mascotas = Mascota.objects.all()
    return render(request, "Registro/listar_mascotas.html", {'mascotas': mascotas})

def agregar_mascota(request):
    if request.method == "POST":
        form = MascotaForm(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.save()
            return redirect("/agregar_mascota")
    else:
        form = MascotaForm()
        return render(request, "Registro/agregar_mascota.html", {'form': form})

def borrar_mascota(request, mascota_id):
    # Recuperamos la instancia de la carrera y la borramos
    instancia = Mascota.objects.get(id=mascota_id)
    instancia.delete()

    # Después redireccionamos de nuevo a la lista
    return redirect('listar_mascotas')

def editar_mascota(request, mascota_id):
    # Recuperamos la instancia de la carrera
    instancia = Mascota.objects.get(id=mascota_id)

    # Creamos el formulario con los datos de la instancia
    form = MascotaForm(instance=instancia)

    # Comprobamos si se ha enviado el formulario
    if request.method == "POST":
        # Actualizamos el formulario con los datos recibidos
        form = MascotaForm(request.POST, instance=instancia)
        # Si el formulario es válido...
        if form.is_valid():
            # Guardamos el formulario pero sin confirmarlo,
            # así conseguiremos una instancia para manipular antes de grabar
            instancia = form.save(commit=False)
            # Podemos guardar cuando queramos
            instancia.save()

    # Si llegamos al final renderizamos el formulario
    return render(request, "Registro/editar_mascota.html", {'form': form})




# Clases GENERICS

# --Otra forma usando clases Generics -------
class MascotaCreate(CreateView):
    model = Mascota
    form_class = MascotaForm
    template_name = 'Registro/mascota_form.html'
    success_url = reverse_lazy("add_mascota")

class MascotaList(ListView):
    model = Mascota
    template_name = 'Registro/list_mascotas.html'
    # paginate_by = 4

class MascotaUpdate(UpdateView):
    model = Mascota
    form_class = MascotaForm
    template_name = 'Registro/mascota_form.html'
    success_url = reverse_lazy('list_mascotas')

class MascotaDelete(DeleteView):
    model = Mascota
    template_name = 'Registro/mascota_delete.html'
    success_url = reverse_lazy('list_mascotas')
    

# El decorador @api_view verifica que la solicitud HTTP apropiada 
# se pase a la función de vista. En este momento, solo admitimos solicitudes GET
@api_view(['GET', 'POST'])
def mascota_collection(request):
    if request.method == 'GET':
        mascotas = Mascota.objects.all()
        serializer = MascotaSerializer(mascotas, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = MascotaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # Si el proceso de deserialización funciona, devolvemos una respuesta con un código 201 (creado
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # si falla el proceso de deserialización, devolvemos una respuesta 400
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def mascota_element(request, pk):
    mascota= get_object_or_404(Mascota, id=pk)

    if request.method == 'GET':
        serializer = MascotaSerializer(mascota)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        mascota.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    elif request.method == 'PUT': 
        mascota_new = JSONParser().parse(request) 
        serializer = MascotaSerializer(mascota, data=mascota_new) 
        if serializer.is_valid(): 
            serializer.save() 
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
