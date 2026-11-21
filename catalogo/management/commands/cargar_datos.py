"""Carga los datos de ejemplo. Se puede ejecutar las veces que quieras:
no duplica registros ni pisa los cambios hechos desde el admin."""
from django.core.management.base import BaseCommand
from django.db import transaction

from catalogo.models import Arreglo, Contacto, Extra, Ramo, TipoFlor

FLORES = [
    ("Rosas", "clásicas y llenas de cariño"),
    ("Tulipanes", "frescos y llenos de alegría"),
    ("Girasoles", "luminosos y optimistas"),
    ("Lirios", "elegantes y serenos"),
    ("Peonías", "románticas y exuberantes"),
    ("Orquídeas", "sofisticadas y delicadas"),
]
RAMOS = [  # nombre, descripción, precio, categoría
    ("Ramo Dulce Amanecer", "", 450, Ramo.CLASICO),
    ("Ramo Pureza", "", 520, Ramo.CLASICO),
    ("Ramo Campo Fresco", "", 380, Ramo.CLASICO),
    ("Ramo Primavera", "tulipanes y peonías", 680, Ramo.TEMPORADA),
    ("Ramo Lavanda y Luz", "flores en tonos lila", 590, Ramo.TEMPORADA),
    ("Ramo Gran Detalle", "24 rosas premium", 890, Ramo.TEMPORADA),
]
ARREGLOS = [
    ("Caja Floral Suave", "arreglo floral en caja", 650),
    ("Florero de Cristal", "flores frescas en florero de cristal", 720),
    ("Centro de Mesa Elegante", "composición floral para mesa", 950),
    ("Orquídea en Maceta", "orquídea delicada en maceta", 480),
]
EXTRAS = [
    ("Tarjeta con mensaje personalizado", "💌", 40),
    ("Globo", "🎈", 90),
    ("Peluche pequeño", "🧸", 150),
    ("Chocolates", "🍫", 120),
    ("Envío a domicilio (desde)", "🚚", 80),
]


class Command(BaseCommand):
    help = "Carga datos de ejemplo sin duplicar (idempotente)."

    @transaction.atomic
    def handle(self, *args, **options):
        nuevos = 0

        def crear(modelo, nombre, **defaults):
            nonlocal nuevos
            _, creado = modelo.objects.get_or_create(nombre=nombre, defaults=defaults)
            nuevos += creado

        for orden, (nombre, desc) in enumerate(FLORES, 1):
            crear(TipoFlor, nombre, descripcion=desc, orden=orden)
        for orden, (nombre, desc, precio, cat) in enumerate(RAMOS, 1):
            crear(Ramo, nombre, descripcion=desc, precio=precio, categoria=cat, orden=orden)
        for orden, (nombre, desc, precio) in enumerate(ARREGLOS, 1):
            crear(Arreglo, nombre, descripcion=desc, precio=precio, orden=orden)
        for orden, (nombre, icono, precio) in enumerate(EXTRAS, 1):
            crear(Extra, nombre, icono=icono, precio=precio, orden=orden)

        _, creado = Contacto.objects.get_or_create(pk=1)
        nuevos += creado

        self.stdout.write(self.style.SUCCESS(f"Listo: {nuevos} registro(s) nuevo(s)."))
