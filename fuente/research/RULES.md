# Reglas de investigación (roadmap travesía Polvoredo)

Contexto: dos principiantes (primos) harán una travesía de varios días en PRIMAVERA (abr–jun) por las montañas que rodean Polvoredo (Burón, León), Parque Regional Montaña de Riaño y Mampodre, junto a Picos de Europa. Pernocta mixta (vivac + refugios/pueblos). Objetivo: fotografía de vida salvaje. Público hispanohablante.

Reglas NO negociables:
1. Cero invención. Solo títulos, autores, URLs que hayas VISTO en WebSearch o WebFetch. Si no verificas algo, descártalo.
2. Si una fuente da 403/429/robots: NO la sortees con curl/python/espejos. Usa otras fuentes. Anota las fuentes bloqueadas.
3. YouTube: solo vídeos confirmados (título+canal vistos en resultados de búsqueda). No inventes IDs.
4. Prefiere: editoriales, universidades, organismos oficiales (Junta CyL, Parques Nacionales, AEMET, Guardia Civil, FEDME, Fundación Oso Pardo, SEO/BirdLife, MIDE), DOI/Semantic Scholar, librerías reconocidas (Casa del Libro, Desnivel, Todostuslibros), webs de autores.
5. Prioriza recursos EN ESPAÑOL cuando existan; añade algunos en inglés de calidad. Para libros en inglés busca si existe edición en español (título + URL de editorial/librería) y guárdala en es={...}.
6. Por habilidad: 3–8 recursos variados (libro, paper, articulo, blog, podcast, video, charla, curso, web, documental), dificultad 1/2/3, al menos uno introductorio (1) y uno académico/oficial cuando exista. Un mismo recurso puede servir a varias habilidades (reutiliza su id).
7. Insignia científica por habilidad: s sólido, p parcial, d en disputa, n sin respaldo + nota breve que lo justifique (1 frase).

FORMATO DE SALIDA: escribe un archivo Python en la ruta indicada con EXACTAMENTE esto:

```python
# recursos
RES = [
  # r(id, titulo, autor, tipo, idioma, url, por_que_vale, dificultad, es=None)
  ('id-corto', 'Título', 'Autor u organismo', 'libro', 'es', 'https://...', 'Por qué vale la pena (1 frase, en español).', 1, None),
  ('otro-id', 'Title', 'Author', 'libro', 'en', 'https://...', '...', 2, {'t':'Título en español','u':'https://...'}),
]
# habilidades
SKILLS = {
  'skill-id': dict(sci='s', sciNote='...', desc='Qué es y cómo se entrena (2-4 frases, concreto para esta travesía en primavera en Riaño/Polvoredo).', jane='Ejemplo concreto aplicado a la travesía (1-2 frases, ej. "En el collado X..."; solo hechos verificados sobre la zona, si no, un escenario práctico genérico sin inventar datos).', res=['id-corto','otro-id'], ethics=None),
}
BLOCKED = ['urls o dominios que no pudiste consultar']
```
Idiomas: 'es' o 'en'. Tipos válidos: libro, paper, articulo, blog, podcast, video, charla, curso, web, documental. ethics: cadena con nota ética/legal/seguridad o None.
Prefija los ids de recursos con tu bloque (p.ej. 'l0-') para evitar choques salvo que sea un recurso obvio compartido.
Al terminar, verifica que el archivo es Python válido (python3 -c "exec(open(...).read())") y responde con un resumen breve (nº recursos, fuentes bloqueadas, dudas).
