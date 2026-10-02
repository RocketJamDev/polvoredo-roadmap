#!/usr/bin/env python3
"""Une la investigación, valida y genera el HTML final."""
import glob, json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from skills import LEVELS, TREE

OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, '..', 'index.html')
TYPES = {
    'libro': {'i': '📕', 'n': 'Libro'}, 'paper': {'i': '📄', 'n': 'Paper'},
    'articulo': {'i': '📰', 'n': 'Artículo'}, 'blog': {'i': '✍️', 'n': 'Blog'},
    'podcast': {'i': '🎧', 'n': 'Podcast'}, 'video': {'i': '🎬', 'n': 'Vídeo'},
    'charla': {'i': '🎤', 'n': 'Charla'}, 'curso': {'i': '🎓', 'n': 'Curso'},
    'web': {'i': '🌐', 'n': 'Web'}, 'documental': {'i': '🎞️', 'n': 'Documental'},
}
errors = []
def err(msg): errors.append(msg)

# --- cargar investigación ---
R, SK = {}, {}
for f in sorted(glob.glob(os.path.join(os.environ.get('RESEARCH_DIR', os.path.join(HERE, 'research')), '*.py'))):
    ns = {}
    exec(open(f, encoding='utf-8').read(), ns)
    for row in ns.get('RES', []):
        if len(row) != 9:
            err(f'{f}: fila con {len(row)} campos: {row[:2]}'); continue
        rid, t, a, ty, lang, url, why, dif, es = row
        rec = dict(t=t, a=a, ty=ty, l=lang, u=url, w=why, d=dif)
        if es: rec['es'] = es
        if rid in R and R[rid]['u'] != url:
            err(f'id duplicado con URL distinta: {rid}')
        R[rid] = rec
    for sid, d in ns.get('SKILLS', {}).items():
        if sid in SK: err(f'habilidad duplicada en research: {sid}')
        SK[sid] = d

# --- montar habilidades ---
skills, ids = [], {t[0] for t in TREE}
for sid, name, lvl, deps in TREE:
    d = SK.get(sid)
    if not d: err(f'sin contenido para habilidad {sid}'); continue
    skills.append(dict(id=sid, name=name, level=lvl, deps=deps, sci=d['sci'],
                       sciNote=d['sciNote'], desc=d['desc'], jane=d['jane'],
                       res=d['res'], ethics=d.get('ethics')))
for sid in SK:
    if sid not in ids: err(f'habilidad investigada que no está en el árbol: {sid}')

# --- validaciones ---
used = set()
for s in skills:
    n = len(s['res'])
    if not 3 <= n <= 8: err(f"{s['id']}: {n} recursos (debe ser 3-8)")
    if len(set(s['res'])) != n: err(f"{s['id']}: recursos repetidos")
    for rid in s['res']:
        if rid not in R: err(f"{s['id']}: recurso inexistente {rid}")
        used.add(rid)
    for dep in s['deps']:
        if dep not in ids: err(f"{s['id']}: dependencia inexistente {dep}")
    if s['sci'] not in 'spdn' or len(s['sci']) != 1: err(f"{s['id']}: insignia inválida")
for rid in set(R) - used: err(f'recurso sin usar: {rid}')
for rid, r in R.items():
    if not r['u'].startswith('http'): err(f'{rid}: URL inválida')
    if r['ty'] not in TYPES: err(f"{rid}: tipo inválido {r['ty']}")
    if r['d'] not in (1, 2, 3): err(f'{rid}: dificultad inválida')
    if r['l'] not in ('es', 'en'): err(f'{rid}: idioma inválido')
    if 'es' in r and not (r['es'].get('t') and r['es'].get('u', '').startswith('http')):
        err(f'{rid}: edición en español incompleta')

# acíclico (DFS)
graph = {s['id']: s['deps'] for s in skills}
state = {}
def visit(n, path):
    if state.get(n) == 1: err('ciclo: ' + ' -> '.join(path + [n])); return
    if state.get(n) == 2: return
    state[n] = 1
    for m in graph.get(n, []): visit(m, path + [n])
    state[n] = 2
for n in graph: visit(n, [])

if errors:
    print('\n'.join('✗ ' + e for e in errors)); sys.exit(1)

data = dict(initial=[], types=TYPES, levels=LEVELS, skills=skills, resources=R)
js = json.dumps(data, ensure_ascii=False, separators=(',', ':')).replace('</', '<\\/')
tpl = open(os.path.join(HERE, 'template.html'), encoding='utf-8').read()
assert '/*__DATA__*/' in tpl
open(OUT, 'w', encoding='utf-8').write(tpl.replace('/*__DATA__*/', js))
print(f'✓ {len(skills)} habilidades, {len(R)} recursos, '
      f"{sum('es' in r for r in R.values())} con edición en español → {OUT}")
