# recursos
RES = [
  # r(id, titulo, autor, tipo, idioma, url, por_que_vale, dificultad, es=None)
  # --- marcha ---
  ('l1-glisshop-bastones', 'Guía para utilizar correctamente los bastones de senderismo', 'Glisshop', 'blog', 'es', 'https://www.glisshop.es/tutoriales/como-caminar-con-bastones-de-senderismo.html', 'Explica de forma visual cómo ajustar la altura (codo a 90°), acortar en subida, alargar en bajada y coordinar brazo-pie opuesto.', 1, None),
  ('l1-bmc-poles', 'How to use walking poles', 'British Mountaineering Council (presenta Chris Townsend)', 'video', 'en', 'https://www.thebmc.co.uk/en/video-how-to-use-walking-poles', 'Vídeo corto de la serie de habilidades de montaña del BMC con un senderista de largo recorrido muy experimentado.', 1, None),
  ('l1-ms-horario', 'Cómo calcular el horario de una excursión a partir del mapa', 'Montaña Segura', 'articulo', 'es', 'https://montanasegura.com/como-calcular-el-horario-de-una-excursion-a-partir-del-mapa/', 'Enseña la regla de referencia (unos 400 m de subida o 4 km por hora) para ajustar el ritmo y calcular horarios realistas.', 1, None),
  ('l1-schwameder-1999', 'Knee joint forces during downhill walking with hiking poles', 'Hermann Schwameder et al. (Journal of Sports Sciences, 17(12), 1999)', 'paper', 'en', 'https://doi.org/10.1080/026404199365362', 'Estudio biomecánico clásico: con bastones las fuerzas en la rodilla al bajar se redujeron un 12-25 %.', 3, None),
  ('l1-hawke-2020', 'Are Trekking Poles Helping or Hindering Your Hiking Experience? A Review', 'Ashley L. Hawke, Randall L. Jensen (Wilderness & Environmental Medicine, 2020)', 'paper', 'en', 'https://journals.sagepub.com/doi/10.1016/j.wem.2020.06.009', 'Revisión de la evidencia sobre bastones: beneficios en carga articular y estabilidad, y matices en gasto energético.', 3, None),
  ('l1-libertad-cimas', 'Montañismo. La libertad de las cimas', 'The Mountaineers (ed. española: Ediciones Desnivel)', 'libro', 'es', 'https://www.libreriadesnivel.com/libros/montanismo-la-libertad-de-las-cimas/9788498292268/', 'El manual de montañismo más vendido de la historia; cubre marcha, orientación, equipo, meteorología y primeros auxilios.', 2, None),
  # --- mapa ---
  ('l1-caballero-manual', 'Manual práctico de orientación con mapa y GPS', 'David Caballero Molano (Ediciones Desnivel, 2019)', 'libro', 'es', 'https://www.libreriadesnivel.com/libros/manual-practico-de-orientacion-con-mapa-y-gps/9788498294354/', 'Manual breve (96 págs.) que combina mapa y brújula con GPS, móvil y apps: justo lo que necesita un principiante.', 1, None),
  ('l1-caballero-ejercicios', 'Ejercicios de orientación con mapa y brújula', 'David Caballero Molano, Marta Hurtado López (Ediciones Desnivel, 2024)', 'libro', 'es', 'https://edicionesdesnivel.com/libros/ejercicios-de-orientacion-con-mapa-y-brujula/', 'Cuaderno de ejercicios para practicar curvas de nivel, puntos de referencia, distancias y rumbos antes de salir.', 2, None),
  ('l1-ign-video', 'Orientación en campo con mapa, brújula y apps', 'Instituto Geográfico Nacional (YouTube)', 'video', 'es', 'https://www.youtube.com/watch?v=si0xLXvPj68', 'Vídeo oficial del IGN que enseña orientación clásica y con apps móviles, con cuestionario para comprobar lo aprendido.', 1, None),
  ('l1-ign-brujula', 'Orientación con brújula (recurso educativo)', 'Instituto Geográfico Nacional', 'web', 'es', 'https://www.ign.es/recursos-educativos/descubre-territorio/brujula.html', 'Recurso interactivo del IGN para aprender a usar la brújula mediante pequeños retos.', 1, None),
  ('l1-cnig-mtn25', 'Centro de Descargas del CNIG – Mapa Topográfico Nacional', 'Centro Nacional de Información Geográfica (IGN)', 'web', 'es', 'https://centrodedescargas.cnig.es/CentroDescargas/mapa-topografico-nacional', 'Descarga gratuita del MTN25 oficial (ráster, vectorial, GeoPDF) para imprimir o cargar en el móvil.', 2, None),
  ('l1-ign-riano-105', 'Riaño. Mapa Topográfico Nacional 1:25.000 (hoja 105-II), 2020', 'Instituto Geográfico Nacional', 'web', 'es', 'https://www.ign.es/web/catalogo-cartoteca/resources/html/048791.html', 'Ficha oficial de la hoja MTN25 de Riaño (3.ª edición, 2020), referencia cartográfica de la zona.', 2, None),
  ('l1-mapas-fernandez', 'Plasman la Montaña de Riaño y Mampodre en dos mapas perfectos y únicos para senderistas', 'Diario de Valderrueda', 'articulo', 'es', 'https://www.diariodevalderrueda.es/texto-diario/mostrar/4452540/plasman-montana-riano-mampodre-mapas-perfectos-unicos-senderistas', 'Presenta los dos mapas excursionistas 1:35.000 del geólogo Aureliano Fernández Revilla sobre el Parque Regional.', 1, None),
  # --- gps ---
  ('l1-ign-apps', 'Aplicaciones móviles del IGN (Mapas de España / Mapas de España Básicos)', 'Instituto Geográfico Nacional', 'web', 'es', 'https://www.ign.es/web/dir-aplicaciones-moviles', 'Apps oficiales y gratuitas con mapas IGN descargables offline y soporte de tracks GPX/KML.', 1, None),
  ('l1-wikiloc-offline', '¿Cómo seguir una ruta Offline?', 'Wikiloc (centro de ayuda)', 'web', 'es', 'https://ayuda.wikiloc.com/article/730-seguir-ruta-offline', 'Pasos oficiales para guardar la ruta y el mapa offline en casa y seguirla sin cobertura en modo avión.', 1, None),
  ('l1-decathlon-bateria', '¿Cómo ahorrar batería en mi teléfono durante una ruta?', 'Decathlon Outdoor (soporte)', 'web', 'es', 'https://support.decathlon-outdoor.com/hc/es/articles/17376101527570--C%C3%B3mo-ahorrar-bater%C3%ADa-en-mi-tel%C3%A9fono-durante-una-ruta', 'Ajustes concretos para que el móvil-GPS aguante una jornada entera.', 1, None),
  ('l1-jacetania-movil', 'Cómo preparar el móvil antes de una ruta por el Pirineo: batería, mapas sin cobertura y trucos de emergencia', 'Jacetania Express', 'articulo', 'es', 'https://jacetaniaexpress.com/como-preparar-el-movil-antes-de-una-ruta-por-el-pirineo-bateria-mapas-sin-cobertura-y-trucos-de-emergencia/', 'Repasa modo avión + GPS, efecto del frío en las baterías de litio y la importancia de llevar mapa y brújula de respaldo.', 1, None),
  # --- plan ---
  ('l1-mide-fedme', 'MIDE. Método de información de excursiones', 'FEDME (Mi Senda)', 'web', 'es', 'https://misendafedme.es/mide/', 'Explicación oficial de la FEDME del método MIDE y de sus cuatro valoraciones (medio, itinerario, desplazamiento, esfuerzo).', 1, None),
  ('l1-mide-ms', 'El MIDE', 'Montaña Segura (Federación Aragonesa de Montañismo / Gobierno de Aragón)', 'web', 'es', 'https://montanasegura.com/el-mide/', 'Fuente original del método creado por Alberto París Roche, con manual y herramientas para valorar tu propia ruta.', 2, None),
  ('l1-ms-senderismo', 'Senderismo con seguridad', 'Montaña Segura', 'web', 'es', 'https://montanasegura.com/senderismo-con-seguridad/', 'Resume el esquema "planifica, equípate y actúa con prudencia", incluido el plan B y avisar de ruta y hora de regreso.', 1, None),
  ('l1-gc-campana', 'La Guardia Civil de Montaña pone en marcha una campaña de seguridad', 'Desnivel', 'articulo', 'es', 'https://www.desnivel.com/excursionismo/la-guardia-civil-de-montana-pone-en-marcha-una-campana-de-seguridad/', 'Recomendaciones de la Guardia Civil de Montaña (GREIM): planificar, no ir solo, móvil cargado, batería externa y ruta descargada.', 1, None),
  ('l1-greim-aristasur', 'El GREIM en los rescates de montaña', 'Aristasur', 'articulo', 'es', 'https://www.aristasur.com/contenido/el-greim-en-los-rescates-de-montana', 'Explica qué es el GREIM y cómo activar un rescate llamando al 062 o al 112.', 1, None),
  ('l1-riano-rutas', 'Rutas Parque Regional Montaña de Riaño y Mampodre (listado con enlaces Wikiloc)', 'Patrimonio Natural de Castilla y León (Junta de Castilla y León)', 'web', 'es', 'https://patrimonionatural.org/ficheros/RUTAS%20PR%20MONTA%C3%91A%20DE%20RIA%C3%91O%20Y%20MAMPODRE-20220901-115452.pdf', 'Listado oficial de los senderos señalizados del parque con sus tracks, base para diseñar etapas y alternativas.', 1, None),
  ('l1-geofocus-tiempos', 'Estimación del tiempo de demora en rutas pedestres: comparación de algoritmos', 'GeoFocus (revista científica)', 'paper', 'es', 'https://geofocus.org/index.php/geofocus/article/view/408', 'Compara algoritmos de cálculo de horarios a pie (incluido el enfoque del MIDE): útil para entender sus límites.', 3, None),
  ('l1-ms-federarse', 'Federarse en montaña', 'Montaña Segura', 'web', 'es', 'https://montanasegura.com/federarse-en-montana/', 'Aclara qué cubre la licencia federativa (accidentes y rescate) frente a no estar asegurado.', 1, None),
  # --- agua ---
  ('l1-wms-agua-2024', 'Wilderness Medical Society Clinical Practice Guidelines on Water Treatment for Wilderness, International Travel, and Austere Situations: 2024 Update', 'Howard D. Backer, Robert W. Derlet, Vincent R. Hill (Wilderness & Environmental Medicine, 2024)', 'paper', 'en', 'https://journals.sagepub.com/doi/10.1177/10806032231218722', 'Guía clínica de referencia: recomienda tratar el agua donde hay pastoreo y compara hervir, filtrar, químicos y UV.', 3, None),
  ('l1-cdc-agua', 'Water treatment while hiking, camping, and traveling', 'CDC (Centers for Disease Control and Prevention)', 'web', 'en', 'https://www.cdc.gov/healthywater/pdf/drinking/backcountry_water_treatment-508.pdf', 'Tabla oficial de eficacia de cada método frente a Giardia y Cryptosporidium (hervir, filtro ≤1 µm, cloro, dióxido de cloro).', 2, None),
  ('l1-fdmescyl-fuentes', 'Cuidado con el agua de las fuentes de montaña: la FDMESCYL se suma al aviso de Picos de Europa', 'Federación de Deportes de Montaña, Escalada y Senderismo de Castilla y León', 'articulo', 'es', 'https://www.fclm.com/2026/07/20/cuidado-con-el-agua-de-las-fuentes-de-montana-la-fdmescyl-se-suma-al-aviso-de-picos-de-europa/', 'Aviso regional: no beber de fuentes de zonas bajas o con ganado, llevar potabilizador y cuidar la higiene de la comida.', 1, None),
  ('l1-salyroca-agua', 'Cómo recoger, purificar y potabilizar agua en la montaña', 'Sal y Roca (El Español)', 'articulo', 'es', 'https://www.salyroca.es/articulo/roca/recoger-purificar-potabilizar-agua-montana/20170604142940003337.html', 'Introducción práctica en español a recoger y tratar agua en ruta.', 1, None),
  # --- comida ---
  ('l1-fmm-alimentacion', 'Alimentación para practicar deportes de montaña', 'Federación Madrileña de Montañismo', 'blog', 'es', 'https://fmm.es/alimentacion-para-practicar-deportes-de-montana/', 'Pautas federativas: gasto que puede rondar 4.000 kcal y 3-4 L de agua al día, comer poco cada ~2 h y beber antes de tener sed.', 1, None),
  ('l1-rei-menu', 'Backpacking Food Ideas & Meal Planning', 'REI Expert Advice', 'web', 'en', 'https://www.rei.com/learn/expert-advice/planning-menu.html', 'Cómo planificar el menú de varios días: 2.500-4.500 kcal por persona y día y llevar siempre comida extra.', 1, None),
  ('l1-forumsport-recetas', '5 recetas para cocinar con tu hornillo en tus trekkings', 'Forum Sport (blog de montaña)', 'blog', 'es', 'https://www.forumsport.com/es-es/blogs/montana/5-recetas-para-cocinar-con-tu-hornillo-en-tus-trekkings/', 'Ideas de cenas sencillas con hornillo para las noches de vivac.', 1, None),
  ('l1-travesiapirenaica-comida', 'Qué comida llevar a una excursión a la montaña', 'Travesía Pirenaica', 'blog', 'es', 'https://travesiapirenaica.com/comida-para-montana/', 'Lista práctica de alimentos densos en energía y fáciles de transportar.', 1, None),
  ('l1-acsm-fluidos', 'American College of Sports Medicine position stand. Exercise and Fluid Replacement', 'Michael N. Sawka et al. (Medicine & Science in Sports & Exercise, 2007)', 'paper', 'en', 'https://journals.lww.com/acsm-msse/Fulltext/2007/02000/Exercise_and_Fluid_Replacement.22.aspx', 'Postura oficial del ACSM sobre hidratación: necesidades individuales, electrolitos y reposición tras el esfuerzo.', 3, None),
]
# habilidades
SKILLS = {
  'marcha': dict(
    sci='p',
    sciNote='Hay estudios biomecánicos que muestran que los bastones reducen la carga en la rodilla al bajar, pero los efectos sobre el gasto energético son dispares y las reglas de ritmo son estimaciones empíricas.',
    desc='Caminar a un ritmo constante que puedas mantener horas con mochila (referencia: unos 400 m de desnivel o 4 km por hora) y no reventarte en la primera cuesta. Con los bastones: codo a 90° en llano, acortarlos en subida, alargarlos y plantarlos delante en bajada, coordinados con el pie contrario. Entrénalo en salidas de fin de semana con la mochila cargada antes de la travesía de primavera.',
    jane='Escenario práctico: en una bajada larga y empinada hacia el fondo del valle, alargad los bastones 5-10 cm, acortad el paso y dejad que los brazos frenen para ahorrar rodillas con la mochila de varios días.',
    res=['l1-glisshop-bastones', 'l1-bmc-poles', 'l1-ms-horario', 'l1-schwameder-1999', 'l1-hawke-2020', 'l1-libertad-cimas'],
    ethics=None),
  'mapa': dict(
    sci='s',
    sciNote='La cartografía topográfica oficial y la navegación con brújula son técnicas consolidadas, enseñadas por el IGN y las federaciones de montaña.',
    desc='Interpretar las curvas de nivel (collados, vaguadas, crestas), orientar el mapa, medir distancias y seguir un rumbo con brújula. Es el respaldo cuando falla el móvil o la niebla tapa las referencias, algo habitual en la Cordillera Cantábrica en primavera. Practicad primero en casa con el MTN25 impreso y después en rutas cortas y señalizadas.',
    jane='La hoja MTN25 105-II "Riaño" (IGN, 3.ª ed. 2020) cubre el entorno del embalse; comprobad en el visor del CNIG qué hojas cubren exactamente vuestras etapas desde Polvoredo e imprimidlas.',
    res=['l1-caballero-manual', 'l1-caballero-ejercicios', 'l1-ign-video', 'l1-ign-brujula', 'l1-cnig-mtn25', 'l1-ign-riano-105', 'l1-mapas-fernandez', 'l1-libertad-cimas'],
    ethics=None),
  'gps': dict(
    sci='s',
    sciNote='El posicionamiento GNSS es una tecnología madura; la Guardia Civil y las federaciones recomiendan el móvil con ruta descargada, siempre con mapa, brújula y batería de respaldo.',
    desc='Cargar el track GPX de cada etapa y los mapas offline (app del IGN, Wikiloc u otras) en casa, con wifi, y navegar en modo avión con el GPS activado para ahorrar batería. Llevad batería externa y protegedla del frío, porque las baterías de litio pierden autonomía con temperaturas bajas. Probad todo el sistema en una salida corta antes de la travesía.',
    jane='Escenario práctico: antes de salir de Polvoredo, descargad el mapa IGN de la zona y los tracks de todas las etapas y alternativas en los dos móviles; en ruta, uno navega y el otro guarda batería por si hay que llamar al 112.',
    res=['l1-ign-apps', 'l1-wikiloc-offline', 'l1-decathlon-bateria', 'l1-jacetania-movil', 'l1-caballero-manual', 'l1-ign-video', 'l1-gc-campana'],
    ethics='El GPS no sustituye al mapa y la brújula: si el móvil se queda sin batería, solo queda la navegación clásica.'),
  'plan': dict(
    sci='p',
    sciNote='El MIDE es un estándar de consenso adoptado por la FEDME, no un modelo validado experimentalmente; los fallos de planificación aparecen de forma reiterada en los análisis de accidentes.',
    desc='Valorar cada etapa con el MIDE (medio, itinerario, desplazamiento, esfuerzo), calcular horarios realistas, mirar la previsión y tener un plan B (atajo, refugio o pueblo de escape). Dejad a alguien la ruta, quiénes vais y la hora límite de regreso. Conoced los recursos de emergencia: 112, 062 (Guardia Civil/GREIM) y las Casas del Parque.',
    jane='El Parque Regional Montaña de Riaño y Mampodre tiene más de 300 km de senderos señalizados (30 PR y tramos del GR 1); la Casa del Parque de Valdeburón, en Lario, es un buen punto para consultar el estado de las rutas antes de salir.',
    res=['l1-mide-fedme', 'l1-mide-ms', 'l1-ms-senderismo', 'l1-gc-campana', 'l1-greim-aristasur', 'l1-riano-rutas', 'l1-geofocus-tiempos', 'l1-ms-federarse'],
    ethics='En caso de emergencia, llamad al 112 o al 062. La Guardia Civil recomienda no ir nunca solo (lo ideal es un grupo de tres o más). Federarse no es obligatorio, pero el seguro federativo cubre el rescate.'),
  'agua': dict(
    sci='s',
    sciNote='Las guías clínicas de la Wilderness Medical Society y del CDC respaldan hervir, filtrar (≤1 µm) y desinfectar con productos químicos, cada método con limitaciones conocidas.',
    desc='Localizar fuentes y arroyos en el mapa, tomar el agua lo más arriba posible y lejos del ganado, y tratarla siempre. Hervir es lo más fiable. Un filtro de ≤1 µm elimina Giardia y Cryptosporidium, y el dióxido de cloro necesita tiempos largos con agua fría. En primavera hay agua de deshielo, pero también ganado subiendo a los puertos.',
    jane='El Parque Nacional de Picos de Europa, vecino de Polvoredo, y la FDMESCYL desaconsejan beber de fuentes en zonas bajas o con ganado sin tratar el agua; filtrad y, si podéis, añadid pastillas o hervid el agua de la cena.',
    res=['l1-wms-agua-2024', 'l1-cdc-agua', 'l1-fdmescyl-fuentes', 'l1-salyroca-agua'],
    ethics='No contaminéis las fuentes: nada de lavar con jabón ni hacer vuestras necesidades cerca del agua, que comparten la fauna, el ganado y otros montañeros.'),
  'comida': dict(
    sci='s',
    sciNote='Las necesidades de energía e hidratación en el ejercicio prolongado están bien establecidas (ACSM); las cifras de kcal diarias son estimaciones que varían con cada persona y cada esfuerzo.',
    desc='Planificar unas 2.500-4.000+ kcal por persona y día con alimentos densos en energía (frutos secos, queso curado, chocolate, deshidratados), picar cada ~2 h y beber antes de tener sed. Organizad la comida en bolsas por día y por comida, y probad el hornillo y las cenas deshidratadas en una noche de prueba. Llevad siempre una ración de emergencia por si la travesía se alarga.',
    jane='Escenario práctico: para cada noche de vivac, preparad una bolsa con cena caliente (cuscús o puré con caldo), desayuno y snacks del día siguiente, y reabasteced en los pueblos o refugios donde paséis la noche.',
    res=['l1-fmm-alimentacion', 'l1-rei-menu', 'l1-forumsport-recetas', 'l1-travesiapirenaica-comida', 'l1-acsm-fluidos', 'l1-fdmescyl-fuentes'],
    ethics='Usad el hornillo con cuidado ante el riesgo de incendio y consultad la normativa del parque sobre fuego. Llevaos toda la basura.'),
}
BLOCKED = [
  'journals.sagepub.com (403 al hacer WebFetch; datos de Hawke & Jensen 2020 y de la WMS 2024 tomados de los resultados de búsqueda)',
  'www.youtube.com (WebFetch no muestra el canal; solo se incluye el vídeo del IGN, cuyo canal aparece en el título de la búsqueda)',
  'www.libreriadesnivel.com, misendafedme.es, www.cdc.gov, ayuda.wikiloc.com (WebFetch: no se pudo verificar el dominio; verificados solo por WebSearch)',
  'www.thebmc.co.uk (WebFetch abortado; verificado por WebSearch)',
]
