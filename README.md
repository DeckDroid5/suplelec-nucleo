# Núcleo de Suplelec

Conocimiento compartido de Suplelec S.A. para sus proyectos en Claude Code: la marca, las reglas de contenido, los datos técnicos aprobados por el técnico, lo que se aprende de los clientes y las convenciones de medición. Lo usan el sitio web (`suplelec`) y el marketing (`suplelec-marketing`), para que los dos digan lo mismo.

## Contenido

| Ruta | Qué es |
| --- | --- |
| `instrucciones/comunes.md` | Reglas que valen para todos los proyectos. Cada `CLAUDE.md` las importa |
| `marca/perfil.md` | Empresa, productos, clientes, voz, palabras clave |
| `marca/identidad.md` | Color, tipografía, logos y estilo y revisión de imágenes |
| `tecnico/usos-cables.md` | Banco de afirmaciones técnicas aprobadas por el técnico (U1, U2…) |
| `reglas/reglas.toml` y `reglas/revisar.py` | Lo que no se publica, y el revisor que lo detecta |
| `publico/` | Puntos de entrada del cliente y preguntas reales |
| `medicion/medicion.md` | UTM, código de campaña, eventos y origen de las cotizaciones |
| `skills/suplelec-marca/` | Skill de Claude Code con el resumen de la marca |
| `solicitudes.md` | Pedidos entre proyectos |
| `CAMBIOS.md` | Registro de cambios del núcleo |
| `scripts/al-iniciar.sh` | Lo que cada proyecto muestra al abrir una sesión |

## Cómo lo usa cada proyecto

Los tres repositorios van uno al lado del otro:

```
~/suplelec            sitio web
~/suplelec-marketing  marketing
~/suplelec-nucleo     este repositorio
```

Cada proyecto tiene, versionados:

- el enlace `nucleo -> ../suplelec-nucleo`;
- en su `CLAUDE.md`, la importación `@nucleo/instrucciones/comunes.md`;
- el enlace `.claude/skills/suplelec-marca -> ../../nucleo/skills/suplelec-marca`;
- en `.claude/settings.json`: acceso a `../suplelec-nucleo`, el hook `SessionStart` (`scripts/al-iniciar.sh`) y el hook `PostToolUse` que corre `reglas/revisar.py` cuando Claude escribe contenido.

Como los dos proyectos apuntan a la misma carpeta, un cambio hecho desde uno se ve al instante en el otro.

## Cómo se cambia

1. Se edita desde el proyecto donde surge la necesidad (carpeta `nucleo/`) o abriendo Claude aquí para mantenimiento.
2. Se anota arriba en `CAMBIOS.md`.
3. Commit y push **en este repositorio**.

Las reglas y los datos técnicos solo cambian con la aprobación del usuario; los técnicos, además, con la del técnico.

## Computadora nueva

```bash
cd ~
git clone git@github-suplelec-nucleo:DeckDroid5/suplelec-nucleo.git
git clone git@github-suplelec:DeckDroid5/suplelec.git
git clone git@github-suplelec-marketing:DeckDroid5/suplelec-marketing.git
```

Cada repositorio tiene su propia deploy key de GitHub y su alias en `~/.ssh/config` (`github-suplelec`, `github-suplelec-nucleo`, `github-suplelec-marketing`): GitHub no deja usar la misma deploy key en dos repositorios. Los pasos están en el `README.md` del sitio.

`revisar.py` usa solo Python 3.13 o más nuevo (sin dependencias).
