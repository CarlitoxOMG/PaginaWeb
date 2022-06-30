from django.shortcuts import render, redirect
from django.contrib.auth.mixins import UserPassesTestMixin, AccessMixin, LoginRequiredMixin
from django.contrib.auth.decorators import login_required, user_passes_test
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Docente
from .forms import DocenteForm
#---------------- las importaciones para la API ------------
from rest_framework import generics
from .serializers import DocenteSerializer

# Create your views here.

class DocenteList (ListView):                    
    model = Docente
    template_name = 'Docente/docente_list.html'

class DocenteCreate (CreateView):
    model = Docente
    form_class = DocenteForm
    template_name = 'Docente/docente_form.html'
    success_url = reverse_lazy('docentes_list')

class DocenteUpdate(UpdateView):
    model = Docente
    form_class = DocenteForm
    template_name = 'Docente/docente_form.html'
    success_url = reverse_lazy('docentes_list')

class DocenteDelete(DeleteView):
    model = Docente
    template_name = 'Docente/docente_borrar.html'
    success_url = reverse_lazy('docentes_list')

# ------------------ API REST --------
class API_objects(generics.ListCreateAPIView):
    queryset = Docente.objects.all()
    serializer_class = DocenteSerializer
    
class API_objects_details(generics.RetrieveUpdateDestroyAPIView):
    queryset = Docente.objects.all()
    serializer_class = DocenteSerializer
