#!/usr/bin/env python3
"""Revisa textos públicos de Suplelec contra nucleo/reglas/reglas.toml.

Uso:
  python3 nucleo/reglas/revisar.py <archivo>...    revisa archivos; sale con 1 si algo bloquea
  echo "texto" | python3 nucleo/reglas/revisar.py -
  python3 nucleo/reglas/revisar.py --hook <patrón>...
      Hook PostToolUse de Claude Code (Write|Edit). Lee el evento por la entrada
      estándar y revisa el archivo escrito si su ruta, relativa al proyecto, calza
      con algún patrón ('contenido/**/*.html'). Si hay hallazgos se los devuelve a
      Claude (código 2) para que los corrija o los consulte con el usuario.

Solo usa la biblioteca estándar (Python 3.13 o más nuevo).
"""
import json
import os
import re
import sys
import tomllib
from pathlib import Path, PurePosixPath

REGLAS = Path(__file__).with_name('reglas.toml')
EXTENSIONES = {'.md', '.html', '.htm', '.txt', '.csv'}

# Lo que se quita antes de revisar. Se cambia por espacios del mismo largo para
# conservar las líneas y las columnas.
QUITAR = [
    re.compile(r'<!--.*?-->', re.S),                        # comentarios (encabezados internos, bloques de WordPress)
    re.compile(r'<(script|style)\b.*?</\1>', re.S | re.I),
    re.compile(r'<[^>]+>'),                                 # etiquetas y sus atributos
    re.compile(r'\]\([^)]*\)'),                             # destino de enlaces de Markdown
    re.compile(r'\b(?:https?://|www\.|wa\.me/|mailto:|tel:)\S+'),
    re.compile(r'\+?506[\s-]?\d{4}[\s-]?\d{4}'),            # teléfonos de Costa Rica
    re.compile(r'\b\d{4}-\d{4}\b'),
    re.compile(r'San José,? \d{5}'),                        # código postal de la dirección
]
EMOJI = re.compile('[\U0001F300-\U0001FAFF☀-➿⭐⭕]')


def cargar_reglas() -> tuple[list[dict], int]:
    datos = tomllib.loads(REGLAS.read_text(encoding='utf-8'))
    reglas = []
    for r in datos['regla']:
        reglas.append({**r, 're': re.compile(r['patron'])})
    return reglas, int(datos.get('max_emojis', 3))


def limpiar(texto: str) -> str:
    for patron in QUITAR:
        texto = patron.sub(lambda m: re.sub(r'[^\n]', ' ', m.group(0)), texto)
    return texto


def revisar_texto(texto: str, reglas: list[dict], max_emojis: int) -> list[tuple[int, str, str, str, str]]:
    """Devuelve (línea, nivel, id, fragmento, motivo) por cada hallazgo."""
    hallazgos = []
    limpio = limpiar(texto)
    for n, linea in enumerate(limpio.splitlines(), 1):
        for r in reglas:
            for m in r['re'].finditer(linea):
                hallazgos.append((n, r['nivel'], r['id'], m.group(0).strip(), r['motivo']))
    emojis = len(EMOJI.findall(limpio))
    if emojis > max_emojis:
        hallazgos.append((0, 'revisar', 'emojis', f'{emojis} emojis', f'Más de {max_emojis}: con mesura y nunca en títulos.'))
    return hallazgos


def formatear(nombre: str, hallazgos) -> str:
    return '\n'.join(
        f'{nombre}:{linea}: [{nivel}] {id_}: «{fragmento}» — {motivo}'
        for linea, nivel, id_, fragmento, motivo in hallazgos
    )


def modo_hook(patrones: list[str]) -> int:
    evento = json.load(sys.stdin)
    ruta = (evento.get('tool_input') or {}).get('file_path')
    if not ruta:
        return 0
    proyecto = Path(os.environ.get('CLAUDE_PROJECT_DIR') or evento.get('cwd') or '.').resolve()
    archivo = Path(ruta)
    if not archivo.is_absolute():
        archivo = proyecto / archivo
    try:
        relativa = PurePosixPath(archivo.relative_to(proyecto).as_posix())
    except ValueError:
        return 0
    if archivo.suffix.lower() not in EXTENSIONES or not any(relativa.full_match(p) for p in patrones):
        return 0
    if not archivo.exists():
        return 0
    reglas, max_emojis = cargar_reglas()
    hallazgos = revisar_texto(archivo.read_text(encoding='utf-8', errors='replace'), reglas, max_emojis)
    if not hallazgos:
        return 0
    print('Reglas de Suplelec (nucleo/reglas/reglas.toml). Corrija lo que dice "bloquea"; '
          'lo que dice "revisar" consúltelo con el usuario si no es claro:', file=sys.stderr)
    print(formatear(str(relativa), hallazgos), file=sys.stderr)
    return 2


def main(argumentos: list[str]) -> int:
    if argumentos[:1] == ['--hook']:
        return modo_hook(argumentos[1:])
    if not argumentos:
        print(__doc__.strip())
        return 1
    reglas, max_emojis = cargar_reglas()
    bloquea = False
    for nombre in argumentos:
        texto = sys.stdin.read() if nombre == '-' else Path(nombre).read_text(encoding='utf-8', errors='replace')
        hallazgos = revisar_texto(texto, reglas, max_emojis)
        if hallazgos:
            print(formatear(nombre, hallazgos))
        bloquea |= any(h[1] == 'bloquea' for h in hallazgos)
    return 1 if bloquea else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
