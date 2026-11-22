# Catálogo floral — Django + SQLite (dev) → PostgreSQL (prod)

catalogo_floral/
├── manage.py · requirements.txt
├── config/                  # settings.py, urls.py, wsgi.py
├── catalogo/
│   ├── models/              # tipo_flor.py, ramo.py, arreglo.py, extra.py, contacto.py
│   ├── views/               # inicio.py (arma el contexto de la página)
│   ├── admin.py             # la florista edita precios y fotos
│   ├── management/commands/ # cargar_datos.py (datos de ejemplo)
│   └── templates/catalogo/  # base.html, index.html, partials/ (1 por sección)
├── static/{css,js,img/{flores,ramos,arreglos,extras}}
└── docs/

Modelos: TipoFlor, Ramo(categoria: clasico|temporada), Arreglo, Extra, Contacto (1 fila).
Todos con nombre, descripcion, precio, imagen, orden y activo.
Etapas: 1 diseño base · 2 Django+modelos+admin · 3 JS total=arreglo+extras · 4 contacto, fotos, despliegue.
