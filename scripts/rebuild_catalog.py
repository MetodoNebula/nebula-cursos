#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
rebuild_catalog.py - Recalcula los recuentos de catalog.json (navegacion de
TODOS los cursos) desde los bundles actuales, PRESERVANDO la estructura
{"projects":[...]}. Nunca lo reemplaza por un resumen de un solo curso.

Por que existe: catalog.json es un recurso COMPARTIDO (los 9 cursos). Varias
sesiones/trabajos escriben sobre el. Si alguna lo deja como {"units","totals"}
de un unico curso, la web deja de cargar ("No se pudo cargar el catalogo") y,
si se cifra asi, tumba el sitio publicado.

Auto-reparador:
  - Si catalog.json es valido ({projects:[...]}) -> se usa como estructura y se
    refresca scripts/catalog.base.json (copia de seguridad de la estructura).
  - Si catalog.json esta roto -> se reconstruye desde scripts/catalog.base.json.
Luego se recalculan los recuentos (contenido por leccion y total por curso)
leyendo los bundles, y se escribe catalog.json de forma atomica.

Uso:  python3 scripts/rebuild_catalog.py
"""
import json, os, sys, collections, tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)                      # .../Nebula_Cursos_Web
CATALOG = os.path.join(ROOT, 'catalog.json')
BASE = os.path.join(HERE, 'catalog.base.json')    # estructura de confianza


def is_projects(cat):
    return isinstance(cat, dict) and isinstance(cat.get('projects'), list) and cat['projects'] \
        and all(isinstance(p, dict) and p.get('key') and isinstance(p.get('units'), list) for p in cat['projects'])


def load_structure():
    cur = None
    try:
        cur = json.load(open(CATALOG, encoding='utf-8'))
    except Exception as e:
        print('  catalog.json no legible (%s)' % e)
    if is_projects(cur):
        print('  catalog.json valido: uso su estructura y refresco la base.')
        json.dump(cur, open(BASE, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
        return cur
    print('  catalog.json ROTO o ausente -> reconstruyo desde scripts/catalog.base.json')
    if not os.path.exists(BASE):
        sys.exit('ERROR: no hay scripts/catalog.base.json para reconstruir. Aborto.')
    base = json.load(open(BASE, encoding='utf-8'))
    if not is_projects(base):
        sys.exit('ERROR: scripts/catalog.base.json tampoco es {projects:[...]}. Aborto.')
    return base


def main():
    print('rebuild_catalog: ROOT=%s' % ROOT)
    cat = load_structure()
    bcache = {}
    def bundle(rel):
        if rel not in bcache:
            bcache[rel] = json.load(open(os.path.join(ROOT, rel), encoding='utf-8'))
        return bcache[rel]

    warns = 0
    for p in cat['projects']:
        tot = collections.OrderedDict((k, 0) for k in p.get('total', {}).get('por_tipo', {}))
        nlec = 0
        for u in p['units']:
            for l in u.get('lecciones', []):
                nlec += 1
                rel, bkey = l.get('bundle'), l.get('bkey')
                bl = None
                try:
                    bl = bundle(rel).get(bkey)
                except Exception:
                    bl = None
                if bl is None:
                    warns += 1
                    print('  AVISO: no encuentro %s :: %s -> mantengo contenido previo' % (rel, bkey))
                    for k, v in (l.get('contenido') or {}).items():
                        tot[k] = tot.get(k, 0) + v
                    continue
                newc = collections.OrderedDict()
                fields = list(l.get('contenido', {}).keys()) or [
                    'objectives','prerequisites','diagnostic_items','theory_blocks','keywords',
                    'worked_examples','guided_exercises','exercises','exam_questions',
                    'challenge_questions','mcq','flashcards','misconceptions','common_mistakes',
                    'exam_notes','summary','curriculum']
                for f in fields:
                    v = bl.get(f)
                    newc[f] = len(v) if isinstance(v, list) else (0 if v is None else 1)
                l['contenido'] = newc
                for k, v in newc.items():
                    tot[k] = tot.get(k, 0) + v
        p.setdefault('total', {})
        p['total']['por_tipo'] = tot
        p['total']['piezas'] = sum(tot.values())
        p['total']['lecciones'] = nlec

    out = json.dumps(cat, ensure_ascii=False, indent=1)
    json.loads(out)  # valida
    fd, tmp = tempfile.mkstemp(dir=ROOT, suffix='.tmp')
    os.close(fd); open(tmp, 'w', encoding='utf-8').write(out); os.replace(tmp, CATALOG)
    # mantiene la base sincronizada con lo bueno recien escrito
    json.dump(cat, open(BASE, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print('OK: catalog.json reescrito. %d cursos, %d avisos.' % (len(cat['projects']), warns))
    for p in cat['projects']:
        print('   %-30s lecciones=%-4d exercises=%-5d piezas=%d' % (
            p['key'], p['total']['lecciones'], p['total']['por_tipo'].get('exercises', 0), p['total']['piezas']))


if __name__ == '__main__':
    main()
