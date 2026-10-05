#!/usr/bin/env bash
# Hook SessionStart de cada proyecto (sitio o marketing). Lo que imprime entra al
# contexto de Claude al abrir la sesión: estado del núcleo, pedidos abiertos para
# este proyecto (solicitudes.md) y los últimos cambios del núcleo (CAMBIOS.md).
#
# Uso (desde .claude/settings.json del proyecto):
#   bash "$CLAUDE_PROJECT_DIR/nucleo/scripts/al-iniciar.sh" sitio
set -uo pipefail
proyecto=${1:?Falta el proyecto: sitio o marketing}
nucleo="$(cd "$(dirname "$0")/.." && pwd -P)"

echo "## Núcleo compartido (${nucleo})"

# Si el núcleo tiene remoto y está limpio, se pone al día (solo avance rápido).
if git -C "$nucleo" remote get-url origin >/dev/null 2>&1; then
  if [[ -z "$(git -C "$nucleo" status --porcelain)" ]]; then
    timeout 15 git -C "$nucleo" pull --ff-only -q 2>/dev/null || echo "- No se pudo actualizar el núcleo desde GitHub (sin red o con cambios divergentes)."
  fi
fi

pendientes=$(git -C "$nucleo" status --porcelain 2>/dev/null)
if [[ -n "$pendientes" ]]; then
  echo "- **Cambios del núcleo sin commit** (hacer commit en ~/suplelec-nucleo, con su línea en CAMBIOS.md):"
  sed 's/^/  /' <<<"$pendientes"
fi

echo
echo "### Solicitudes abiertas para ${proyecto} (nucleo/solicitudes.md)"
abiertas=$(awk -v p="$proyecto" '
  /^## / { en = ($0 ~ /^## Abiertas/) }
  en && /^\| S[0-9]+/ {
    n = split($0, c, "|")
    for (i = 2; i <= 6; i++) gsub(/^ +| +$/, "", c[i])
    if (c[4] ~ ("→ *" p "$")) print "- " c[2] " (" c[4] "): " c[5] ". Cuándo: " c[6] "."
  }' "$nucleo/solicitudes.md")
echo "${abiertas:-- Ninguna.}"

echo
echo "### Últimos cambios del núcleo (nucleo/CAMBIOS.md)"
grep -m 3 '^- ' "$nucleo/CAMBIOS.md" || echo "- Ninguno."
