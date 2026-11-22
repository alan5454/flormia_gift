"""Comprueba que cada {% include %}, {% extends %} y {% static %} apunte a un
archivo que existe (con mayúsculas/minúsculas exactas en Linux)."""
import re
from pathlib import Path

from django.apps import apps
from django.contrib.staticfiles import finders
from django.core.management.base import BaseCommand, CommandError
from django.template import TemplateDoesNotExist, TemplateSyntaxError
from django.template.loader import get_template

PATRON = re.compile(r"""\{%\s*(include|extends|static)\s+(['"])(.+?)\2""")


class Command(BaseCommand):
    help = "Verifica plantillas y archivos estáticos referenciados."

    def handle(self, *args, **options):
        raiz = Path(apps.get_app_config("catalogo").path) / "templates"
        errores, revisadas = [], 0
        for archivo in sorted(raiz.rglob("*.html")):
            nombre = archivo.relative_to(raiz).as_posix()
            try:
                get_template(nombre)
            except (TemplateDoesNotExist, TemplateSyntaxError) as e:
                errores.append(f"{nombre}: {e}")
                continue
            for tag, _, ref in PATRON.findall(archivo.read_text(encoding="utf-8")):
                if tag == "static":
                    ok = finders.find(ref) is not None
                else:
                    try:
                        get_template(ref)
                        ok = True
                    except TemplateDoesNotExist:
                        ok = False
                if not ok:
                    errores.append(f"{nombre}: {tag} '{ref}' no existe")
            revisadas += 1
        if errores:
            raise CommandError("\n" + "\n".join(errores))
        self.stdout.write(self.style.SUCCESS(f"OK: {revisadas} plantilla(s) revisada(s)."))
