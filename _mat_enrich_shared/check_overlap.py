#!/usr/bin/env python3
"""check_overlap.py - Nebula Courses - puerta 6: rotulos que se pisan.

POR QUE EXISTE
--------------
El defecto de calidad mas frecuente del proyecto no lo detectaba
ninguna puerta: dos rotulos que se solapan, una etiqueta encima de una
curva, una cota que pisa el eje. Se cazaban MIRANDO el PNG, y mirar es
lo que mas cuesta -- las imagenes son el 84 % de lo que entra en el
contexto de un agente.

Este control busca ese mismo defecto **sin imagen**: extrae la caja de
cada palabra del PDF con `pdftotext -bbox` y marca las que se pisan
entre si. Cuesta una llamada de texto en vez de una pagina renderizada.

No sustituye a mirar: no ve una curva mal dibujada, ni una flecha que
apunta al sitio equivocado, ni un angulo que miente. Sustituye a mirar
PARA ESTO, que es lo que mas veces hacia falta.

Uso:
    python3 check_overlap.py leccion.pdf [--min-area 0.35] [--json]
Salida: JSON con las colisiones por pagina; codigo 1 si hay alguna.
"""
import json
import re
import subprocess
import sys
import tempfile
import os
import collections

# Dos palabras consecutivas de la misma linea casi se tocan por
# construccion; solo interesa el solape REAL de area.
MIN_AREA = 0.35          # fraccion de la caja menor cubierta por la otra
MIN_ALTO = 0.45          # y ademas tienen que compartir altura de verdad


def cajas(pdf):
    with tempfile.NamedTemporaryFile(suffix='.html', delete=False) as t:
        tmp = t.name
    try:
        subprocess.run(['pdftotext', '-bbox', pdf, tmp],
                       check=True, capture_output=True)
        html = open(tmp, encoding='utf-8', errors='replace').read()
    finally:
        if os.path.exists(tmp):
            os.remove(tmp)
    pag = 0
    out = collections.defaultdict(list)
    for m in re.finditer(r'<page |<word xMin="([\d.]+)" yMin="([\d.]+)" '
                         r'xMax="([\d.]+)" yMax="([\d.]+)">(.*?)</word>', html):
        if m.group(0).startswith('<page'):
            pag += 1
            continue
        x0, y0, x1, y1 = (float(m.group(i)) for i in range(1, 5))
        w = m.group(5)
        if not w.strip():
            continue
        out[pag].append((x0, y0, x1, y1, w))
    return out


import unicodedata

# ERR-0142 - LA TIPOGRAFIA MATEMATICA SE SOLAPA POR DISENO.
#   La primera version de esta puerta marco 2268 "colisiones" en 75
#   lecciones. Ninguna lo era: `\vec F` pone la flecha ENCIMA de la F,
#   un radical cubre su contenido, un exponente se monta sobre su base.
#   Publicarla asi habria obligado a los redactores a reescribir
#   matematica correcta para callarla -- el mismo error que ya costo
#   cuatro agentes con `check_content_loss`.
#
#   Una colision DE VERDAD es entre dos rotulos legibles. Asi que se
#   exige que las dos piezas sean palabras: tres caracteres o mas, con
#   letras, y sin signos matematicos ni marcas combinantes.
_MATH = set('√∫∑∏±×÷≈≤≥≠∞∂∇⃗̂̄˙⁄∠△∥⊥')


def _es_rotulo(w):
    """True si la pieza es una palabra legible y no un glifo matematico."""
    w = w.strip()
    if len(w) < 3:
        return False
    if any(c in _MATH for c in w):
        return False
    # marcas combinantes (acentos, flechas de vector) no son rotulos
    if any(unicodedata.combining(c) for c in w):
        return False
    letras = sum(c.isalpha() for c in w)
    return letras >= 3


def solapan(a, b):
    ax0, ay0, ax1, ay1, _ = a
    bx0, by0, bx1, by1, _ = b
    ix = min(ax1, bx1) - max(ax0, bx0)
    iy = min(ay1, by1) - max(ay0, by0)
    if ix <= 0 or iy <= 0:
        return 0.0
    inter = ix * iy
    menor = min((ax1 - ax0) * (ay1 - ay0), (bx1 - bx0) * (by1 - by0))
    if menor <= 0:
        return 0.0
    # exigir tambien solape vertical sustancial: si solo se rozan por el
    # borde superior son dos lineas seguidas, no una colision.
    alto = iy / min(ay1 - ay0, by1 - by0)
    return (inter / menor) if alto >= MIN_ALTO else 0.0


def audit(pdf, min_area=MIN_AREA):
    hits = []
    for pag, ws in cajas(pdf).items():
        ws.sort(key=lambda w: (w[1], w[0]))
        for i, a in enumerate(ws):
            # solo hace falta comparar con los que empiezan cerca en vertical
            for b in ws[i + 1:]:
                if b[1] > a[3]:
                    break
                if not (_es_rotulo(a[4]) and _es_rotulo(b[4])):
                    continue
                f = solapan(a, b)
                if f >= min_area:
                    hits.append({'pagina': pag, 'a': a[4], 'b': b[4],
                                 'solape': round(f, 2),
                                 'x': round(a[0]), 'y': round(a[1])})
    return {'pdf': os.path.basename(pdf), 'colisiones': len(hits),
            'verdict': 'OK' if not hits else 'OVERLAP',
            'detail': hits[:20]}


def main():
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    if not args:
        sys.exit(__doc__)
    ma = MIN_AREA
    for a in sys.argv[1:]:
        if a.startswith('--min-area'):
            ma = float(a.split('=')[1]) if '=' in a else ma
    r = audit(args[0], ma)
    print(json.dumps(r, ensure_ascii=False, indent=1))
    sys.exit(0 if r['colisiones'] == 0 else 1)


if __name__ == '__main__':
    main()
