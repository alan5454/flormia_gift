from django.db import models
from .base import ConImagen


class Ramo(ConImagen):
    CLASICO, TEMPORADA = "clasico", "temporada"
    CATEGORIAS = [(CLASICO, "Clásico"), (TEMPORADA, "De temporada / especial")]

    categoria = models.CharField(max_length=10, choices=CATEGORIAS, default=CLASICO)
    precio = models.DecimalField(max_digits=8, decimal_places=2)

    class Meta(ConImagen.Meta):
        ordering = ["categoria", "orden", "nombre"]
