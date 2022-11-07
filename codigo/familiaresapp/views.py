from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template,Context
from familiaresapp.models import Familia

# Create your views here.

def lista_familiares(request):

    familiares = Familia.objects.all()

    archivo = open(r"C:\Users\Admin\Desktop\primermvt\codigo\familiaresapp\templates\inicio.html")

    plantilla = Template(archivo.read())

    archivo.close()

    datos = {"datos_familiares": familiares}

    contexto = Context(datos)

    documento = plantilla.render(contexto)
    
    return HttpResponse(documento)
