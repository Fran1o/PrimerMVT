from django.urls import path
from familiaresapp.views import *

urlpatterns = [

    path('home/', home),
    path('familia/', crear_familiar),
    path('primos/', crear_primos),
    path('tios/', crear_tios)
]

