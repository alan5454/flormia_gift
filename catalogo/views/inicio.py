from django.shortcuts import render

from catalogo.models import Arreglo, Contacto, Extra, Ramo, TipoFlor


def inicio(request):
    """Página principal. Pasa a index.html exactamente estas variables:
    flores, ramos_clasicos, ramos_temporada, arreglos, extras y contacto
    (contacto puede ser None; la plantilla lo tolera)."""
    ramos = Ramo.objects.filter(activo=True)
    contexto = {
        "flores": TipoFlor.objects.filter(activo=True),
        "ramos_clasicos": ramos.filter(categoria=Ramo.CLASICO),
        "ramos_temporada": ramos.filter(categoria=Ramo.TEMPORADA),
        "arreglos": Arreglo.objects.filter(activo=True),
        "extras": Extra.objects.filter(activo=True),
        "contacto": Contacto.objects.first(),
    }
    return render(request, "catalogo/index.html", contexto)
