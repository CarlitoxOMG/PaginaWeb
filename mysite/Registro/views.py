from django.shortcuts import render, redirect
from .models import Mascota
from .forms import MascotaForm
# las clases genericas
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
# esta libreria nos permitira redireccionamiento
from django.urls import reverse_lazy



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