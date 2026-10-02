# recursos
RES = [
  # r(id, titulo, autor, tipo, idioma, url, por_que_vale, dificultad, es=None)
  # --- zona ---
  ('l0-pr-riano', 'Parque Regional Montaña de Riaño y Mampodre', 'Fundación Patrimonio Natural de Castilla y León', 'web', 'es', 'https://patrimonionatural.org/espacios-naturales/parque-regional/parque-regional-montana-de-riano-y-mampodre', 'Ficha oficial del parque: 101.336 ha, cumbres como Coriscao (2.234 m) y Peña Ten, fauna (rebeco, lobo, oso ocasional, urogallo) y figuras de protección.', 1, None),
  ('l0-cp-valdeburon', 'Casa del Parque "Valdeburón"', 'Fundación Patrimonio Natural de Castilla y León', 'web', 'es', 'https://patrimonionatural.org/casas-del-parque/casas-del-parque/casa-del-parque-de-picos-de-europa-sector-oriental-valdeburon', 'Centro de visitantes en Lario (Ctra. Polvoredo s/n, Burón), con exposición sobre ecosistemas del valle a las cumbres, contacto y horarios oficiales.', 1, None),
  ('l0-porn-picos', 'Decreto 9/1994, de 20 de enero, por el que se aprueba el Plan de Ordenación de los Recursos Naturales de Picos de Europa', 'Junta de Castilla y León', 'web', 'es', 'https://medioambiente.jcyl.es/web/jcyl/binarios/1002/394/PORN%20Picos%20de%20Europa%20(1).pdf?blobheader=application%2Fpdf%3Bcharset%3DUTF-8&blobnocache=true', 'Texto legal del PORN que sigue regulando usos en el actual Parque Regional (antes "Picos de Europa en CyL"); el PRUG del parque está aún en tramitación.', 3, None),
  ('l0-ley-parque', 'Ley 12/1994, de 18 de julio, de Declaración del Parque Regional de Picos de Europa, en Castilla y León', 'BOE / Cortes de Castilla y León', 'web', 'es', 'https://www.boe.es/buscar/act.php?id=BOE-A-1994-18883', 'Ley de declaración del parque (renombrado Montaña de Riaño y Mampodre en 2019), base de su zonificación y régimen de protección.', 3, None),
  ('l0-picos-normas', 'Picos de Europa: normas de visita y recomendaciones', 'MITECO - Organismo Autónomo Parques Nacionales', 'web', 'es', 'https://www.miteco.gob.es/en/parques-nacionales-oapn/red-parques-nacionales/parques-nacionales/picos-europa/guia-visitante/normas-recomendaciones.html', 'Normas oficiales del Parque Nacional colindante; imprescindible si la travesía entra en Picos (vivac solo por encima de 1.800 m según el nuevo PRUG, Decreto 17/2025 en CyL).', 1, None),
  ('l0-cnig-mtn25', 'Mapa Topográfico Nacional 1:25.000 (MTN25)', 'Centro Nacional de Información Geográfica (IGN)', 'web', 'es', 'https://centrodedescargas.cnig.es/CentroDescargas/mapa-topografico-nacional', 'Cartografía oficial gratuita (CC-BY 4.0) descargable para planificar y llevar en papel o GPS las hojas de Burón, Riaño y Mampodre.', 2, None),
  ('l0-mide', 'MIDE. Método de Información de Excursiones', 'FEDME', 'web', 'es', 'https://misendafedme.es/mide/', 'Sistema oficial español para valorar severidad, orientación, desplazamiento y esfuerzo de una ruta antes de elegirla.', 1, None),
  # --- forma ---
  ('l0-ms-entrenar', 'Entrenar para la montaña', 'Montaña Segura', 'articulo', 'es', 'https://montanasegura.com/entrenar-para-la-montana/', 'Guía práctica para principiantes: fuerza excéntrica para bajadas, resistencia, propiocepción y entrenar con mochila cargada.', 1, None),
  ('l0-uphill', 'Entrenamiento para atletas de montaña', 'Kilian Jornet, Steve House, Scott Johnston (Ediciones Desnivel)', 'libro', 'es', 'https://www.desnivel.com/librosdesnivel/entrenamiento-para-atletas-de-montana/', 'Manual de referencia sobre fisiología y planificación de resistencia aeróbica y fuerza específica para montaña.', 3, None),
  ('l0-new-alpinism', 'Training for the New Alpinism', 'Steve House, Scott Johnston (Patagonia)', 'libro', 'en', 'https://uphillathlete.com/product/training-for-the-new-alpinism-book/', 'Clásico sobre construir base aeróbica y fuerza; útil para entender la progresión aunque está orientado a alpinismo.', 3, {'t': 'Entrenamiento para el nuevo alpinismo (Ediciones Desnivel, 2017)', 'u': 'https://www.libreriadesnivel.com/libros/entrenamiento-para-el-nuevo-alpinismo/9788498293975/'}),
  ('l0-knapik', 'Soldier load carriage: historical, physiological, biomechanical, and medical aspects', 'Joseph J. Knapik, Katy L. Reynolds, Everett Harman (Military Medicine, 2004)', 'paper', 'en', 'https://pubmed.ncbi.nlm.nih.gov/14964502/', 'Revisión científica de referencia sobre efectos fisiológicos y lesiones al cargar mochila, y cómo el entrenamiento con carga los reduce.', 3, None),
  ('l0-ms-autosuf', 'Travesías en verano en autosuficiencia', 'Montaña Segura', 'articulo', 'es', 'https://montanasegura.com/travesias-en-verano-en-autosuficiencia/', 'Guía de travesías de varios días cargando todo: planificación, mochila (~45 L mínimo), material de vivac, preparación física y cuidado de pies.', 2, None),
  # --- equipo ---
  ('l0-fedme-equipo', 'Senderismo: llevar equipamiento adecuado', 'FEDME', 'web', 'es', 'https://fedme.es/senderismo-pg05/', 'Recomendaciones federativas sobre sistema de tres capas, mochila, protección solar y extras imprescindibles.', 1, None),
  ('l0-ms-refugios', 'Travesías en verano entre refugios', 'Montaña Segura', 'articulo', 'es', 'https://montanasegura.com/travesias-en-verano-entre-refugios/', 'Lista de material y criterio de ligereza para travesías de refugio en refugio (mochila de ~40 L), complementaria a la de autosuficiencia.', 1, None),
  ('l0-ms-podcast', 'Vestimenta y equipo a la mochila para una excursión segura (Montaña Segura en diez minutos)', 'Montaña Segura', 'podcast', 'es', 'https://podcasts.apple.com/us/podcast/vestimenta-y-equipo-a-la-mochila-para-una-excursi%C3%B3n/id1699543208?i=1000622633167', 'Episodio de 13 min sobre calzado, abrigo, impermeable, mapa y teléfono: el "paso 2" de una salida segura.', 1, None),
  ('l0-desnivel-trekking', 'Material de trekking imprescindible: del nivel principiante al experto', 'Desnivel.com', 'articulo', 'es', 'https://www.desnivel.com/material/material-de-trekking-imprescindible-del-nivel-principiante-al-experto/', 'Repaso por niveles del material de trekking de la revista de montaña de referencia en España.', 1, None),
  # --- meteo ---
  ('l0-aemet-picos', 'Predicción de montaña: Picos de Europa (Cordillera Cantábrica de León)', 'AEMET', 'web', 'es', 'https://www.aemet.es/es/eltiempo/prediccion/montana?p=peu1', 'Predicción oficial diaria por zonas (incluida "Cordillera Cantábrica de León"): cielo, precipitación, tormentas, viento en altura, sensación térmica e isotermas de 0 y -10 °C.', 1, None),
  ('l0-aemet-bpa', 'Boletín de información nivológica y de peligro de aludes: Picos de Europa', 'AEMET', 'web', 'es', 'https://www.aemet.es/documentos/es/eltiempo/prediccion/montana/boletin_peligro_aludes/BPA_PN_Picos_Europa.pdf', 'Boletín oficial de nieve y aludes; clave en abril-mayo, cuando puede quedar nieve tardía en collados y laderas norte.', 2, None),
  ('l0-aemet-servicios', 'Servicios meteorológicos para la montaña', 'AEMET', 'web', 'es', 'https://www.aemet.es/en/conocermas/montana/detalles/serv_meteo', 'Explica qué productos de montaña publica AEMET y cómo interpretarlos.', 2, None),
  ('l0-ms-tormentas', 'Tormentas de evolución', 'Montaña Segura', 'articulo', 'es', 'https://montanasegura.com/tormentas-de-evolucion/', 'Cómo reconocer el crecimiento de cúmulos a cumulonimbos, por qué estallan a partir de mediodía y qué hacer si te pilla en cresta o cima.', 1, None),
  ('l0-colorado-meteo', 'Meteorología. Cómo prever el tiempo en montaña', 'Joaquín Colorado (Ediciones Desnivel)', 'libro', 'es', 'https://www.desnivel.com/librosdesnivel/meteorologia-como-prever-el-tiempo-en-montana/', 'Manual de bolsillo para interpretar nubes, frentes y predicciones antes y durante la actividad.', 2, None),
  ('l0-pons-meteo', 'Tiempo y clima en montaña. Manual práctico sobre meteorología', 'Jordi Pons Otálora (Ediciones Desnivel)', 'libro', 'es', 'https://www.desnivel.com/librosdesnivel/tiempo-y-clima-en-montana-manual-practico-sobre-meteorologia/', 'Enseña a leer señales de nubes y tipos de tormenta usando la propia montaña como campo de prácticas.', 2, None),
  # --- etica ---
  ('l0-lnt-es', 'No dejes rastro: educación en ética al aire libre y los 7 principios', 'Leave No Trace Center for Outdoor Ethics', 'web', 'es', 'https://es.lnt.org/', 'Sitio oficial en español de Leave No Trace, con los 7 principios y cursos online gratuitos.', 1, None),
  ('l0-lnt-7', 'The 7 Principles', 'Leave No Trace Center for Outdoor Ethics', 'web', 'en', 'https://lnt.org/why/7-principles/', 'Versión de referencia de los 7 principios con explicación ampliada de cada uno.', 1, None),
  ('l0-buenas-practicas-fauna', 'Buenas prácticas para la observación de oso pardo, lobo y lince en España', 'Ministerio / Plan Sectorial de Turismo de Naturaleza (2015), alojado por Alto Narcea Muniellos', 'web', 'es', 'https://www.altonarceamuniellos.org/sites/default/files/altonarcea/DOCUMENTOS%20INTERES/Manual_Buenas_Practicas_Observacion.pdf', 'Manual oficial: pasar desapercibido, no difundir ubicaciones en redes, no acercarse a crías ni oseras; directamente aplicable a fotografiar fauna en la zona osera.', 2, None),
  # --- botiquin ---
  ('l0-ms-botiquin', 'Botiquín', 'Montaña Segura', 'articulo', 'es', 'https://montanasegura.com/botiquin/', 'Lista concreta y ligera de botiquín de montaña (analgésicos, curas, manta térmica por grupo) pensada para el monte.', 1, None),
  ('l0-cruzroja-curso', 'Curso Online de Primeros Auxilios Básicos', 'Cruz Roja Española', 'curso', 'es', 'https://www.cruzroja.es/principal/web/formacion/curso-online-de-primeros-auxilios-basicos', 'Curso oficial de 20 h en campus virtual con certificado de Cruz Roja; base para saber actuar antes de que llegue el rescate.', 1, None),
  ('l0-subirats-pa', 'Primeros auxilios en montaña', 'Enric Subirats Bayego (Ediciones Desnivel)', 'libro', 'es', 'https://www.libreriadesnivel.com/libros/primeros-auxilios-en-montana/9788498292312/', 'Manual claro e ilustrado de un médico de montaña, centrado en lesiones y situaciones típicas del medio natural.', 2, None),
  ('l0-subirats-med', 'Manual de medicina de montaña', 'Enric Subirats Bayego (Ediciones Desnivel)', 'libro', 'es', 'https://www.desnivel.com/librosdesnivel/manual-de-medicina-de-montana/', 'Referencia basada en la evidencia para profundizar (hipotermia, traumatismos, evacuación); nivel avanzado.', 3, None),
  # --- foto-base ---
  ('l0-cta-triangulo', 'El triángulo de exposición en fotografía', 'Capture the Atlas', 'blog', 'es', 'https://capturetheatlas.com/es/triangulo-de-exposicion-explicado-fotografia/', 'Explicación visual y clara de apertura, velocidad e ISO y cómo compensarlos entre sí.', 1, None),
  ('l0-roger-benito', 'TRIANGULO de EXPOSICIÓN ¿cómo utilizar el modo manual de nuestra cámara?', 'Roger Benito', 'video', 'es', 'https://www.youtube.com/watch?v=-ZM3ZRIY-Vk', 'Vídeo en español que lleva el triángulo de exposición directamente al uso del modo manual.', 1, None),
  ('l0-xataka-af', 'Curso de Fotografía: 20. Modos de Autofocus', 'Xataka Foto', 'articulo', 'es', 'https://www.xatakafoto.com/curso-de-fotografia/curso-de-fotografia-20-modos-de-autofocus', 'Lección de un curso gratuito sobre AF-S, AF-C y áreas de enfoque; el AF continuo es la base para fauna en movimiento.', 1, None),
  ('l0-peterson', 'Understanding Exposure', 'Bryan Peterson (Penguin Random House)', 'libro', 'en', 'https://www.penguinrandomhouse.com/books/248820/understanding-exposure-fourth-edition-by-bryan-peterson/', 'El libro clásico para entender la exposición con ejemplos prácticos (contraluz, poca luz, sujetos en movimiento).', 2, {'t': 'Los secretos de la exposición fotográfica (Ediciones Tutor)', 'u': 'https://amazon.com/secretos-exposicion-fotografica-Understanding-Exposure/dp/8479028793'}),
  ('l0-freeman', 'El ojo del fotógrafo. Composición y diseño para crear mejores fotografías digitales', 'Michael Freeman (Blume)', 'libro', 'es', 'https://www.casadellibro.com/libro-el-ojo-del-fotografo-composicion-y-diseno-para-crear-mejores-fot-ografias-digitales/9788480768436/1248410', 'Referencia sobre composición: encuadre, elementos gráficos, luz y color, explicados con diagramas.', 2, None),
  ('l0-wolfe-gardner', 'Manual básico de fotografía al aire libre', 'Art Wolfe, Mark Gardner (Ediciones Desnivel)', 'libro', 'es', 'https://www.desnivel.com/librosdesnivel/manual-basico-de-fotografia-al-aire-libre/', 'Guía de campo sobre exposición, composición, acercamiento a vida salvaje y cuidado del equipo en viaje.', 1, None),
]
# habilidades
SKILLS = {
  'zona': dict(
    sci='s',
    sciNote='Información de organismos oficiales (Patrimonio Natural CyL, BOE, MITECO, IGN); la normativa del Parque Regional depende aún de un PORN de 1994 y un PRUG en tramitación.',
    desc='Conocer la geografía (cabeceras del Esla, Porma y Cea; cumbres de más de 2.000 m como Coriscao o Peña Ten), la fauna y la normativa del Parque Regional y del Parque Nacional colindante. Se entrena leyendo la ficha oficial, estudiando las hojas MTN25 de la zona, valorando rutas con el MIDE y visitando la Casa del Parque antes de salir.',
    jane='La Casa del Parque "Valdeburón" está en Lario, en la carretera de Polvoredo (Burón): una parada el primer día para confirmar normativa, estado de los caminos y avistamientos recientes. Si la ruta entra en el Parque Nacional de Picos, el vivac solo es legal por encima de 1.800 m, sin tienda y un máximo de 3 noches.',
    res=['l0-pr-riano', 'l0-cp-valdeburon', 'l0-cnig-mtn25', 'l0-mide', 'l0-picos-normas', 'l0-porn-picos', 'l0-ley-parque'],
    ethics='Antes de vivaquear o acampar en el Parque Regional hay que consultar con la Casa del Parque o con la Junta, porque la normativa del Parque Nacional (Decreto 17/2025, art. 51) no se aplica automáticamente al Regional y el PRUG del Regional aún se está tramitando.'),
  'forma': dict(
    sci='s',
    sciNote='Hay revisiones científicas sólidas sobre transporte de carga y entrenamiento (Knapik et al.); los planes concretos para principiantes son guías prácticas, no ensayos.',
    desc='Construir base aeróbica, fuerza excéntrica para las bajadas y equilibrio, y sobre todo acostumbrar el cuerpo a caminar varias horas seguidas con la mochila cargada. Para dos principiantes conviene empezar 8-12 semanas antes, haciendo salidas de fin de semana con desnivel y aumentando poco a poco el peso de la mochila.',
    jane='Escenario práctico: en las semanas previas, encadenar dos días seguidos de 5-6 h con 800-1.000 m de desnivel y la mochila de la travesía, para comprobar ampollas, rozaduras y ritmo real antes de ir a Polvoredo.',
    res=['l0-ms-entrenar', 'l0-ms-autosuf', 'l0-uphill', 'l0-new-alpinism', 'l0-knapik', 'l0-mide'],
    ethics=None),
  'equipo': dict(
    sci='p',
    sciNote='El sistema de capas y las listas de material son consenso de federaciones y expertos, basados en experiencia más que en estudios controlados.',
    desc='Aprender el sistema de tres capas (interior transpirable, aislante y exterior impermeable), elegir calzado probado y una mochila del volumen adecuado (unos 40 L entre refugios, 45 L o más en autosuficiencia) y ajustar la lista de material al vivac primaveral. Se entrena haciendo una lista, pesándolo todo y probándolo en salidas cortas.',
    jane='Escenario práctico: en primavera puede amanecer helando en un collado y hacer calor a media mañana en el valle; llevar las capas a mano para quitar y poner sin parar mucho, y un saco de dormir válido para temperaturas bajo cero en el vivac.',
    res=['l0-fedme-equipo', 'l0-ms-refugios', 'l0-ms-autosuf', 'l0-ms-podcast', 'l0-desnivel-trekking'],
    ethics=None),
  'meteo': dict(
    sci='s',
    sciNote='Basada en predicciones oficiales de AEMET y en física atmosférica bien establecida (convección, isotermas).',
    desc='Consultar a diario la predicción de montaña de AEMET para la Cordillera Cantábrica de León (tormentas, viento en altura, isoterma de 0 °C) y el boletín de nieve y aludes mientras quede nieve. En primavera hay que vigilar dos riesgos: las tormentas que crecen a partir de mediodía y la nieve que queda tarde en laderas norte y collados.',
    jane='Escenario práctico: si AEMET anuncia tormentas por la tarde, salir de madrugada, estar fuera de cimas y crestas al mediodía y tener pensado de antemano un descenso a Polvoredo o a otro pueblo.',
    res=['l0-aemet-picos', 'l0-aemet-bpa', 'l0-aemet-servicios', 'l0-ms-tormentas', 'l0-colorado-meteo', 'l0-pons-meteo'],
    ethics='Seguridad: con nieve dura de primavera en pendientes, sin crampones ni piolet ni formación, la decisión correcta es dar la vuelta.'),
  'etica': dict(
    sci='p',
    sciNote='Los 7 principios de Leave No Trace se apoyan en investigación sobre impacto recreativo, aunque algunos detalles varían según el ecosistema.',
    desc='Aplicar los 7 principios de No Dejes Rastro (planificar, pisar y acampar en superficies resistentes, llevarse los residuos, dejar lo que encuentras, no hacer fuego, respetar la fauna y a los demás) y las buenas prácticas para observar fauna sensible. Se entrena con el curso gratuito de es.lnt.org y aplicándolo en cada salida de práctica.',
    jane='En la Montaña de Riaño hay oso ocasional, lobo y urogallo: no publicar en redes la ubicación de los avistamientos, no acercarse a crías ni madrigueras y vivaquear lejos de fuentes y de zonas de cría.',
    res=['l0-lnt-es', 'l0-lnt-7', 'l0-buenas-practicas-fauna', 'l0-picos-normas'],
    ethics='Molestar intencionadamente a especies protegidas (oso pardo, urogallo cantábrico) puede ser una infracción legal además de un problema ético; en caso de duda, retirarse.'),
  'botiquin': dict(
    sci='s',
    sciNote='Los primeros auxilios siguen protocolos de Cruz Roja y de medicina de montaña basada en la evidencia; el contenido exacto del botiquín es una recomendación práctica.',
    desc='Llevar un botiquín ligero y saber usarlo: ampollas, heridas, esguinces, hipotermia y cómo avisar al 112 dando la ubicación. Se entrena haciendo un curso oficial de primeros auxilios y revisando el botiquín antes de cada salida.',
    jane='Escenario práctico: una torcedura de tobillo a medio día del pueblo más cercano; vendaje funcional, manta térmica, llamar al 112 con coordenadas y decidir si se puede bajar andando.',
    res=['l0-ms-botiquin', 'l0-cruzroja-curso', 'l0-subirats-pa', 'l0-subirats-med'],
    ethics='Un curso no convierte en sanitario: ante una lesión seria, prioriza llamar al 112 y no improvises tratamientos avanzados.'),
  'foto-base': dict(
    sci='s',
    sciNote='Óptica y exposición son física bien establecida; la composición tiene reglas convencionales más que ciencia estricta.',
    desc='Dominar el triángulo de exposición (apertura, velocidad e ISO), los modos de enfoque (AF-C para animales en movimiento) y las nociones básicas de composición antes de salir. Se entrena en casa y en parques fotografiando aves o mascotas en modo manual o semiautomático y revisando el histograma.',
    jane='Escenario práctico: un rebeco moviéndose al amanecer con poca luz; velocidad de 1/1000 s o más rápida, apertura grande y subir el ISO lo que haga falta, con AF-C y ráfaga.',
    res=['l0-cta-triangulo', 'l0-roger-benito', 'l0-xataka-af', 'l0-wolfe-gardner', 'l0-freeman', 'l0-peterson'],
    ethics=None),
}
BLOCKED = [
  'https://pubmed.ncbi.nlm.nih.gov/15677062/ (WebFetch devolvió página de cookies; se usó el artículo 14964502 verificado en búsqueda)',
  'https://www.cruzroja.es/principal/web/formacion/curso-online-de-primeros-auxilios-basicos (HTTP 503 en WebFetch; título, 20 h y certificado verificados en WebSearch)',
  'https://www.youtube.com/watch?v=g9-t_CKnXwQ (canal no verificable; descartado)',
]
