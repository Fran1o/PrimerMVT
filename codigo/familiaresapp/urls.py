from django.urls import path
from familiaresapp.views import *

urlpatterns = [

    path('home/', home),
    path('familia/', crear_familiar),
    path('buscarfamiliares/', buscar_familiares),

    path('primos/', crear_primos),
    path('buscarprimos/', buscar_primos),

    path('tios/', crear_tios),
    path('buscartios/', buscar_tios)
    
]

