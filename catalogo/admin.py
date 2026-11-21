from django.contrib import admin
from .models import Arreglo, Contacto, Extra, Ramo, TipoFlor


@admin.register(TipoFlor)
class TipoFlorAdmin(admin.ModelAdmin):
    list_display = ("nombre", "descripcion", "orden", "activo")
    list_editable = ("orden", "activo")


@admin.register(Ramo)
class RamoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "categoria", "precio", "orden", "activo")
    list_editable = ("precio", "orden", "activo")
    list_filter = ("categoria", "activo")


@admin.register(Arreglo)
class ArregloAdmin(admin.ModelAdmin):
    list_display = ("nombre", "precio", "orden", "activo")
    list_editable = ("precio", "orden", "activo")


@admin.register(Extra)
class ExtraAdmin(admin.ModelAdmin):
    list_display = ("icono", "nombre", "precio", "orden", "activo")
    list_editable = ("precio", "orden", "activo")


@admin.register(Contacto)
class ContactoAdmin(admin.ModelAdmin):
    list_display = ("telefono", "whatsapp", "redes", "direccion")
