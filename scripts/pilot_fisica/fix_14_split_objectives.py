# -*- coding: utf-8 -*-
"""
Fix de integridad referencial (Fase 7): la atomizacion (Fase 4) repartio
objectives[] entre las dos partes de cada leccion dividida, pero algunas
piezas de practica de la Parte A referencian un objective_id que quedo en
la Parte B (y viceversa). La causa: el reparto de piezas de practica se
hizo por solapamiento de concept_ids con los theory_blocks de cada parte,
mientras que el reparto de objectives[] se hizo con un criterio distinto;
ambos criterios no siempre coinciden pieza a pieza.

Solucion: cada pareja de partes recibe la UNION completa de los objectives
originales (en vez de un subconjunto exclusivo). Es una duplicacion
minuscula (una lista de una o dos frases por objetivo, no contenido
explicativo), y resuelve el 100% de las referencias rotas sin tocar ninguna
pieza de practica ni inventar nada.
"""
import json, os

BASE = os.path.expanduser("~/mnt/Nebula_Cursos_Web")
PILOT = os.path.join(BASE, "pilot/selectividad_fisica_v2")

PAIRS = [
    ("electromagnetismo", "05a_El_potencial_eléctrico_definición_y_energía.json", "05b_El_potencial_eléctrico_superficies_equipotenciales_y_signos.json"),
    ("ondas", "11a_Ondas_estacionarias_qué_son_y_dónde_están_los_nodos.json", "11b_Ondas_estacionarias_energía_y_errores_frecuentes.json"),
    ("optica", "03a_El_ángulo_límite_y_la_reflexión_total.json", "03b_Decidir_la_reflexión_total_y_el_ángulo_de_Brewster.json"),
    ("ondas", "05a_Diferencia_de_fase_puntos_en_fase_y_en_oposición.json", "05b_Diferencia_de_fase_el_procedimiento_y_sus_trampas.json"),
    ("campo_gravitatorio", "02a_La_ley_de_gravitación_universal_enunciado.json", "02b_La_ley_de_gravitación_universal_aplicaciones.json"),
    ("cuantica", "06a_Indeterminación_el_principio_y_el_final_de_la_trayectoria.json", "06b_La_nueva_mecánica_cuántica_Schrödinger_y_Born.json"),
]

for unit, bkey_a, bkey_b in PAIRS:
    fp = os.path.join(PILOT, f"selectividad_fisica__{unit}.json")
    d = json.load(open(fp, encoding="utf-8"))
    la = d[bkey_a]
    lb = d[bkey_b]
    union = []
    seen_ids = set()
    for o in la.get("objectives", []) + lb.get("objectives", []):
        oid = o.get("id")
        if oid not in seen_ids:
            seen_ids.add(oid)
            union.append(o)
    la["objectives"] = union
    lb["objectives"] = union
    json.dump(d, open(fp, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print(f"{unit}: {bkey_a} y {bkey_b} -> {len(union)} objectives (union) en ambas partes")

print("\nRegenerando schema_v2 para reflejar los objectives unificados...")
