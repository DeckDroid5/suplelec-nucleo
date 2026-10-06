# Medición

Convenciones que comparten el sitio y el marketing para medir qué trae contactos y clientes nuevos, desde el clic hasta la factura en Alegra, sin pedirle a ventas que anote nada.

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

Cuando el sitio lo tenga (solicitud S1), el mensaje prellenado de WhatsApp termina con "ref: G-INC-01" si la visita llegó con ese `utm_campaign`. Solo informa a quien atiende; no se anota en ningún lado (§4). Los anuncios de clic a WhatsApp de Meta llevan el código en su mensaje inicial.

## 3. Eventos del sitio (GA4)

`whatsapp_click`, `phone_click`, `email_click` y `generate_lead` (envío del formulario) son eventos clave. GA4 solo carga si el visitante acepta las cookies (Ley 8968), así que cuenta menos visitas de las reales: los totales salen de Search Console (clics desde Google) y Cloudflare (todas las visitas).

## 4. Cotizaciones y clientes nuevos (Alegra)

**Ventas no anota el origen de las cotizaciones** (decisión del usuario, 5 de octubre de 2026: llevar ese seguimiento a mano es complicado). La medición no depende de ventas:

- **De Alegra, sin que nadie anote nada:** cotizaciones de la semana, **clientes nuevos** (su primera cotización) y cuántas terminan en factura. Los clientes nuevos son la señal principal de que el marketing trae gente; los recurrentes compran igual.
- **Del sitio:** los eventos de §3 (cuántos tocan WhatsApp, llaman, escriben o mandan el formulario) y en qué página.
- **De los anuncios:** las conversiones que cuenta cada plataforma con esos mismos eventos. El `ref:` de §2 llega en el mensaje y le dice a quien atiende de qué anuncio viene, pero no se registra.

Así, el informe compara semana a semana los contactos desde el sitio con las cotizaciones de clientes nuevos, sin unir cada cotización con su fuente.
