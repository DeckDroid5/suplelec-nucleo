# Usos de cada línea de cable

*Aprobado por el técnico el 27 y 28 de septiembre de 2026 (página de usos y hojas R1 a R4, `docs/catalogo.md` §7).*

*Banco de afirmaciones técnicas aprobadas de Suplelec: el sitio y el marketing solo publican lo que está aquí o en una ficha. Las rutas `docs/`, `contenido/`, `scripts/` y `privado/` son del repositorio del sitio (`~/suplelec`), donde viven las fichas y las herramientas de revisión.*

Qué se puede decir de cada familia del catálogo (`docs/catalogo.md` §2): para qué sirve y dónde se instala según su clasificación. Cada afirmación lleva un número (U1, U2…) y su fuente; los textos del sitio (`contenido/`) y `privado/fichas/fuentes.csv` los citan. Una afirmación técnica nueva que no esté aquí ni en una ficha pasa por el técnico antes de publicarse.
<!-- solo-repo -->
**Sin códigos.** Este documento se versiona: no lleva números de parte.
<!-- /solo-repo -->

## Fuentes

| Clave | Fuente | Fecha |
| --- | --- | --- |
| F1 | Páginas de producto de Southwire (dueña de Genesis desde 2023), una por familia: pestañas "Application & Features", "Standards & References" y "Construction". Copia en `privado/fichas/web/southwire/`, bajada con `scripts/catalogo/paginas-southwire.sh` | Consultadas el 26-9-2026 |
| F2 | Catálogo de productos Genesis 2023. Las páginas citadas son las impresas en el catálogo | Diciembre de 2023 |
| F3 | Fichas de Southwire por categoría (una por familia de Genesis, incluida la del RS-485). Copia en `privado/fichas/web/southwire/` y texto en `privado/fichas/texto/southwire-2025/`. En lugares de instalación y normas coinciden con F1, salvo lo que dice la sección 6 | 2025 |
| F4 | Fichas técnicas de Genesis por código (`privado/fichas/genesis/`) | 2018 a 2021 |
| F5 | Fichas de productos marca Southwire de la misma clasificación: cable armado Red Alert MC-FPLP, multiconductor riser con y sin shield, FPLR, alarma de robo y control de acceso. Sirven de referencia de uso para cables equivalentes | Varias |
| F6 | Decreto Ejecutivo 36979-MEIC, Reglamento de Oficialización del Código Eléctrico de Costa Rica (RTCR 458:2011), en el [SCIJ](https://pgrweb.go.cr/scij/Busqueda/Normativa/Normas/nrm_texto_completo.aspx?param1=NRTC&nValor1=1&nValor2=77291&nValor3=96805&strTipM=TC) y el [MEIC](https://www.meic.go.cr/wp-content/uploads/2024/11/36979.pdf) | Consultado el 26-9-2026 |
| F7 | Benemérito Cuerpo de Bomberos: [Pruebas de detección y alarma](https://www.bomberos.go.cr/pruebas-de-deteccion-y-alarma/) y [Reglamento Nacional de Protección Contra Incendios 2023](https://www.bomberos.go.cr/wp-content/uploads/2023/03/RNPCI-2023.pdf) | Consultado el 26-9-2026 |
| F8 | CFIA, centro de ayuda: "¿Cuáles normas o certificaciones de productos eléctricos están aprobadas según el código eléctrico?" (el profesional responsable elige las certificaciones; los entes extranjeros, reconocidos internacionalmente o aceptados por el ECA). Copia en `privado/fichas/texto/` | Actualizado el 1-5-2024; consultado el 28-9-2026 |
| F9 | OSHA, programa NRTL: páginas de UL LLC e Intertek Testing Services NA (las dos con UL 13, UL 444 y UL 1424 en su alcance) | Consultado el 28-9-2026 |


## Respuestas y criterios del técnico

Los textos citan estas respuestas por su clave.

| Clave | Respuesta |
| --- | --- |
| P1 | El cable de incendio siempre es rojo. Aunque los cables de control también sean FPLR (U33), para incendio se recomienda la línea roja |
| P2 | El shield se necesita en circuitos de señal que pasan cerca de fuentes electromagnéticas que generan corrientes parásitas |
| P3, R2-3 | Los multipares tienen poca rotación: quedan en el catálogo sin destacar |
| P4 | Para comunicación de aire acondicionado sirve el CMR sin shield. El RS-485 es siempre un bus de comunicación de alta velocidad |
| P5 | El cable plenum es de uso muy esporádico: sus familias van al final y no se destacan |
| P6, R1-3 | El FPL para enterrado directo viene negro: el código no exige un color y el negro protege la chaqueta del sol y la humedad |
| R1-1 | Jerarquía de incendio: FPLP reemplaza a FPLR y FPL; FPLR reemplaza a FPL y no va en plenum; FPL no reemplaza a ninguno (NEC 760.154) |
| R1-2, G7-2 | Lazo SLC de paneles direccionables: FPLR 18/2 sin shield (el shield agrega capacitancia y corrompe los datos del lazo); con shield solo si la especificación o el manual del panel lo piden, conectado a tierra como indique el manual. Cerca de motores, variadores o tableros, el ruido se evita separando la tubería, no con shield |
| R1-4 | El armado de Southwire es MC-FPL (la cinta dice "TYPE MC 600V OR TYPE FPL 300V 90°C DRY"), no FPLP |
| R1-5 | El FPLR no va en plenum (no pasa la prueba de plenum) y el FPL no va en riser (no pasa UL 1666) |
| R2-1 | Los usos propuestos para el cable de control reflejan la demanda en Costa Rica |
| R2-2 | Los teclados de alarma se cablean sin shield (22/4 o 18/4) |
| R3-1 | El conductor amarillo del RS-485 de 1,5 pares es la referencia común de señal |
| R3-2 | Se publica la impedancia de 115 Ω del RS-485 |
| R3-3 | El termostato plenum (CL2P) sí va en cielos que funcionan como retorno de aire |
| R3-4, R4-2 | En las diferencias de temperatura se publica 75 °C, de las fichas 2025, sujeto a lo impreso en la chaqueta |
| R3-5 | En el termostato híbrido, el conductor de 18 AWG es el rojo, de alimentación |
| R3-6 | El termostato de 22 AWG no se agrega: solo bajo consulta |
| R4-1 | La clasificación del Audacious riser es la impresa en la chaqueta (queda CL2R, de la ficha 2025) |
| R4-3 | Audacious para alta fidelidad, cine en casa y salas de reuniones; cable de sonido riser para sonido ambiental distribuido de 70 V o 100 V en oficinas y pasillos |
| G-1 | Se citan las normas en su edición más reciente, diciendo cuál está oficializada en Costa Rica (U10) |
| G-2 | Son correctas las frases de experiencia de la guía 1 (el FPLR es el más usado; la inspección revisa la clasificación impresa) |
| G-3 | Prueba de uso general: UL 1685 (edición 2025), la versión actual de la prueba de bandeja vertical de UL 1581 |
| G-4 | Sugiere ilustrar en las guías 1 y 8 cuándo el cielo es plenum: con el retorno de aire por ducto el espacio sobre el cielo no es plenum; con el retorno abierto, sí (DG8). Texto de la sección aprobado el 28 de septiembre de 2026 |
| G2 | Guía 2 (homologación): correctos el calibre más grueso (G2-1), la tabla de lo que tiene que coincidir (G2-2), los errores comunes (G2-3) y el manual del panel (G2-4). **G2-5:** Bomberos solo revisa el funcionamiento; el cable lo verifica el CFIA |
| G3 | Guía 3 (aire acondicionado): no hace falta un calibre de referencia para la comunicación (G3-1); correctos el bus en cadena con terminación en los extremos (G3-2) y que el cable de termostato no se recomienda para comunicación (G3-3); el cable RS-485 siempre trae shield (G3-4) |
| G4 | Guía 4 (UL y ETL): correctos la confusión del nombre UL (G4-1), la "c" de Canadá y el directorio del laboratorio (G4-3). **G4-2:** no se menciona el ECA ni el certificador extranjero, porque la competencia puede usarlo; un ingeniero puede rechazar un cable ETL por costumbre de usar UL, sin fundamento técnico |
| G5 | Guía 5 (alarma de robo), aprobada el 1 de octubre de 2026. **G5-1:** el teclado lleva 18/4 en tramos largos (consume corriente para pantalla e iluminación; evita la caída de tensión) o si el fabricante lo pide. **G5-2:** la sirena consume más que los sensores: 18/2 (18/4 si tiene contacto contra sabotaje). **G5-3:** es común conectar en serie los contactos de puertas o ventanas vecinas en una misma zona: "un cable hasta cada sensor o zona de sensores" |
| G6 | Guía 6 (control de acceso), aprobada el 1 de octubre de 2026 sin cambios: correctas las tres opciones de cableado (G6-1), la cerradura en 18 AWG por su consumo (G6-2) y el lector siempre con shield, porque sus datos son sensibles al ruido (G6-3) |
| G7 | Guía 7 (incendio), aprobada el 1 de octubre de 2026 con la corrección del SLC (R1-2, G7-2). **G7-1:** el NAC lleva más corriente; 16/2 es lo común y en tramos largos la especificación puede pedir 14 o 12 AWG. **G7-3:** correcto: Bomberos revisa el funcionamiento según NFPA 72 y el profesional responsable ante el CFIA, el cable |
| G9 | Guía 9 (termostato), aprobada el 1 de octubre de 2026: correctos el 18/5 para equipos sencillos y el 18/8 para más etapas o funciones (G9-1) y los conductores de reserva; los termostatos con Wi-Fi necesitan un conductor común (C) (G9-2) |
| G11 | Guía 11 (bus BACnet, RS-485 y Modbus), aprobada el 5 de octubre de 2026. **G11-1:** correcto: el cable de control puede transmitir datos, pero en un bus RS-485 da fallas; el bus pide par trenzado, shield e impedancia acoplada a las terminaciones. **G11-2:** el cable de 115 Ω funciona con terminaciones de 115 a 120 Ω. **G11-3:** sin distancia máxima: la indica el manual del equipo. **G11-4:** el drenaje del shield, como pida el manual: a tierra en un solo extremo del bus; en los dos extremos o en varios puntos se forman lazos de tierra que meten ruido en la red. **G11-5:** no se recomiendan calibres |
| G10 | Fórmula de la guía 10 (caída de tensión), 5 de octubre de 2026. **G10-1:** caída = 2 × L × I × R ÷ 1000, correcta y del lado seguro con toda la carga al final; la calculadora debe permitir además repartir los equipos a lo largo del tramo (punto a punto), para no sobredimensionar circuitos largos con varios equipos. **G10-2:** se calcula con la tensión de la batería al final de su autonomía: 20,4 V en sistemas de 24 V y 10,5 V en los de 12 V. **G10-3:** el criterio es que la tensión no baje de la mínima de la ficha del equipo; 10 % de caída (o lo que pida la norma local) como referencia general. **G10-4:** corregir por temperatura (el cobre sube cerca de 4 % cada 10 °C), con un campo para la temperatura. **G10-5:** el 22 AWG sólido con el dato de la ficha 2025 (18,0 Ω/1000 pies). **G10-6:** notificación de incendio, alarma de robo y control de acceso (sugirió también alimentación de cámaras sin PoE: no va, el video no está en el sitio). **G10-7:** aviso aprobado: "Es una referencia para elegir el calibre. Manda el manual del panel y de cada equipo, y el diseño lo firma el profesional responsable." Resistencias por calibre (fichas 2025, a 20 °C, Ω/km): sólido 22: 59,1; 20: 36,4; 18: 21,4; 16: 13,5; 14: 8,4; 12: 5,3; trenzado 24: 87,6; 22: 55,4; 18: 21,9; 16: 13,7; 14: 8,6; 12: 5,4 |
| Sol | "Resistente a la luz solar" no quiere decir que el cable pueda quedar a la intemperie (U7) |

---

## 1. Conceptos que aplican a todas las familias

*Van en las guías, no en las páginas de producto (técnico, 27 de septiembre).*

**U1.** La clasificación de un cable dice dónde se puede instalar. De mayor a menor exigencia: **plenum** (P), **vertical o riser** (R), **uso general** (sin letra o G) y **vivienda** (X). Un cable de nivel más alto puede reemplazar a uno de nivel más bajo, pero no al revés: un CMP sirve donde se pide CMR, y un CMR no sirve donde se pide CMP. *(F2, pág. 63: jerarquía de sustitución para cables CM, CL2 y CL3)*

**U2.** Qué es cada nivel *(F2, pág. 64)*:
- **Plenum:** se instala en ductos o en espacios por donde circula el aire del edificio.
- **Riser:** se instala en tramos verticales que atraviesan varios pisos.
- **Uso general:** se instala en tubería o canalización, o en un solo piso.

**U3.** Las letras dicen para qué circuitos está listado el cable *(F1, normas de cada familia; F5)*:
- **FPL** (FPLP, FPLR, FPL): circuitos de alarma contra incendio de potencia limitada. Norma UL 1424; artículo 760 del NEC.
- **CL2 y CL3** (con P, R o sin letra): circuitos de control remoto, señalización y potencia limitada clase 2 y clase 3. Norma UL 13; artículo 725 del NEC.
- **CM** (CMP, CMR, CM): circuitos de comunicaciones. Norma UL 444; artículo 800 del NEC.
- **FT4 y FT6:** las mismas pruebas de llama según la norma canadiense (FT4 equivale a riser; FT6, a plenum).

**U4.** En incendio la jerarquía es la misma: FPLP reemplaza a FPLR y FPL; FPLR reemplaza a FPL; FPL no reemplaza a ninguno. *(Técnico, R1-1, 28 de septiembre de 2026: NEC 760.154 y UL 1424)*

**U5.** *(No se usa: el técnico consideró innecesaria la explicación del artículo 300.22.)*

**U6.** Los cables riser y de uso general pueden entrar a esos espacios de aire si van dentro de canalización metálica que cumpla 300.22(B), o sobre bandeja metálica de fondo sólido con tapa metálica sólida. Sueltos, no: ahí va un cable plenum. *(F1: así lo dice cada familia riser y de uso general; lo de "sueltos no" es deducción de Claude)* *(Aprobado el 28 de septiembre de 2026)*

**U7.** **Resistente a la luz solar**: la chaqueta fue evaluada durante 720 horas bajo luz ultravioleta y humedad ligera. *(F2, pág. 67)* **Corrección del técnico (28 de septiembre de 2026):** solo indica cierto grado de resistencia; **no** quiere decir que el cable pueda quedar a la intemperie. Para exteriores se usa un cable dedicado (el FPL para exterior y enterrado directo o el Audacious para enterrado directo). El sitio ya no lo presenta como ventaja en los cables de interior (sale de "Lo esencial"; sigue en las especificaciones).

**U8.** **Enterrado directo** quiere decir que se puede enterrar con tubería o sin ella. Se evalúa por absorción de agua y resistencia al aplastamiento. *(F2, pág. 67)*

**U9.** UL e Intertek (ETL) son laboratorios reconocidos (NRTL) y prueban con las mismas normas: un listado UL y uno ETL de la misma clasificación significan lo mismo. El número de archivo del listado va impreso en la chaqueta. *(F2, págs. 61 y 62)*

**U10.** En Costa Rica, la norma NFPA 70 (el NEC) está oficializada como Código Eléctrico de Costa Rica por el Decreto 36979-MEIC (RTCR 458:2011), que adopta "su última versión actualizada en español". La vigente es la de 2020, oficializada en La Gaceta 126 del 10 de julio de 2024 (comunicado del CFIA). La edición más reciente del NEC es la 2026: reúne los requisitos de los cables de energía limitada en el artículo 722 (en la 2020 están en los artículos 760, 725 y 800), sin cambiar las clasificaciones ni la jerarquía de sustitución. Por decisión del usuario, las guías citan la edición más reciente y dicen cuál está oficializada. *(F6; investigación del 28 de septiembre de 2026, pregunta G-1)*

**U11.** Bomberos exige que los sistemas de detección y alarma cumplan NFPA 72 y los revisa con pruebas funcionales. *(F7)*

**U12.** Tensión nominal: 300 V en los cables de incendio, control, comunicación y audio; 150 V en el de termostato; 600 V en el armado (como tipo MC). *(F1, F2)*

---

## 2. Incendio

**U13.** Sistemas de incendio que atienden estos cables: detección convencional e inteligente (direccionable), notificación audible y visual, y comunicación masiva de emergencia. *(F2, pág. 21)*

**U14.** Circuitos típicos: señalización de protección contra incendio, detectores de humo, comunicación por voz, control de audio y circuitos de iniciación. *(F5, ficha FPLR de Southwire)*

**U15.** Las páginas de Southwire de las familias Genesis de incendio (FPLR, FPLP y enterrado directo, con y sin shield) dicen "UL listed, and Made in the USA". *(F1)*

### 2.1 Cable de incendio FPLR sin shield

**U16.** Clasificación FPLR, CL3R y FT4, resistente a la luz solar. Conductores de cobre desnudo sólido (en 12 AWG también trenzado), aislamiento de polipropileno y chaqueta de PVC. 300 V, de −20 a 75 °C. *(F1; F2, pág. 24)* La ficha 2025 agrega el listado de comunicaciones CMR de 22 a 16 AWG. *(F3)*

**U17.** Se puede instalar: en risers; dentro de edificios, fuera de espacios de aire y de risers; en canalización metálica según 300.22(B); sobre bandeja metálica de fondo sólido con tapa; expuesto al sol. *(F1)*

**U18.** No va en un cielo falso que sirve de retorno de aire (ahí va FPLP) y no se entierra (ahí va el FPL para enterrado directo). *(Técnico, R1-5, 28 de septiembre de 2026: el FPLR no cumple la prueba de plenum)*

### 2.2 Cable de incendio FPLR con shield

**U19.** Igual que el FPLR sin shield (U16 y U17), más una lámina metálica (foil) sobre todos los conductores. *(F1; F2, pág. 25)*

**U20.** Cuándo se usa con shield en vez de sin shield: en circuitos de señal que pasan cerca de fuentes electromagnéticas que generan corrientes parásitas. *(Técnico, respuesta a P2)*

### 2.3 Cable de incendio FPLP sin shield

**U21.** Clasificación FPLP, CL3P y FT6 (prueba de plenum NFPA 262). Aislamiento de PVC de baja emisión de humo y chaqueta de PVC para plenum. 300 V, de −20 a 75 °C. *(F1; F2, pág. 22)* La ficha 2025 agrega el listado de comunicaciones CMP de 22 a 16 AWG. *(F3)*

**U22.** Se puede instalar: en ductos fabricados (300.22(B)); en otros espacios de aire (300.22(C)); en risers; dentro de edificios. *(F1)* Reemplaza al FPLR en cualquier lugar (U4).

**U23.** No tiene listado de resistencia a la luz solar: no debe quedar expuesto al sol. *(Deducción de Claude, aprobada el 28 de septiembre de 2026; ver U7)*

### 2.4 Cable de incendio FPLP con shield

**U24.** Igual que el FPLP sin shield (U21 a U23), más una lámina metálica sobre todos los conductores. *(F1; F2, pág. 23)*

### 2.5 Cable de incendio FPL para enterrado directo

**U25.** Clasificación FPL y CL2 (prueba de uso general UL 1685), listado para enterrado directo y resistente a la luz solar. Aislamiento de PVC resistente al sol y chaqueta de PVC. 300 V, de −20 a 75 °C. *(F1; F2, pág. 26)*

**U26.** Se puede instalar: enterrado, con tubería o sin ella; en canalización metálica según 300.22(B); sobre bandeja metálica con tapa; dentro de edificios, fuera de espacios de aire y de risers. *(F1)*

**U27.** Uso típico: tramos de un sistema de incendio que van enterrados, con tubería o sin ella, o por exteriores expuestos al sol. *(F1; F2, pág. 26: "Outdoor Rating: Direct Burial, Sunlight Resistant". Confirmado con las fichas el 28 de septiembre de 2026)*

**U28.** No va en risers ni en espacios de aire (no es FPLR ni FPLP). *(Técnico, R1-5, 28 de septiembre de 2026: no tiene la prueba de riser UL 1666)* Es CL2 y no CL3, así que no reemplaza a un cable CL3. *(Deducción de Claude, aprobada el 28 de septiembre de 2026)*

### 2.6 Cable de incendio armado MC (Southwire, Red Alert)

**Actualización del 28 de septiembre de 2026:** la ficha más nueva del cable que vende Suplelec (un par con shield, SPEC 60411 de enero de 2026) y su página en Southwire lo listan como **MC-FPL**: 600 V como MC y 300 V y 90 °C en seco como FPL. La ficha vieja (F5) decía MC-FPLP. Southwire no declara el país de origen: solo que cumple "Buy American" si se pide "Made in the USA Only". El sitio no dice "hecho en EE. UU." de este cable. **Confirmado por el técnico (R1-4):** la leyenda de la cinta interna dice "TYPE MC 600V OR TYPE FPL 300V 90°C DRY"; no es FPLP.

**U29.** Conductores THHN/THWN (14 y 12 AWG) o TFN (18 y 16 AWG), tierra verde o de cobre estañado, armadura de aluminio entrelazada **roja**. Listado como tipo MC (600 V) y FPLP (300 V) según la ficha vieja; la vigente dice MC-FPL (R1-4). *(F5)*

**U30.** Usos según Southwire *(F5)*:
- Plenums, ductos y otros espacios de aire (NEC 300.22(C) y 760.135(C)).
- Circuitos de alarma contra incendio de potencia limitada y no limitada: detectores de humo, campanas, sirenas, paneles de control y dispositivos de iniciación y señalización.
- Circuitos clase 1, 2 y 3 de control remoto y señalización; circuitos de fuerza, iluminación, control y señal.
- Instalación oculta o expuesta, pasado por pared o empotrado en repello, en bandeja y canalizaciones aprobadas.
- Lugares de reunión (NEC 518.4), teatros (520.5) y bajo piso elevado de salas de cómputo (645.5(D)).
- Lugares peligrosos clase I división 2, clase II división 2 y clase III división 1.

---

## 3. Robo y control de acceso

**U31.** Sistemas que atienden: alarma de robo (intrusión), control de acceso y video. *(F2, págs. 8 y 9)*

**U32.** Usos de los cables multiconductor según Southwire: circuitos de control remoto, señalización y potencia limitada (NEC 725); de 22 a 16 AWG, también comunicaciones (NEC 800). Seguridad, sonido y audio, parlantes, perifoneo, intercomunicador, refuerzo de sonido, alarma, control de acceso y controles de potencia limitada. *(F5, fichas multiconductor riser con y sin shield)*

**U33.** Los cables de control Genesis **también están listados como FPLR o FPLP**, además de CMR o CMP. *(F1)* Aun así, para incendio se usa siempre cable rojo (técnico, respuesta a P1): el sitio no presenta el cable de control como opción para incendio.

### 3.1 Cable de control CMR sin shield

**U34.** De 22 a 16 AWG: CMR, CL3R, FPLR y FT4. En 14 y 12 AWG: solo CL3R y FPLR (no CMR). Resistente a la luz solar. Cobre desnudo, aislamiento de polipropileno, chaqueta de PVC. 300 V, de −20 a 75 °C. *(F1; F2, pág. 13)*

**U35.** Se puede instalar en los mismos lugares que el FPLR (U17). *(F1)*

**U36.** Uso típico sin shield: sensores y contactos de alarma de robo, y la interconexión de alarmas de robo con su panel. *(F5, ficha de cable de alarma de robo)* Con shield, los circuitos de señal que pasan cerca de fuentes electromagnéticas que generan corrientes parásitas. *(Técnico, respuesta a P2)*

### 3.2 Cable de control CMR con shield

**U37.** Igual que el CMR sin shield (U34 y U35), más una lámina metálica sobre todos los conductores. *(F1; F2, pág. 14)*

**U38.** Uso típico con shield: lectores de tarjeta (en el cable de control de acceso Genesis, el componente del lector siempre lleva shield; ver U45). *(F2, pág. 19)* Para comunicación de aire acondicionado sirve también el CMR **sin** shield. *(Técnico, respuesta a P4)* Los teclados de alarma se cablean sin shield (22/4 o 18/4); el shield, solo con mucho ruido electromagnético o distancias muy largas. *(Técnico, R2-2)*

### 3.3 Cable de control CMP sin shield y con shield

**U39.** De 22 a 16 AWG: CMP, CL3P, FPLP y FT6. En 14 y 12 AWG: solo CL3P y FPLP. PVC de baja emisión de humo y chaqueta de PVC para plenum. Con shield: lámina metálica sobre todos los conductores. *(F1; F2, págs. 10 y 11)*

**U40.** Se puede instalar en los mismos lugares que el FPLP (U22). *(F1)*

### 3.4 Cable multipar

**U41.** Tres construcciones *(F1; F2, págs. 12 y 15)*:
- **Multipar con shield general, plenum:** CMP, CL3P, FPLP, FT6. Lámina sobre todos los conductores.
- **1 par con shield, plenum:** CMP, CL3P, FPLP, FT6. Lámina sobre el par.
- **Multipar con shield en cada par, uso general:** CM y CL2, resistente a la luz solar, de −20 a 60 °C. Lámina sobre cada par.

**U42.** Los de plenum van donde va el FPLP (U22). El de uso general va en canalización metálica, en bandeja metálica con tapa, dentro de edificios fuera de espacios de aire y risers, y expuesto al sol. *(F1)*

**U43.** Usos típicos del multipar: circuitos de señal y de potencia limitada en sistemas de seguridad y control, como alarma de robo y control de acceso. *(F4: fichas "Security & Control Cable" de los dos multipares; F1: "signal and limited-power transmission applications"; F2, págs. 8, 12 y 15: sección de seguridad. Confirmado con las fichas el 28 de septiembre de 2026)* Queda P3 para saber si alguno se pide en los proyectos de Suplelec.

### 3.5 Cable de control de acceso (Profusion y compuesto)

**U44.** Reúne en un solo cable los cuatro circuitos de una puerta: lector de tarjeta, cerradura, contacto de puerta y botón de salida. *(F2, pág. 9; F5, ficha de control de acceso de Southwire: "puertas de control de acceso con cuatro funciones")*

**U45.** Componentes *(F2, pág. 19)*:

| Componente | Calibre y conductores | Shield en la versión estándar | Shield en la versión para ambientes ruidosos |
| --- | --- | --- | --- |
| Lector de tarjeta | 22 AWG, 6 conductores (3 pares en la versión para ambientes ruidosos) | Sí | Sí |
| Cerradura | 18 AWG, 4 conductores | No | Sí |
| Contacto de puerta | 22 AWG, 2 conductores | No | Sí |
| Botón de salida | 22 AWG, 4 conductores | No | Sí |

**U46.** **Profusion:** los cuatro cables van torcidos como una cuerda, sin chaqueta general ni cintas. **Compuesto:** una chaqueta cubre los cuatro, lo que facilita el jalado y las curvas. *(F2, págs. 9 y 18)*

**U47.** Plenum: CMP, CL3P, FPLP, FT6. Riser: CMR, CL3R, FPLR, FT4. Se instalan donde va el FPLP o el FPLR, respectivamente (U17 y U22). *(F1; F2, pág. 18)*

---

## 4. Aire acondicionado y automatización

**U48.** Sistemas que atienden: gestión de clima y energía en edificios, control de clima en casas, y sistemas centralizados, localizados y por zonas. *(F2, pág. 31)*

### 4.1 Cable BACnet MS/TP y RS-485, plenum

**U49.** Para redes de comunicación EIA-485 (RS-485), como BACnet MS/TP, en automatización de edificios. El RS-485 es siempre un bus de comunicación de alta velocidad. *(Técnico, respuesta a P4)* Baja capacitancia (12,5 pF por pie en cobre desnudo; unos 41 pF/m) para transmitir datos a distancias largas. *(F3; F2, pág. 40)*

**U50.** Clasificación CMP, FPLP, CL3P y FT6. Conductores de cobre desnudo o estañado, trenzados de 7 hilos (19 en 18 AWG), aislamiento FEP, lámina sobre todos los conductores, chaqueta de PVC para plenum. 300 V, de −20 a 75 °C. *(F3)*

**U51.** Se puede instalar: en ductos fabricados (300.22(B)); en otros espacios de aire (300.22(C)); en risers; dentro de edificios. *(F3; F1)*

**U52.** Viene en 1, 1,5 y 2 pares. El de 1,5 pares es un par (negro y blanco) más un conductor amarillo. *(F3)* El conductor amarillo es la referencia común de señal: evita diferencias de potencial de tierra entre controladores. *(Técnico, R3-1)*

**U53.** Datos eléctricos que se mostrarán en la tabla de variantes, porque son lo primero que preguntan los clientes de este cable (sugerencia del técnico). Capacitancia y resistencia de la ficha 2025, convertidas a metros *(F3)*; impedancia de las fichas por código *(F4)*:

| Variante | Capacitancia | Impedancia | Resistencia en DC a 20 °C |
| --- | --- | --- | --- |
| 24 AWG, 1 par | 41 pF/m (12,5 pF/pie) | 115 Ω | 87,6 Ω/km |
| 22 AWG, 1 par | 41 pF/m | 115 Ω | 55,4 Ω/km |
| 18 AWG, 1 par | 41 pF/m | 115 Ω | 21,9 Ω/km |
| 24 AWG, 1,5 pares | 41 pF/m | 115 Ω | 87,6 Ω/km |
| 22 AWG, 1,5 pares | 41 pF/m | 115 Ω | 55,4 Ω/km |
| 22 AWG, 2 pares | 41 pF/m | 115 Ω | 55,4 Ω/km |
| 22 AWG, 1 par, cobre estañado | 47,6 pF/m (14,5 pF/pie) | Sin dato | 55,4 Ω/km |

La impedancia (115 Ω nominales) solo aparece en las fichas de 2018; la de 2025 no la trae. **Técnico (R3-2):** se publica 115 Ω, porque los integradores la necesitan. La del cobre estañado queda vacía: su ficha no la trae.

### 4.2 Cable LonWorks y cable de comunicación Comm 3/4, plenum

**U54.** **LonWorks nivel 4, plenum:** CMP, CL3P, FPLP, FT6. Aislamiento FEP, baja capacitancia para distancias largas. Viene con o sin shield. *(F1; F2, pág. 41)*

**U55.** **Comunicación Comm 3/4, plenum:** impedancia y capacitancia diseñadas según la especificación de comunicación Comm 3/4 (de un fabricante de equipos de aire acondicionado). FPLP, CMP, FT6. Cobre estañado, aislamiento FEP, lámina sobre todos los conductores. *(F1; F2, pág. 41)*

**U56.** Ambos se instalan donde va el FPLP (U22). *(F1)*

### 4.3 Cable de termostato, uso general (estándar e híbrido)

**U57.** Clasificación CL2, resistente a la luz solar. 150 V. Aislamiento de polipropileno y chaqueta de PVC. *(F1; F2, pág. 37)*

**U58.** Se puede instalar: en canalización metálica según 300.22(B); sobre bandeja metálica con tapa; dentro de edificios, fuera de espacios de aire y de risers. *(F1; la ficha dice también "expuesto al sol": ver U7)* No va en risers ni en espacios de aire. *(Deducción de Claude, aprobada el 28 de septiembre de 2026)*

**U59.** Colores de los conductores, en orden: rojo, blanco, verde, azul, amarillo, café, naranja, negro, rosado, gris, canela y morado. *(F2, pág. 37)*

**U60.** **Termostato híbrido:** el conductor de alimentación es de 18 AWG y los demás de 20 AWG. Usa menos cobre y pesa menos; la caída de tensión es despreciable hasta 250 pies (unos 76 m). *(F2, pág. 34)*

### 4.4 Cable de termostato, plenum

**U61.** Clasificación CL2P (prueba de plenum NFPA 262). 150 V, de −20 a 75 °C según la ficha 2025 (60 °C según la página y el catálogo; ver la sección 6). PVC de baja emisión de humo y chaqueta de PVC para plenum. *(F1; F2, pág. 39)*

**U62.** Se puede instalar: en ductos fabricados (300.22(B)); en risers; dentro de edificios. *(F1)* La página de Southwire **no** menciona otros espacios de aire (300.22(C)), aunque es un cable plenum. **Técnico (R3-3):** sí va en cielos que funcionan como retorno de aire; la clasificación CL2P lo permite.

---

## 5. Audio

**U63.** Sistemas que atienden: salas de conferencias y reuniones, y audio de cine en casa. *(F2, pág. 50)*

### 5.1 Cable de audio Audacious, riser

**U64.** Conductores de cobre libre de oxígeno, con muchos hilos, para reducir la distorsión. *(F2, pág. 50; F1)* Chaqueta de PVC, resistente a la luz solar, 300 V, de −20 a 75 °C. *(F1; F2, pág. 51)*

**U65.** Se puede instalar en los mismos lugares que el FPLR (U17): risers, dentro de edificios, canalización metálica y expuesto al sol. *(F1)*

**U66.** Clasificación: la ficha 2025 y la página de Southwire dicen CMR y **CL2R**; el catálogo 2023 dice CMR y **CL3R**. **Técnico (R4-1):** se publica lo impreso en la chaqueta; mientras tanto queda CL2R, de la ficha 2025 (CL3R sustituye a CL2R).

### 5.2 Cable de audio Audacious, enterrado directo

**U67.** Clasificación CM y CL3, listado para enterrado directo y resistente a la luz solar. Cobre libre de oxígeno, 300 V, de −20 a 60 °C según la página y el catálogo (75 °C según la ficha 2025; ver la sección 6). *(F1; F2, pág. 52; F3)*

**U68.** Se puede instalar: enterrado, con tubería o sin ella; en exteriores expuestos al sol y a la humedad. *(F1)* Uso típico: parlantes de exteriores y jardines. *(F3 y F2, págs. 50 y 52: cable de audio y parlantes, listado para enterrar y para exteriores. Confirmado con las fichas el 28 de septiembre de 2026)*

### 5.3 Cable de sonido, riser (Home Theater)

**U69.** Conductores de cobre desnudo torcidos, que atenúan la interferencia electromagnética. *(F2, pág. 50)* Clasificación CMR, CL3R, FPLR y FT4, resistente a la luz solar. *(F1)*

**U70.** Temperatura máxima: la ficha 2025 y el catálogo 2023 dicen 75 °C; la página de Southwire dice 60 °C. *(Técnico, R4-2: 75 °C, sujeto a la chaqueta)*

**U71.** Se puede instalar en los mismos lugares que el FPLR (U17). *(F1)*

### 5.4 Afirmaciones generales (5 de octubre de 2026)

**U72.** El cable RS-485 sirve también para Modbus RTU, que usa el mismo bus RS-485 que BACnet MS/TP (U49). *(Técnico, 5-10-2026, confirmado por el usuario)*

**U73.** Los conductores de todos los cables de señal del catálogo son 100 % cobre: para señales no se usan aleaciones (como el aluminio recubierto de cobre), porque degradan la señal. *(Técnico, 5-10-2026, confirmado por el usuario)*

---

## 6. Diferencias entre fuentes

Cuando las fuentes no coinciden, manda la más nueva (F3, luego F1, sobre F2 y F4), sujeta a lo impreso en la chaqueta (R3-4, R4-1, R4-2). Así se resolvieron las temperaturas del termostato, el termostato plenum, el Audacious enterrado y el cable de sonido (75 °C), la clasificación del Audacious riser (CL2R) y el listado de comunicaciones de las familias FPLR y FPLP (CMR o CMP de 22 a 16 AWG, solo en la ficha 2025).

---

## 7. Líneas del catálogo que no están en las familias previstas

Genesis también vende en Latinoamérica un **cable paralelo (zip)** y un **cable torcido sin chaqueta** de uso general (CL2 y CM), y un **cable de tierra aislado** (CL2). Por ahora no se incluyen. Si el técnico cree que se piden, se agregan a la familia de robo.

---

<!-- solo-repo -->
## Decisiones del usuario

- **Trane y LonWorks (decidido el 27 de septiembre):** son marcas, pero también estándares, y se pueden nombrar. Como casi nadie pregunta por ellos: LonWorks se queda en el nombre del cable, porque es el protocolo y lo que identifica al cable (como BACnet). "Trane" no aparece en el sitio: ese cable se llama "cable de comunicación plenum con shield" y la especificación Comm 3/4 va solo en la fila de normas.
- **Las frases comerciales del catálogo** ("reduce hasta un 30 % el tiempo de cableado", "hasta 16 % menos material", "hasta 50 % menos costo que tubería y cable") no se usan en el sitio sin su aprobación.
- **Origen (decidido el 27 de septiembre):** se quitaron los 17 códigos de otro país, sin sello de EE. UU. o que ya no están en las fichas 2025: incendio armado MC de Genesis, mini split (bandeja y armado), FPLR de capacitancia media, control CMP 18/12 y cable sin chaqueta. Detalle en `docs/catalogo.md` §2.
<!-- /solo-repo -->
