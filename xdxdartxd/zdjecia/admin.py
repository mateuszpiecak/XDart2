from django.contrib import admin
from .models import Zdjecie
# Register your models here.

class ZdjecieAdmin(admin.ModelAdmin):
    lista_wyswietlania = ["tytul", "data"]

    class Meta:
        model = Zdjecie

admin.site.register(Zdjecie, ZdjecieAdmin)