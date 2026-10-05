# Medición

Convenciones que comparten el sitio y el marketing para saber de dónde sale cada cotización, desde el clic hasta la factura en Alegra.

## 1. UTM en los enlaces al sitio

Todo enlace a suplelec.com que se publique fuera del sitio lleva UTM, en minúsculas y con guiones.

| Parámetro | Valores |
| --- | --- |
| `utm_source` | `facebook`, `instagram`, `linkedin`, `gbp` (Google Business Profile), `whatsapp`, `google`, `bing`, `correo` |
| `utm_medium` | `social` (publicación), `cpc` (anuncio), `perfil` (biografía o ficha), `mensaje` (WhatsApp o correo) |
| `utm_campaign` | `<año>-<mes>-<tema>`: `2026-11-que-pase-la-inspeccion`. Para anuncios, el código de §2 en minúsculas: `g-inc-01` |
| `utm_content` | Opcional, la pieza: `carrusel-fplr` |

Ejemplo: `https://suplelec.com/catalogo/incendio/?utm_source=linkedin&utm_medium=social&utm_campaign=2026-11-que-pase-la-inspeccion`. El enlace de la ficha de Google Business Profile: `?utm_source=gbp&utm_medium=perfil`.

## 2. Código de campaña en WhatsApp

Para los anuncios. Formato `<canal>-<aplicación>-<número>`:

- Canal: `G` (Google Ads), `M` (Meta), `L` (LinkedIn), `B` (Microsoft).
- Aplicación: `INC` (incendio), `ROB` (robo y control de acceso), `AIR` (aire acondicionado), `BAC` (BACnet), `AUD` (audio), `GEN` (general).

Cuando el sitio lo tenga (solicitud S1), el mensaje prellenado de WhatsApp termina con "ref: G-INC-01" si la visita llegó con ese `utm_campaign`. Los anuncios de clic a WhatsApp de Meta llevan el código en su mensaje inicial.

## 3. Eventos del sitio (GA4)

`whatsapp_click`, `phone_click`, `email_click` y `generate_lead` (envío del formulario) son eventos clave. GA4 solo carga si el visitante acepta las cookies (Ley 8968), así que cuenta menos visitas de las reales: los totales salen de Search Console (clics desde Google) y Cloudflare (todas las visitas).

## 4. Origen de cada cotización (Alegra)

Ventas escribe el origen en las observaciones de cada cotización en Alegra:

`Origen: sitio` · `Origen: WhatsApp` · `Origen: llamada` · `Origen: anuncio` · `Origen: redes` · `Origen: recurrente` · `Origen: referido`, y el `ref:` si el mensaje traía uno.

Con eso, el informe cuenta cuántas cotizaciones salieron de cada fuente y cuántas terminaron en factura (estado "facturada").
