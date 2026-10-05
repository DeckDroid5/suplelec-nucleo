# Puntos de entrada y preguntas reales

Las situaciones en las que un cliente piensa en comprar cable de señal (*category entry points*, Ehrenberg-Bass). Gana la marca que el cliente asocia a más de ellas: cada pieza de contenido o anuncio se ata a una. Salen de `marca/perfil.md` §5 (por qué llega el cliente, sus frases y sus objeciones).

| # | Situación | Quién | Qué necesita oír |
| --- | --- | --- | --- |
| E1 | "Me especificaron un cable de otra marca" | Electromecánica, ingeniero | Que se homologa: envíe el modelo y le cotizamos el equivalente que cumple |
| E2 | "Mi proveedor no tiene" o "la obra está parada" | Todos | Entrega inmediata del stock disponible; cotización en menos de una hora |
| E3 | "Viene la inspección" o "el inspector rechazó el cable" | Electromecánica, constructora | Cable certificado (UL o ETL) y el correcto para cada tramo |
| E4 | "El diseño pide FPLR, plenum o con shield" | Ingeniero, electromecánica | Qué significa cada clasificación y cuál tenemos |
| E5 | "Un cliente del almacén pide cable de alarma" | Almacén eléctrico | Respuesta rápida para no perder la venta |
| E6 | "Estoy cotizando un proyecto o una licitación" | Electromecánica, constructora | Cotización formal con datos de Hacienda |
| E7 | "El cable pasa cerca de motores o variadores" | Ingeniero, técnico | Cuándo usar shield |
| E8 | "El cielo funciona como retorno de aire" | Ingeniero, electromecánica | Cable plenum (FPLP, CMP) |
| E9 | Temporada alta (mayo a julio) | Almacén eléctrico | Disponibilidad y rapidez |

## Preguntas reales (`preguntas.csv`)

Cada pregunta que llega por WhatsApp, el formulario, una llamada, un comentario o una búsqueda en Search Console, con sus palabras. Columnas: `fecha`, `origen` (whatsapp, formulario, llamada, comentario, search-console), `segmento` (almacen, electromecanica, constructora, ingeniero), `entrada` (E1 a E9), `pregunta`, `estado` (nueva, en-faq, en-guia, en-redes, descartada) y `donde` (URL o archivo donde quedó respondida). Sin nombres de clientes. Marketing las anota; el sitio las convierte en preguntas frecuentes o guías.
