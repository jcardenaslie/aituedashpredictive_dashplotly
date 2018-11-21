regiones = ['VIII Región del Bío-Bío', 'XIII Región Metropolitana de Santiago',
       'X Región de Los Lagos', 'II Región de Antofagasta',
       'VII Región del Maule',
       'VI Región del Libertador General Bernardo O Higgins',
       'I Región de Tarapacá', 'V Región de Valparaíso',
       'XII Región de Magallanes y de La Antártica Chilena',
       'XI Región de Aysen del General Carlos Ibáñez del Campo',
       'IX Región de La Araucanía', 'XV Region de Arica y Parinacota',
       'XIV Región de Los Ríos', 'IV Región de Coquimbo',
       'III Región de Atacama']

provincias = {
#1
'XV Region de Arica y Parinacota':['Arica', 'Parinacota'],
#2
'I Región de Tarapacá':['Iquique', 'Tamarugal'], 
#3
'II Región de Antofagasta':['Antofagasta', 'El Loa', 'Tocopilla'],
#4
'III Región de Atacama':['Chañaral', 'Copiapó', 'Huasco'],
#5
'IV Región de Coquimbo':['Choapa', 'Elqui', 'Limari'],
#6
'V Región de Valparaíso':['Isla de Pascua', 'Los Andes', 'Petorca', 
    'Quillota', 'San Antonio', 'San Felipe', 'Valparaiso'],
#7
'XIII Región Metropolitana de Santiago':['Chacabuco', 'Cordillera', 'Maipo', 'Melipilla', 'Santiago', 'Talagante'],
#8
'VI Región del Libertador General Bernardo O Higgins':['Cachapoal', 'Cardenal Caro', 'Colchagua'],
#9
'VII Región del Maule':['Cauquenes', 'Curico', 'Linares', 'Talca'],
#10
'VIII Región del Bío-Bío':['Arauco', 'BioBío', 'Concepción','Ñuble'], 
#11
'IX Región de La Araucanía':['Cautín', 'Malleco'], 
#12
'X Región de Los Lagos':['Valdivia', 'Ranco'], 
#13
'XI Región de Aysen del General Carlos Ibáñez del Campo':['Chiloe', 'Llanquihue', 'Osorno', 'Palena'],
#14
'XII Región de Magallanes y de La Antártica Chilena':['Aisén', 'Capitan Prat', 'Coihaique', 'General Carrera'],
#15
'XIV Región de Los Ríos':['Antártica Chilena', 'Magallanes', 'Tierra del Fuego', 'Ultima Esperanza'],
}

