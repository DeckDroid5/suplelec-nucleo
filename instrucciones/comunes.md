# Instrucciones comunes de Suplelec

Valen para todos los proyectos de Suplelec en Claude Code. Cada proyecto las importa desde su `CLAUDE.md` y agrega solo lo suyo. En marca, contenido y datos técnicos mandan estas.

Suplelec S.A. importa cables de señal en Costa Rica (incendio, robo y control de acceso, aire acondicionado, BACnet RS485 y audio), de Genesis y Southwire. No vende en línea: todo termina en "Solicitar cotización" (formulario, WhatsApp o correo). La empresa, sus clientes y su voz: `nucleo/marca/perfil.md`.

## Proyectos y dónde se abre Claude

| Carpeta | Qué es | Se abre Claude aquí para… |
| --- | --- | --- |
| `~/suplelec` | Sitio web (WordPress) | El sitio: páginas, catálogo, guías, SEO técnico, hosting |
| `~/suplelec-marketing` | Marketing, publicidad y redes | Contenido para redes, anuncios, informes, presencia en línea |
| `~/suplelec-nucleo` | Este conocimiento compartido | Solo mantenimiento. Lo normal es editarlo desde el proyecto donde surge el cambio, por su enlace `nucleo/` |

Los tres repositorios van uno al lado del otro. Cada proyecto tiene el enlace `nucleo -> ../suplelec-nucleo`, así que los dos ven al instante lo mismo. El ERP interno de Suplelec es otro proyecto y no se toca desde aquí.

## Núcleo, progreso y memoria

- **Progreso:** cada proyecto tiene su `docs/progreso.md`, con "Para retomar" (estado y primeros pasos) e historial. Se actualiza al terminar cada tarea: es la memoria del proyecto.
- **Pedidos entre proyectos:** `nucleo/solicitudes.md`. Al empezar, el hook muestra los abiertos para el proyecto. Al cumplir uno, se pasa a "Hechas" con la fecha.
- **Cambios del núcleo:** se anotan arriba en `nucleo/CAMBIOS.md` (fecha, proyecto, qué y por qué) y se hace commit **en el repositorio del núcleo**, no en el del proyecto. Las reglas y los datos técnicos solo cambian con la aprobación del usuario; los datos técnicos, además, con la del técnico.
- **Memoria automática de Claude:** es de cada carpeta y de esta computadora; el otro proyecto no la ve. Lo que vale para toda la empresa (una regla, una preferencia del usuario sobre la marca o el contenido) se escribe aquí, no en esa memoria.
- **Revisión de reglas:** `nucleo/reglas/revisar.py` revisa el texto público contra `nucleo/reglas/reglas.toml`. Corre solo cuando se escribe contenido (hook) y se puede correr a mano: `python3 nucleo/reglas/revisar.py <archivos>`.

## Principios del usuario

- **Limpio y portable.** Todo se reproduce con Git, Docker y los scripts de cada repositorio; no se instala nada en el sistema si se puede evitar.
- **Después de cada fase creativa, una fase de limpieza:** compactar documentos, borrar lo que ya no sirve (archivos, artifacts, código muerto), ordenar datos y revisar herramientas, skills, plugins y MCP.
- **Plugins y conectores de claude.ai:** `data`, `productivity` y `marketing-skills` están desactivados. Si una tarea necesita uno que no está activo (o un MCP sin autenticar), se le avisa al usuario para que lo active; no se rodea.
- **Nada sale ni se gasta sin el usuario:** publicar, enviar mensajes, cambiar anuncios o presupuestos y tocar producción o Cloudflare requieren su confirmación en esa sesión.

## Idioma

- Documentos y comunicación con el equipo: español.
- Textos públicos: español de Costa Rica, **trato de usted**, frases cortas y técnicas.
- Código: nombres en inglés o según la convención de la herramienta; comentarios en español.

## Reglas que no se rompen

**Precisión técnica**

- Todo dato técnico sale de una ficha técnica del fabricante (`privado/fichas/` del sitio) y queda anotado en `privado/fichas/fuentes.csv`. La ficha manda sobre la web, porque respalda ante un reclamo; la web solo complementa y se dice cuando es la única fuente.
- Lo aprobado por el técnico está en `nucleo/tecnico/usos-cables.md` (afirmaciones U1, U2…). Una afirmación nueva pasa por el técnico. Si falta el dato: `[VALIDAR CON TÉCNICO]`, y no se publica.
- Nada técnico se publica sin la aprobación del técnico confirmada por el usuario. En público: "Revisado por el equipo técnico de Suplelec", sin nombres.
- **Revisión del técnico:** como página web legible en el teléfono (artifact privado), **nunca en PDF**; una tarjeta por familia con la fuente de cada dato. Cuando aprueba todo y las respuestas ya están en `usos-cables.md`, se borran la hoja y su artifact.
- **Normas:** se cita la edición más reciente (hoy NEC 2026) y se dice cuál está oficializada en Costa Rica (NEC 2020).
- **"Resistente a la luz solar" no quiere decir para exteriores.** Para tramos al sol se usa un cable para exteriores (FPL para exterior y enterrado, audio para enterrado directo). El dato puede ir en una tabla, nunca como ventaja.
- **No se explica cómo se acepta un certificador extranjero** (ECA ni requisitos de acreditación): ayuda a la competencia a importar equivalentes. En certificación: qué significa el listado, que UL y ETL prueban con las mismas normas y que el profesional responsable verifica el material ante el CFIA.

**Nada de códigos ni fichas en público**

- Ni números de parte, ni PDF, ni enlaces a fichas, ni códigos en fotos, nombres de archivo o metadatos. `privado/` nunca se versiona ni se sube.
- La ficha se le envía **en privado** al ingeniero que la necesita (por ejemplo, para homologar). No se promete una comparación escrita dato por dato.

**Contenido**

- Sin precios (si alguna vez hay uno, con IVA incluido; nunca "+ IVA"). Sin "stock garantizado": "entrega inmediata del stock disponible".
- Sin clientes: solo los proyectos autorizados de `nucleo/marca/perfil.md` §7. Sin competidores.
- No se mencionan el crédito, el método de entrega, la fecha de fundación ni si el cable viene en caja o carrete (solo el largo por rollo: 305 m o 152 m).
- Sin festividades ni fechas especiales, sin emojis en títulos, sin frases de relleno ("en el mundo actual", "descubra", "sin duda"), sin nada que se vea genérico o hecho por IA.
- Sin rostros del equipo ni la bodega en fotos y videos de la marca. (Los asesores sí pueden publicar en LinkedIn desde su perfil personal, con su foto.)

**Marcas**

- Solo Genesis y Southwire, cada una por su lado: no se dice que Genesis es de Southwire. Nunca Belden, Windy City ni el cable de red.
- UL y ETL solo junto al producto certificado. "Hecho en EE. UU." solo en la familia que tiene el sello en su ficha.

**Imágenes**

- Desde el 4 de octubre de 2026, Claude genera las imágenes con fal.ai (fotos y video, MCP `fal-ai`, pago por uso: consultar el precio antes de generar) y las compone con Canva (diseños con la marca). Las revisa con rigor y el usuario elige; nada se publica sin su elección.
- No se bajan ni se componen imágenes de internet ni de los sitios de los fabricantes por iniciativa propia. Las fotos de marca de Genesis y Southwire las entrega el usuario.
- Lo que muestra un producto concreto sale de las ilustraciones 3D propias (exactas), no de la IA.
- Estilo, paleta y revisión: `nucleo/marca/identidad.md`.
