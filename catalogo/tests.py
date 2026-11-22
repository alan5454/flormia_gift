from django.test import TestCase
from django.urls import reverse

from catalogo.models import Arreglo, Contacto, Extra, Ramo, TipoFlor


class InicioTests(TestCase):
    def get(self):
        return self.client.get(reverse("catalogo:inicio"), secure=True)

    def test_base_de_datos_vacia(self):
        r = self.get()
        self.assertEqual(r.status_code, 200)
        self.assertContains(r, "Convierte un día ordinario")

    def test_registros_con_campos_vacios(self):
        TipoFlor.objects.create(nombre="Rosas")
        Ramo.objects.create(nombre="Ramo A", precio=450)
        Ramo.objects.create(nombre="Ramo B", precio=680, categoria=Ramo.TEMPORADA,
                            imagen="img/no-existe.jpg")
        Arreglo.objects.create(nombre="Caja", precio=650, imagen="https://x.test/f.jpg")
        Extra.objects.create(nombre="Globo", precio=90)
        Contacto.objects.create()
        r = self.get()
        self.assertEqual(r.status_code, 200)
        for texto in ("Rosas", "Ramo A", "$450", "Ramo B", "Caja", 'data-precio="90.00"'):
            self.assertContains(r, texto)
