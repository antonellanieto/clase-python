from django.shortcuts import render
from django.http import HttpResponse
from .models import Familiares


def pagina_principal(request):
    familiar = Familiares(nombre='Maria Cecilia', apellido='Casola', nacimiento='1969-01-12',relacion='Madre')


 

    return render(request, 'index.html', {'nombre': 'María Cecilia', 'apellido': 'Casola', 'nacimiento': '1969-01-12', 'relacion': 'Madre'})