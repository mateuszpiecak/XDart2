from django.shortcuts import render
from .models import Zdjecie
# Create your views here.

def lista_wyswietlania(request):
    queryset = Zdjecie.objects.all()
    context = {
        "zdjecia": queryset
    }
    return render(request, "zdjecie.html", context)
