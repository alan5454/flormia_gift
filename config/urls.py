from django.contrib import admin
from django.urls import path

urlpatterns = [
    path("admin/", admin.site.urls),
    # Etapa 2b: path("", include("catalogo.urls")) con la página dinámica
]
