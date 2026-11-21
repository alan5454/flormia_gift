from django.db import models
from .base import Ordenable


class Extra(Ordenable):
    """Complemento que se suma al precio (tarjeta, globo, peluche...)."""
    icono = models.CharField(max_length=10, blank=True)
    precio = models.DecimalField(max_digits=8, decimal_places=2)
