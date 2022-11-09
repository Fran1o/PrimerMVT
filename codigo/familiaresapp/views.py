from django.shortcuts import render
from django.template import Template, Context
from familiaresapp.models import Familia

# Create your views here.

def lista_familiares(request):

    familiares = Familia.objects.all()
    
    return render(request, "inicio.html", {"mis_familiares": familiares})
