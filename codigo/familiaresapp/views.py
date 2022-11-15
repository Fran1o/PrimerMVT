from django.shortcuts import render
from familiaresapp.models import Familia, Primos, Tios
from familiaresapp.forms import FamiliaFormulario, PrimosFormulario, TiosFormulario

# Create your views here.

def home(request):

    return render(request, "familiaresapp/index.html")


def crear_familiar(request):

    if request.method == "POST":

        formulario = FamiliaFormulario(request.POST)

        if formulario.is_valid():

            data = formulario.cleaned_data

            familiar = Familia(nombre=data["nombre"], fecha_nacimiento=data["fecha_nacimiento"], edad=data["edad"])
            familiar.save()

    formulario = FamiliaFormulario()

    return render(request, "familiaresapp/familiar_form.html", {"formulario": formulario})


def crear_primos(request):

    if request.method == "POST":

        formulario = PrimosFormulario(request.POST)

        if formulario.is_valid():

            data = formulario.cleaned_data

            primos = Primos(nombre=data["nombre"], fecha_nacimiento=data["fecha_nacimiento"], edad=data["edad"])
            primos.save()

    formulario = PrimosFormulario()

    return render(request, "familiaresapp/primos_form.html", {"formulario": formulario})


def crear_tios(request):

    if request.method == "POST":

        formulario = TiosFormulario(request.POST)

        if formulario.is_valid():

            data = formulario.cleaned_data

            tios = Tios(nombre=data["nombre"], fecha_nacimiento=data["fecha_nacimiento"], edad=data["edad"])
            tios.save()

    formulario = TiosFormulario()

    return render(request, "familiaresapp/tios_form.html", {"formulario": formulario})




     