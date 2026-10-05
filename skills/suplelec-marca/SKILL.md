---
name: suplelec-marca
description: Reglas de marca, diseño y contenido de Suplelec. Usar al escribir cualquier texto público (páginas, productos, guías, publicaciones en redes, anuncios, mensajes de WhatsApp, correos), al diseñar o modificar el tema de WordPress (theme.json, patrones, plantillas, CSS) y al preparar imágenes o videos.
---

# Marca Suplelec

Las fuentes de verdad están en el núcleo compartido: `nucleo/instrucciones/comunes.md` (reglas), `nucleo/marca/perfil.md` (empresa, clientes, voz), `nucleo/marca/identidad.md` (color, tipografía, logos, imágenes) y `nucleo/tecnico/usos-cables.md` (lo que el técnico aprobó). Leer la sección que aplique antes de trabajar; este archivo solo resume lo que no se puede olvidar.

## Contenido (perfil §8)

- Trato de usted, español de Costa Rica, frases cortas y técnicas.
- Acción principal: "Solicitar cotización" (WhatsApp +506 6309-2565 o ventas@suplelec.com).
- Nunca: precios, "stock garantizado", nombres de clientes, competidores, emojis en títulos, frases de relleno ("en el mundo actual", "descubra", "sin duda"), festividades, crédito, método de entrega, fecha de fundación, "caja", "carrete" o "Pull Box" (solo el largo por rollo).
- Nunca códigos de producto ni fichas técnicas en público; nunca "Ver ficha".
- Marcas: solo Genesis y Southwire, cada una por su lado (no decir que Genesis es de Southwire). No mencionar Belden, Windy City ni el cable de red. "Hecho en EE. UU." solo en la familia con el sello en su ficha.
- "Resistente a la luz solar" no quiere decir que el cable pueda quedar a la intemperie: no presentarlo como ventaja en cables de interior; para exteriores, un cable dedicado.
- Normas: citar la edición más reciente (hoy, NEC 2026) y decir cuál está oficializada en Costa Rica (NEC 2020).
- Datos técnicos: solo los de `usos-cables.md` o una ficha. Si no, `[VALIDAR CON TÉCNICO]` y no se publica.
- Revisión técnica: "Revisado por el equipo técnico de Suplelec", sin nombres.
- Antes de dar por bueno un texto: `python3 nucleo/reglas/revisar.py <archivo>`.

## Redes y anuncios

- Cada pieza se ata a una situación real del cliente (`nucleo/publico/puntos-de-entrada.md`) y a un pilar del plan de marketing.
- Hashtags y emojis con mesura: ninguno en títulos, pocos en el texto.
- Los anuncios usan las ilustraciones 3D; las imágenes de IA, solo de contexto (Meta las etiqueta).
- Enlaces al sitio con UTM según `nucleo/medicion/medicion.md`.

## Diseño

- Color, tipografía y logos: `nucleo/marca/identidad.md`. Naranja `#ef7521` y verde `#06d6a0` nunca como texto sobre fondo claro; texto marino sobre naranja, nunca blanco.
- **En el sitio** (`docs/diseno.md`): solo colores de la paleta de `theme.json`; texto secundario `muted-foreground` `#5c5c5c`; bordes de campos `input` `#8a8278`; tamaños, espacios, radios y sombras solo de la escala; nada por debajo de 13 px; sin videos automáticos, carruseles, librerías de UI ni CDN de fuentes.

## Imágenes (identidad §4)

- Producto: solo las ilustraciones 3D aprobadas. Fotos oficiales de Southwire y Genesis (autorizadas) solo en Marcas.
- Contexto: imágenes de fal.ai (Seedream o Nano Banana Pro) con los bloques de prompt de la identidad, revisadas con su lista (§4.4) y elegidas por el usuario.
- Sin rostros, bodega, logos de terceros, texto legible ni nada que las haga pasar por fotos de Suplelec o de un proyecto.
- Sin códigos visibles en etiquetas, en la leyenda de la chaqueta, en nombres de archivo ni en EXIF.
- En el sitio: AVIF o WebP, máximo 120 KB la principal y 60 KB las de tarjeta, con `width` y `height`.
