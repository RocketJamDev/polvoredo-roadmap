# Travesía Polvoredo

Roadmap interactivo para preparar una travesía de varios días en primavera por las montañas que rodean Polvoredo (Burón, León), en el Parque Regional Montaña de Riaño y Mampodre, con fotografía de fauna.

34 habilidades en 6 niveles y 197 recursos verificados. Cada habilidad lleva una insignia de respaldo científico y, cuando hace falta, una nota de ética, ley o seguridad. El progreso se guarda en el navegador de cada persona (`localStorage`) y se puede exportar o importar como JSON desde el botón «Copia».

## Estructura

```
index.html        La web (un solo archivo, sin dependencias). Es lo que sirve GitHub Pages.
.nojekyll         Evita que GitHub Pages procese el sitio con Jekyll.
fuente/
  skills.py       Niveles, nombres y dependencias del árbol.
  research/*.py   Recursos y textos de cada habilidad, por bloques.
  template.html   Plantilla (CSS + JS); el JSON se inyecta en /*__DATA__*/.
  build.py        Valida los datos y genera ../index.html.
```

## Regenerar la web

Después de editar los datos o la plantilla:

```bash
cd fuente && python3 build.py
```

`build.py` falla si una habilidad no tiene entre 3 y 8 recursos, si un recurso no existe o sobra, si hay dependencias rotas o ciclos, o si hay URLs, tipos o dificultades inválidos.

## Publicar en GitHub Pages

```bash
git add .
git commit -m "Roadmap travesía Polvoredo"
gh repo create survival-roadmap --public --source . --push   # o crea el repo en github.com y haz git push
```

Luego en GitHub: **Settings → Pages → Build and deployment → Source: Deploy from a branch**, rama `main`, carpeta `/ (root)`. La web queda en `https://<usuario>.github.io/survival-roadmap/`.

> GitHub Pages en cuentas gratuitas exige que el repositorio sea público.

## Aviso

Esta guía no sustituye a la formación presencial ni al criterio en el terreno. Emergencias: **112**. Consulta la normativa vigente del parque (Casa del Parque Valdeburón, Lario) y la predicción de AEMET antes de salir.
