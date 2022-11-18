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

            familiares = Familia(nombre=data["nombre"],fechanacimiento=data["fechanacimiento"],edad=data["edad"])
            familiares.save()

        return render(request, "familiaresapp/index.html")
        
    else:

        formulario = FamiliaFormulario()

    return render(request, "familiaresapp/familiar_form.html", {"formulario": formulario})


def crear_primos(request):

    if request.method == "POST":

        formulario = PrimosFormulario(request.POST)

        if formulario.is_valid():

            data = formulario.cleaned_data

            primos = Primos(nombre=data["nombre"],fechanacimiento=data["fechanacimiento"],edad=data["edad"])
            primos.save()

        return render(request, "familiaresapp/index.html")
        
    else:

        formulario = PrimosFormulario()

    return render(request, "familiaresapp/primos_form.html", {"formulario": formulario})

    


def crear_tios(request):

    if request.method == "POST":

        formulario = TiosFormulario(request.POST)

        if formulario.is_valid():

            data = formulario.cleaned_data

            tios = Tios(nombre=data["nombre"],fechanacimiento=data["fechanacimiento"],edad=data["edad"])
            tios.save()

        return render(request, "familiaresapp/index.html")
        
    else:

        formulario = TiosFormulario()

    return render(request, "familiaresapp/tios_form.html", {"formulario": formulario})


#BUSQUEDA


def buscar_familiares(request):

    if request.GET:

        nombre_familiar = request.GET.get("nombre_familiar", "")

        if nombre_familiar == "":

            familiares = []

        else:

            familiares = Familia.objects.filter(nombre__icontains=nombre_familiar)

        return render(request, "familiaresapp/buscarfamiliares.html", {"familiares": familiares})

    return render(request, "familiaresapp/buscarfamiliares.html", {"familiares": [] })


def buscar_primos(request):

    if request.GET:

        nombre_primo = request.GET.get("nombre_primo", "")

        if nombre_primo == "":

            primos = []

        else:

            primos = Primos.objects.filter(nombre__icontains=nombre_primo)

        return render(request, "familiaresapp/buscarprimos.html", {"primos": primos})

    return render(request, "familiaresapp/buscarprimos.html", {"primos": [] })


def buscar_tios(request):

    if request.GET:

        nombre_tios = request.GET.get("nombre_tios", "")

        if nombre_tios == "":

            tios = []

        else:

            tios = Tios.objects.filter(nombre__icontains=nombre_tios)

        return render(request, "familiaresapp/buscartios.html", {"tios": tios})

    return render(request, "familiaresapp/buscartios.html", {"tios": [] })



     