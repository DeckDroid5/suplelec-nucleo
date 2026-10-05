# Identidad visual de Suplelec

Lo que necesita cualquier pieza de la marca: sitio, redes, anuncios, presentaciones. El detalle de cómo lo aplica el sitio (tokens de `theme.json`, componentes, escala) está en `docs/diseno.md` del sitio. El sistema de diseño original es el artifact "Suplelec" (https://claude.ai/artifact/Tn8zz2cUrbTJ5P8auHPWrB).

## 1. Color

| Nombre | Hex | Uso |
| --- | --- | --- |
| Marino | `#1e284e` | Color principal: texto, títulos, fondos oscuros |
| Naranja | `#ef7521` | Acción ("Solicitar cotización") y acentos. **Nunca como texto sobre fondo claro** |
| Verde | `#06d6a0` | WhatsApp y acentos sobre marino. **Nunca como texto sobre fondo claro** |
| Azul | `#2952a8` | Enlaces y datos informativos |
| Blanco cálido | `#fffcf9` | Fondo principal y texto sobre marino |
| Crema | `#f4f0ea` | Fondos suaves |
| Gris de texto | `#5c5c5c` | Texto secundario sobre claro |

**Contraste (AA, siempre):** marino sobre cualquier fondo claro; marino sobre naranja (4,93:1) o sobre verde (7,58:1); blanco cálido, verde o naranja sobre marino. **Prohibido:** texto blanco sobre naranja (2,90:1), texto naranja o verde sobre claro, texto azul sobre marino.

**Proporción:** 80 % claro, 15 % marino, 5 % acentos. El naranja es para la acción.

## 2. Tipografía

| Fuente | Uso |
| --- | --- |
| Roboto Slab (600 y 700) | Títulos |
| IBM Plex Sans (400 a 600) | Texto |
| JetBrains Mono (400 y 500) | Solo valores técnicos: `16/2`, `FPLR`, `305 m` |

Sin mayúsculas sostenidas ni emojis en títulos. Nada por debajo de 13 px en pantalla.

## 3. Logos

**Juego completo en `marca/logos/`** (SVG y PNG; qué disposición y qué color usar, y tamaños mínimos, en `marca/logos/README.md`): vertical y horizontal con y sin lema, solo el nombre con y sin lema, isotipo, minúsculas y avatares, cada uno a color, inverso (a color sobre marino), blanco, negro y marino. En Canva, carpeta "Suplelec · Logos".

Los que usa el sitio también están publicados (otras herramientas los suben por URL): `https://suplelec.com/wp-content/themes/suplelec/assets/logo/` + `suplelec-horizontal.svg`, `-horizontal-blanco.svg`, `-horizontal-lema.svg`, `-horizontal-lema-blanco.svg`, `-vertical.svg`, `-vertical-blanco.svg` y `-isotipo.svg`.

No se deforman ni se les cambia el color; espacio libre alrededor igual al alto de la "S". A color solo sobre claro; sobre marino, el inverso o el blanco. Genesis, Southwire, UL y ETL (autorizados) están en `…/assets/logo/marcas/` y `…/assets/logo/certificaciones/`: UL y ETL solo junto al producto certificado.

**Lema y frases de marca:** "Encuéntrelo con nosotros", "Consígalo con nosotros". **Activos distintivos** (se repiten siempre igual): naranja sobre marino, los cables 3D sobre fondo crema, "cotización en menos de una hora".

## 4. Imágenes

### 4.1 Qué se usa

- **Producto:** las ilustraciones 3D propias (exactas, desde el catálogo). Nunca fotos de caja o carrete.
- **Contexto:** imágenes generadas con IA (fal.ai) que pasan la revisión (§4.4). Nunca se presentan como fotos de Suplelec o de un proyecto real; la de proyectos dice "Foto ilustrativa".
- **Diseños** (publicaciones, portadas, imágenes para compartir): Canva, con este color, estas fuentes y estos logos. En Canva existe el kit de marca **"Suplelec"** (también hay uno viejo, "Suplelec Old"). El conector de Canva solo lista los kits: no lee ni cambia sus colores, fuentes ni voz, así que el kit se ajusta a mano en Canva (Marca → kit → Colores, Fuentes, Logos, Voz de marca) con las tablas de §1 a §3. Revisado el 5 de octubre de 2026: el logo coincide; colores, fuentes y voz los confirma el usuario. El MCP de Canva también genera imágenes (`generate-image`), quita fondos y separa capas: sirve para retoques y variantes; para fotos realistas se prefiere fal.ai, que tiene más modelos y precio conocido por imagen. Modelo para las series: **Nano Banana Pro** (`fal-ai/nano-banana-pro`, USD 0,15 por imagen en 1K, más en 4K), elegido por calidad el 5 de octubre de 2026; en 4K da 5504 × 3072.

### 4.2 Dirección: el cable es el protagonista

Tres series con el mismo tratamiento: fondo o sombras en marino, una luz principal suave y un filo de luz naranja.

| Serie | Qué es |
| --- | --- |
| A. Bodegones de sistema | El dispositivo de cada sistema con su cable pelado, sobre fondo marino, como foto de catálogo |
| B. Dónde viven los cables | Arquitectura de Costa Rica a la hora azul, sin personas ni letreros; con tono marino cuando va de fondo |
| C. Materia | Macros de cobre, lámina de aluminio, hilo de drenaje y pares trenzados |

*Dirección propuesta el 4 de octubre de 2026; la está revisando el usuario.*

### 4.3 Bloques de prompt (van al final de cada prompt, en inglés)

**Serie A**

```
Commercial studio product photograph. Seamless deep navy blue background (hex #1e284e) that falls off to near black at the edges. One large soft key light from the upper left and a thin warm orange rim light (hex #ef7521) from behind on the right that outlines the edges of the objects. Dark, slightly glossy surface with soft reflections. Realistic materials and proportions, sharp focus on the cable end, gentle depth of field. Medium-format camera, 100 mm macro lens, f/8. Horizontal 16:9 composition: subject in the right half, the left half dark and empty for text. No people, no hands, no text, no letters, no numbers, no labels, no logos, no brand names, no printing on the cable jacket, no watermarks.
```

**Serie B**

```
Architectural photograph at blue hour, a few minutes after sunset. Deep blue sky with the last warm orange light on the horizon, interior lights on, damp ground with soft reflections. Straight vertical lines, 24 mm tilt-shift lens, f/8, tripod, natural colors. Horizontal 16:9 composition with calm, empty sky on one side. No people, no cars, no signs, no logos, no text, no flags. A generic building, not a recognizable real one.
```

**Serie C**

```
Extreme macro photograph, focus stacked. Seamless deep navy blue background (hex #1e284e), soft key light from the left and a thin warm orange rim light (hex #ef7521) from behind. Realistic copper, aluminum foil and plastic textures. Horizontal 16:9 composition, subject on one side, the rest dark and empty. No people, no hands, no text, no letters, no numbers, no logos, no printing on any surface.
```

Para redes, el mismo bloque con "Vertical 4:5 composition" o "Vertical 9:16 composition".

**Colores reales de los cables** (de `contenido/catalogo/` del sitio): incendio, chaqueta roja con conductores negro y rojo; control CMR, gris con negro, rojo, blanco y verde, y lámina con drenaje si lleva shield; termostato, blanco con rojo, blanco, verde, azul y amarillo; BACnet RS485, amarillo con un par negro y blanco estañado y lámina con drenaje; audio, blanco con negro y rojo de hilos finos.

### 4.4 Revisión antes de publicar (Claude)

Cada imagen se revisa a tamaño completo:

- **Errores típicos de la IA:** letras o números inventados (en la chaqueta, pantallas o botones), conductores que se funden o no salen de ningún lado, tornillos y bornes deformes, perspectivas imposibles, caras o manos escondidas en reflejos.
- **Detalle técnico** contra el catálogo: color de chaqueta y conductores, cantidad de conductores, sólido o trenzado, y lámina con drenaje **solo** en cables con shield. El cable de incendio es rojo. En escenas de instalación, el cable no cuelga suelto sobre el cielo ni de los tubos. Una mala práctica no se publica aunque se vea bonita.
- **Reglas:** sin rostros, sin bodega, sin marcas de terceros, sin códigos ni texto legible, sin nada que parezca un proyecto real de Suplelec ni un edificio real reconocible.
- **Que no se note la IA:** brillo plástico, simetrías perfectas o texturas repetidas son motivo de rechazo.
- **Serie pareja:** misma luz y mismo color en todas.
- **Anuncios:** Meta etiqueta las imágenes hechas con IA; en anuncios se prefieren las ilustraciones 3D y las de IA quedan para contexto.
- **Técnica (sitio):** WebP de 120 KB como máximo (60 KB en tarjetas), sin metadatos, con `width` y `height`.

Si algo falla y no se arregla con un recorte o un retoque pequeño, se genera otra.
