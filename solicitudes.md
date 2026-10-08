# Solicitudes entre proyectos

Pedidos de un proyecto al otro. Al abrir una sesión, el hook (`scripts/al-iniciar.sh`) muestra los abiertos para ese proyecto. Al cumplir uno, se mueve a "Hechas" con la fecha. Formato de cada fila: número, fecha, `origen → destino`, qué y cuándo.

## Abiertas

| # | Fecha | De → para | Qué | Cuándo |
| --- | --- | --- | --- | --- |
| S1 | 2026-10-04 | marketing → sitio | Código de campaña en el mensaje prellenado de WhatsApp: si la visita llega con `utm_campaign`, el mensaje termina con "ref: …" (`medicion/medicion.md` §2), para que ventas anote el origen en Alegra | Antes de los anuncios (enero de 2027) |
| S2 | 2026-10-04 | marketing → sitio | Consentimiento para publicidad (`ad_storage`, `ad_user_data`) en el aviso de cookies y política de privacidad actualizada (Ley 8968) | Antes de anuncios con medición de conversiones |
| S5 | 2026-10-05 | marketing → sitio | Indexación (primer informe semanal, `privado/informes/2026-S40.md` de marketing): de 44 URL del sitemap, Google tiene 5 indexadas; 30 "descubiertas, sin indexar" y 8 que aún no reconoce (normal 4 días después del lanzamiento, pero conviene empujar). 1) Quitar de Search Console los sitemaps viejos `sitemap.rss` y `sitemap.xml` (del sitio anterior, leídos en junio de 2025, con errores); la cuenta de servicio es restringida y no puede. 2) Pedir la indexación a mano de las páginas clave (guías y aplicaciones primero; unas 10 por día). 3) Activar IndexNow en Rank Math (ya en la lista del sitio). **2026-10-07, sitio:** 3) hecho en el despliegue (Rank Math, módulo IndexNow, solo en suplelec.com) y sitemap con las 5 aplicaciones; 1) y 2) los hace el usuario en Search Console. El informe de cada lunes dirá cómo avanza | Esta semana |

## Hechas

| # | Fecha | De → para | Qué | Hecha |
| --- | --- | --- | --- | --- |
| S3 | 2026-10-04 | marketing → sitio | Imágenes para compartir (Open Graph, 1200 × 630) desde las plantillas de Canva | 2026-10-07: cerrada con aprobación del usuario; el sitio las genera con código (`scripts/compartir/generar.sh`: marino, logo, título e imagen de la página), 46 en producción desde el despliegue del 7 de octubre |
| S4 | 2026-10-04 | sitio → marketing | Informe semanal de tráfico y SEO del sitio; lo que pida trabajo en el sitio vuelve como solicitud | 2026-10-05: `scripts/informes/semanal.py` de marketing (GA4, Search Console con la indexación de cada URL, PageSpeed y CrUX; Bing y Cloudflare cuando estén sus claves). Primer informe: S5 |
