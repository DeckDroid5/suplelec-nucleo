# Núcleo de Suplelec

Este repositorio no es un proyecto de trabajo: guarda el conocimiento que comparten el sitio (`~/suplelec`) y el marketing (`~/suplelec-marketing`). Lo normal es editarlo desde ellos, por su enlace `nucleo/`. Si Claude se abre aquí, es para mantenimiento: ordenar, compactar, revisar reglas o resolver solicitudes viejas.

- Qué hay y cómo se usa: `README.md`.
- Aquí, las rutas `nucleo/…` de las instrucciones comunes son rutas de la raíz de este repositorio.
- Cada cambio va arriba en `CAMBIOS.md`, con commit en este repositorio.
- Antes de cambiar `reglas/reglas.toml`, probarlo contra los textos aprobados del sitio, sin falsos positivos: `python3 reglas/revisar.py $(find ../suplelec/contenido -name '*.html' -o -name '*.md')`.

@instrucciones/comunes.md
