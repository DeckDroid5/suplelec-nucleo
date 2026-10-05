# Solicitudes entre proyectos

Pedidos de un proyecto al otro. Al abrir una sesión, el hook (`scripts/al-iniciar.sh`) muestra los abiertos para ese proyecto. Al cumplir uno, se mueve a "Hechas" con la fecha. Formato de cada fila: número, fecha, `origen → destino`, qué y cuándo.

## Abiertas

| # | Fecha | De → para | Qué | Cuándo |
| --- | --- | --- | --- | --- |
| S1 | 2026-10-04 | marketing → sitio | Código de campaña en el mensaje prellenado de WhatsApp: si la visita llega con `utm_campaign`, el mensaje termina con "ref: …" (`medicion/medicion.md` §2), para que ventas anote el origen en Alegra | Antes de los anuncios (enero de 2027) |
| S2 | 2026-10-04 | marketing → sitio | Consentimiento para publicidad (`ad_storage`, `ad_user_data`) en el aviso de cookies y política de privacidad actualizada (Ley 8968) | Antes de anuncios con medición de conversiones |
| S3 | 2026-10-04 | marketing → sitio | Imágenes para compartir (Open Graph, 1200 × 630) desde las plantillas de Canva | Cuando estén las plantillas |
| S4 | 2026-10-04 | sitio → marketing | Informe semanal de tráfico y SEO del sitio; lo que pida trabajo en el sitio (páginas que caen, consultas sin página, errores de indexación) vuelve como solicitud | Al tener los accesos de Google (`docs/medicion.md` de marketing) |

## Hechas

| # | Fecha | De → para | Qué | Hecha |
| --- | --- | --- | --- | --- |
