from django.shortcuts import render
from django.http import HttpResponse
from .models import Familiares


def pagina_principal(request):
    familiar = Familiares('','María Cecilia', 'Casola', 55, '1966-12-01', 'Madre')
    familiar2 = Familiares('','Martina', 'Nieto', 19, '2022-11-23', 'Hermana')


 

    return render(request, 'index.html', {'objetos': [familiar, familiar2]})