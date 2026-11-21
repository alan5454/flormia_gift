from django.db import models


class Ordenable(models.Model):
    """Campos comunes: nombre único, orden de aparición y visibilidad."""
    nombre = models.CharField(max_length=100, unique=True)
    orden = models.PositiveSmallIntegerField(default=0)
    activo = models.BooleanField(default=True)

    class Meta:
        abstract = True
        ordering = ["orden", "nombre"]

    def __str__(self):
        return self.nombre


class ConImagen(Ordenable):
    descripcion = models.CharField(max_length=200, blank=True)
    # Ruta dentro de static/ (ej. "img/ramos/pureza.jpg") o URL completa.
    imagen = models.CharField(max_length=300, blank=True)

    class Meta(Ordenable.Meta):
        abstract = True