comunas = {
 'Aisén': ['Aisén', 'Cisnes', 'Guaitecas'],
 'Antofagasta': ['Antofagasta', 'Mejillones', 'Sierra Gorda', 'Taltal'],
 'Antártica Chilena': ['Cabo de Hornos', 'Antártica'],
 'Arauco': ['Lebu', 'Arauco', 'Cañete', 'Contulmo', 'Curanilahue',  'Los Álamos','Tirúa'],
 'Arica': ['Arica', 'Camarones'],
 'BioBío': ['Los Ángeles',   'Antuco',   'Cabrero',   'Laja',   'Mulchén',   'Nacimiento',   'Negrete',   'Quilaco',   'Quilleco',   'San Rosendo',   'Santa Bárbara',   'Tucapel',   'Yumbel',   'Alto Biobío'],
 'Cachapoal': ['Rancagua',   'Codegua',   'Coinco',   'Coltauco',   'Doñihue',   'Graneros',   'Las Cabras',   'Machalí',   'Malloa',   'Mostazal',   'Olivar',   'Peumo',   'Pichidegua',   'Quinta de Tilcoco',   'Rengo',   'Requínoa',   'San Vicente'], 
 'Capitan Prat': ['Cochrane', "O'Higgins", 'Tortel'],
 'Cardenal Caro': ['Pichilemu',   'La Estrella',   'Litueche',   'Marchihue',   'Navidad',   'Paredones'],  
 'Cauquenes': ['Cauquenes', 'Chanco', 'Pelluhue'],
 'Cautín': ['Temuco',   'Carahue',  'Cunco',  'Curarrehue',  'Freire',  'Galvarino',  'Gorbea',  'Lautaro',  'Loncoche',  'Melipeuco',  'Nueva Imperial',  'Padre Las Casas',  'Perquenco',  'Pitrufquén',  'Pucón',  'Saavedra',  'Teodoro Schmidt',  'Toltén',  'Vilcún',  'Villarrica',  'Cholchol'],
 'Chacabuco': ['Colina', 'Lampa', 'Tiltil'],
 'Chañaral': ['Chañaral', 'Diego de Almagro'],
 'Chiloe': ['Castro',   'Ancud',  'Chonchi',  'Curaco de Vélez',  'Dalcahue',  'Puqueldón',  'Queilén',  'Quellón',  'Quemchi',  'Quinchao'],
 'Choapa': ['Illapel', 'Canela', 'Los Vilos', 'Salamanca'],
 'Coihaique': ['Coihaique', 'Lago Verde'],
 'Colchagua': ['San Fernando',   'Chépica',  'Chimbarongo',  'Lolol',  'Nancagua',  'Palmilla',  'Peralillo',  'Placilla',  'Pumanque',  'Santa Cruz'],
 'Concepción': ['Concepción',   'Coronel',  'Chiguayante',  'Florida',  'Hualqui',  'Lota',  'Penco',  'San Pedro de la Paz',  'Santa Juana',  'Talcahuano',  'Tomé',  'Hualpén'],
 'Copiapó': ['Copiapó', 'Caldera', 'Tierra Amarilla'],
 'Cordillera': ['Puente Alto', 'Pirque', 'San José de Maipo'],
 'Curico': ['Curicó',  'Hualañé',  'Licantén',  'Molina',  'Rauco',  'Romeral',  'Sagrada Familia',  'Teno',  'Vichuquén'], 
 'El Loa': ['Calama', 'Ollagüe', 'San Pedro de Atacama'],
 'Elqui': ['La Serena',  'Coquimbo',  'Andacollo',  'La Higuera',  'Paiguano',  'Vicuña'],
 'General Carrera': ['Chile Chico', 'Río Ibáñez'],
 'Huasco': ['Vallenar', 'Alto del Carmen', 'Freirina', 'Huasco'],
 'Ignorada': ['Ignorada'],
 'Iquique': ['Iquique', 'Alto Hospicio'],
 'Isla de Pascua': ['Isla de Pascua'],
 'Limari': ['Ovalle',  'Combarbalá',  'Monte Patria',  'Punitaqui',  'Río Hurtado'],
 'Linares': ['Linares',  'Colbún',  'Longaví',  'Parral',  'Retiro',  'San Javier',  'Villa Alegre',  'Yerbas Buenas'],
 'Llanquihue': ['Puerto Montt',  'Calbuco',  'Cochamó',  'Fresia',  'Frutillar',  'Los Muermos',  'Llanquihue',  'Maullín',  'Puerto Varas'],
 'Los Andes': ['Los Andes', 'Calle Larga', 'Rinconada', 'San Esteban'],
 'Magallanes': ['Punta Arenas', 'Laguna Blanca', 'Río Verde', 'San Gregorio'],
 'Maipo': ['San Bernardo', 'Buin', 'Calera de Tango', 'Paine'],
 'Malleco': ['Angol',  'Collipulli',  'Curacautín',  'Ercilla',  'Lonquimay',  'Los Sauces',  'Lumaco',  'Purén',  'Renaico',  'Traiguén',  'Victoria'],
 'Marga Marga': ['Quilpué', 'Villa Alemana', 'Limache', 'Olmué'],
 'Melipilla': ['Melipilla', 'Alhué', 'Curacaví', 'María Pinto', 'San Pedro'],
 'Osorno': ['Osorno',  'Puerto Octay',  'Purranque',  'Puyehue',  'Río Negro',  'San Juan de la Costa',  'San Pablo'],
 'Palena': ['Chaitén', 'Futaleufú', 'Hualaihué', 'Palena'],
 'Parinacota': ['Putre', 'General Lagos'],
 'Petorca': ['La Ligua', 'Cabildo', 'Papudo', 'Petorca', 'Zapallar'],
 'Quillota': ['Quillota', 'Calera', 'Hijuelas', 'La Cruz', 'Nogales'],
 'Ranco': ['Futrono', 'La Unión', 'Lago Ranco', 'Río Bueno'],
 'San Antonio': ['San Antonio',  'Algarrobo',  'Cartagena',  'El Quisco',  'El Tabo',  'Santo Domingo'],
 'San Felipe': ['San Felipe',  'Catemu',  'Llaillay',  'Panquehue',  'Putaendo',  'Santa María'],
 'Santiago': ['Santiago',  'Cerrillos',  'Cerro Navia',  'Conchalí',  'El Bosque',  'Estación Central',  'Huechuraba',  'Independencia',  'La Cisterna',  'La Florida',  'La Granja',  'La Pintana',  'La Reina',  'Las Condes',  'Lo Barnechea',  'Lo Espejo',  'Lo Prado',  'Macul',  'Maipú',  'Ñuñoa',  'Pedro Aguirre Cerda',  'Peñalolén',  'Providencia',  'Pudahuel',  'Quilicura',  'Quinta Normal',  'Recoleta',  'Renca',  'San Joaquín',  'San Miguel',  'San Ramón',  'Vitacura'],
 'Talagante': ['Talagante',  'El Monte',  'Isla de Maipo',  'Padre Hurtado',  'Peñaflor'],
 'Talca': ['Talca',  'Constitución',  'Curepto',  'Empedrado',  'Maule',  'Pelarco',  'Pencahue',  'Río Claro',  'San Clemente',  'San Rafael'], 
 'Tamarugal': ['Camiña', 'Colchane', 'Huara', 'Pica', 'Pozo Almonte'], 
 'Tierra del Fuego': ['Porvenir', 'Primavera', 'Timaukel'], 
 'Tocopilla': ['Tocopilla', 'María Elena'],
 'Ultima Esperanza': ['Natales', 'Torres del Paine'],
 'Valdivia': ['Valdivia',  'Corral',  'Lanco',  'Los Lagos',  'Máfil',  'Mariquina',  'Paillaco',  'Panguipulli'], 
 'Valparaiso': ['Valparaíso',  'Casablanca',  'Concón',  'Juan Fernández',  'Puchuncaví',  'Quintero',  'Viña del Mar'], 
 'Ñuble': ['Chillán',  'Bulnes',  'Cobquecura',  'Coelemu',  'Coihueco',  'Chillán Viejo',  'El Carmen',  'Ninhue',  'Ñiquén',  'Pemuco',  'Pinto',  'Portezuelo',  'Quillón',  'Quirihue',  'Ránquil',  'San Carlos',  'San Fabián',  'San Ignacio', 'San Nicolás',  'Treguaco',  'Yungay']
 }
