from contextlib import nullcontext
from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.views.generic import ListView

# Create your views here.

def home(request):
    return render(request, 'administracion/home.html')

def contacto(request):
    return render(request, 'administracion/contacto.html')

def correspondencia(request, template_name='administracion/correspondencia.html'):
    if request.GET.get('featured'):
        opcion = request.GET.get('featured')
        correspondencias = Correspondencia.objects.filter(residencia=opcion)
    else:
        correspondencias = Correspondencia.objects.all().order_by('residencia')
    residencias = Residencia.objects.all()
    return render(request, template_name, {'correspondencias': correspondencias, 'residencias': residencias})
