from django.db import models
from .base import ConImagen


class Arreglo(ConImagen):
    precio = models.DecimalField(max_digits=8, decimal_places=2)
