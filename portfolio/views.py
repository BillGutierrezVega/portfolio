from django.shortcuts import render
from .models import Project

# Create your views here.
def home(request):
    # Obtiene todos los objetos de la tabla Project
    projects = Project.objects.all()

    # Pasa los objetos de Project como contexto al render
    return render(request, 'home.html', {'projects': projects})