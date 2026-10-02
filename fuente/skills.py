# Estructura del árbol: niveles, nombres y dependencias.
# El contenido (desc, ejemplo, insignia, recursos) viene de research/*.py
LEVELS = [
    dict(id=0, name='Cimientos', sub='Lo que hay que saber antes de pisar el monte'),
    dict(id=1, name='Planificar y moverse', sub='Rutas, navegación, agua y comida'),
    dict(id=2, name='Vida en ruta y seguridad', sub='Dormir fuera, nieve y emergencias'),
    dict(id=3, name='Vida salvaje', sub='Conocer, respetar y encontrar la fauna'),
    dict(id=4, name='Fotografía de fauna', sub='La razón del viaje'),
    dict(id=5, name='Extras', sub='Sin requisitos: para curiosos'),
]

TREE = [
    # id, nombre, nivel, deps
    ('zona', 'Conocer la zona: Riaño-Mampodre y Picos', 0, []),
    ('forma', 'Preparación física para travesía', 0, []),
    ('equipo', 'Equipo, capas y mochila', 0, []),
    ('meteo', 'Meteorología de montaña en primavera', 0, []),
    ('etica', 'Ética de montaña / No dejar rastro', 0, []),
    ('botiquin', 'Botiquín y primeros auxilios básicos', 0, []),
    ('foto-base', 'Fundamentos de fotografía', 0, []),

    ('marcha', 'Técnica de marcha y bastones', 1, ['forma', 'equipo']),
    ('mapa', 'Mapa topográfico y brújula', 1, ['zona']),
    ('gps', 'Navegación digital (GPS y tracks)', 1, ['mapa']),
    ('plan', 'Planificación de ruta (MIDE, plan B)', 1, ['zona', 'meteo']),
    ('agua', 'Agua: encontrarla y potabilizarla', 1, ['equipo']),
    ('comida', 'Alimentación y cocina en travesía', 1, ['equipo']),

    ('pernocta', 'Vivac, acampada y normativa', 2, ['plan', 'etica']),
    ('dormir', 'Dormir abrigado e hipotermia', 2, ['equipo', 'meteo']),
    ('nieve', 'Neveros y nieve de primavera', 2, ['plan', 'marcha']),
    ('emergencias', 'Emergencias: 112, rescate y comunicación', 2, ['plan', 'gps']),
    ('aux-remoto', 'Primeros auxilios en lugares remotos', 2, ['botiquin']),
    ('bichos', 'Garrapatas, víboras y otros riesgos', 2, ['botiquin']),

    ('fauna', 'Fauna de la Cordillera Cantábrica', 3, ['zona']),
    ('aves', 'Aves de montaña', 3, ['fauna']),
    ('oso', 'Oso pardo: convivencia y encuentros', 3, ['fauna', 'etica']),
    ('ganado', 'Ganado y mastines de protección', 3, ['fauna']),
    ('observar', 'Observación de fauna', 3, ['fauna', 'marcha']),

    ('foto-fauna', 'Fotografía de fauna en travesía', 4, ['foto-base', 'observar']),
    ('foto-etica', 'Ética y legalidad de la foto de naturaleza', 4, ['foto-fauna', 'aves']),
    ('hides', 'Hides, camuflaje y fototrampeo', 4, ['foto-fauna', 'foto-etica']),
    ('edicion', 'Revelado y edición', 4, ['foto-fauna']),

    ('rastreo', 'Huellas y rastros', 5, []),
    ('plantas', 'Plantas y setas', 5, []),
    ('fuego', 'Fuego (y su normativa)', 5, []),
    ('refugio', 'Refugio improvisado de emergencia', 5, []),
    ('nudos', 'Nudos útiles', 5, []),
    ('orientacion-natural', 'Orientación natural sin brújula', 5, []),
]
