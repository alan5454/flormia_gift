from django.db import models


class Contacto(models.Model):
    """Una sola fila con los datos de la florería."""
    telefono = models.CharField(max_length=40, blank=True)
    whatsapp = models.CharField(max_length=40, blank=True)
    redes = models.CharField("redes sociales", max_length=200, blank=True)
    direccion = models.CharField("dirección", max_length=250, blank=True)

    def __str__(self):
        return "Datos de contacto"
