from .base import ConImagen


class TipoFlor(ConImagen):
    class Meta(ConImagen.Meta):
        verbose_name = "tipo de flor"
        verbose_name_plural = "tipos de flores"
