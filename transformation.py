import pandas as pd
import numpy as np

def is_nrofam(x):
    if x == 'Sin Información':
        return False
    else:
        return True
    
def transform(tipo, rut, giro, nombre, apellidopaterno, apellidomaterno, rutcontacto, nombrecontacto,
    apellidocontacto, telcontacto, celcontacto, email, direccion, numero, depto, region, provincia,
    comuma, rangoedad, sexo, nacionalidad, estadocivil, nrogrupofamiliar, actividad, cargo, situacionlaboral,
    empleador, antiguedadlaboral, fechanacimiento, presencial, remoto, medio):
    
    comuna = 'Otro'; region = 'Metropolitana'; provincia= 'Santiago'
    
#     print(tipo, rut, giro, nombre, apellidopaterno, apellidomaterno, rutcontacto, nombrecontacto,
#     apellidocontacto, telcontacto, celcontacto, email, direccion, numero, depto, region, provincia,
#     comuma, rangoedad, sexo, nacionalidad, estadocivil, nrogrupofamiliar, actividad, cargo, situacionlaboral,
#     empleador, antiguedadlaboral, fechanacimiento, presencial, remoto, medio)

    direccion = direccion + ' ' + str(numero) + ' '+ str(depto)
    nombre_completo = nombre + ' ' + apellidopaterno + ' ' + apellidomaterno
    
    new = {
        'tipo cliente':[tipo], #1
        'rut':[rut], #2
        'giro' : [giro], #3
        'nombre' : [nombre], #4
        'apellido 1' : [apellidopaterno], #5
        'apellido 2' : [apellidomaterno], #6
        'nombre completo' : [nombre_completo], #7
        'rutcontacto' : [rutcontacto], #8
        'nombrecontacto' : [nombrecontacto], #9
        'apellidocontacto' : [apellidocontacto],  #10
        'telefono' :[ telcontacto], #11
        'celular' : [celcontacto], #12
        'correo electronico' : [email], #13
        'direccion' : [direccion], #14
        'region' : [region], #15
        'provincia' : [provincia], #16
        'comuna' : [comuna], #17
        'rangoedad' : [rangoedad], #18
        'sexo' : [sexo], #19
        'nacionalidad' : [nacionalidad], #20
        'estado civil' : [estadocivil], #21
        'nrogrupofamiliar' : [nrogrupofamiliar], 
        'actividad' : [actividad], 
        'cargo' : [cargo], 
        'situacionlaboral' : [situacionlaboral],
        'empleador' : [empleador], 
        'antiguedadlaboral': [antiguedadlaboral], 
        'fecha nacimiento' : [fechanacimiento], 
        'presencial' : [presencial], 
        'remoto' : [remoto], 
        'medio' : [medio]
        }

    new_persona = pd.DataFrame.from_dict(new)
    # print(new_persona.columns)
    ###############################################################################################################
    
    new_persona['medio_inicial'] = new_persona['medio']
    ###############################################################################################################
    new_persona['is_nrofam'] = [ is_nrofam(x) for x in new_persona['nrogrupofamiliar'] ]
    
    #REGION#######################################################################################################
    new_persona ['loc_region'] = new_persona ['region'].replace(
        {'VIII Región del Bío-Bío':'Bio-Bio',
         'XIII Región Metropolitana de Santiago':'Metropolitana'}
    )
    new_persona ['loc_region'] = new_persona ['region'].replace(
        ['II Región de Antofagasta',
           'IV Región de Coquimbo', 'VII Región del Maule',
           'X Región de Los Lagos',
           'V Región de Valparaíso',
           'VI Región del Libertador General Bernardo O Higgins',
           'XIV Región de Los Ríos',
           'XI Región de Aysen del General Carlos Ibáñez del Campo',
           'I Región de Tarapacá', 'IX Región de La Araucanía',
           'XII Región de Magallanes y de La Antártica Chilena',
           'XV Region de Arica y Parinacota', 'III Región de Atacama'],'Otro'
    )
    
    #PROVINCIA#######################################################################################################
    new_persona['loc_provincia'] = new_persona['provincia'].replace(
    {'Concepción':'Concepcion',
     'Santiago':'Santiago'}
    )
    new_persona['loc_provincia'] = new_persona['provincia'].replace(
        ['Antofagasta', 'Limarí', 'Talca', 'Biobío', 'Ñuble',
           'Llanquihue','Maipo', 'Valparaíso', 'Cachapoal',
           'Arauco', 'Valdivia', 'Coyhaique', 'Linares', 'Osorno',
           'San Felipe de Aconcagua', 'Iquique', 'Cautín', 'Capitán Prat',
           'Aysén', 'Chacabuco', 'Melipilla', 'Magallanes', 'Malleco',
           'Arica ', 'Elqui', 'El Loa', 'Cauquenes', 'Colchagua', 'Valdivia ',
           'Copiapó', 'Última Esperanza', 'Cordillera', 'Curicó', 'Chiloé',
           'Choapa', 'Huasco','Arica','Isla de Pascua'],'Otro'
    )
    
    #COMUNA#######################################################################################################
    new_persona['loc_comuna'] = new_persona['comuna'].replace(
    ['Ovalle', 'Constitución','Tomé', 'Chillán','Yungay',
     'Puerto Montt', 'Santiago', 'El Bosque', 'La Florida','Las Condes',
     'Ñuñoa', 'Providencia', 'Buin','Florida','Viña del Mar',
     'Machalí', 'Vitacura', 'Arauco', 'Contulmo', 'Concón',
     'Santa Juana', 'Puerto Varas', 'Cañete', 'Huechuraba', 'Valdivia',
     'Coyhaique', 'Colbún', 'Osorno', 'San Felipe', 'Iquique',
     'Rancagua', 'Lota', 'Temuco', 'Cochrane', 'Chillán Viejo', 'Maipú',
     'Aysén', 'Villarrica', 'La Reina', 'Peñalolén', 'Estación Central',
     'Colina', 'Quilicura', 'Curanilahue', 'Algarrobo', 'Talca',
     'San Carlos', 'Punta Arenas', 'Mulchén', 'Coelemu', 'Angol',
     'Laja', 'Nacimiento', 'Arica', 'La Serena', 'Hualqui',
     'San Miguel', 'Calama', 'Pelluhue', 'Quillón', 'Valparaíso',
     'Llanquihue', 'Los Álamos', 'Renca', 'Santa Cruz', 'Panguipulli',
     'Cabrero', 'Cerrillos', 'Pudahuel', 'Copiapó', 'Natales', 'Tirúa',
     'Cauquenes', 'La Cisterna', 'Yumbel', 'Ránquil', 'Padre Las Casas',
     'Las Cabras', 'Coquimbo', 'Lebu', 'San José de Maipo', 'San Ramón',
     'Curicó', 'Independencia', 'Lampa ', 'Castro', 'Punitaqui',
     'Conchalí', 'San Rosendo', 'Alto Hospicio', 'Illapel', 'Huasco',
     'Collipulli', 'Tucapel', 'Alto Biobío','Pirque','Lampa','Isla de Pascua','Antofagasta', 'Arica'],'Otro'
)
    #IS #####################################################################################################################
    new_persona['is_nombre'] = ~new_persona['nombre'].isnull()
    new_persona['is_apellido1'] = ~new_persona['apellido 1'].isnull()
    new_persona['is_apellido2'] = ~new_persona['apellido 2'].isnull()
    new_persona['is_nombrecompleto'] = ~new_persona['nombre completo'].isnull()
    new_persona['is_correo'] = ~new_persona['correo electronico'].isnull()
    new_persona['is_direccion'] = ~new_persona['direccion'].isnull()
    new_persona['is_telefono'] = ~new_persona['telefono'].isnull()
    new_persona['is_actividad'] = ~new_persona['actividad'].isnull()
    new_persona['is_estado_civil'] = ~new_persona['estado civil'].isnull()
    new_persona['is_fnac'] = ~new_persona['fecha nacimiento'].isnull()
    new_persona['is_celular'] = ~new_persona['celular'].isnull()
    new_persona['is_profesion'] = ~new_persona['cargo'].isnull()
    ########################################################################################################################
    
    new_persona['is_recontacto'] = False
    
    if new_persona['presencial'].tolist()[0] == 'Si':
        new_persona['is_presencial'] = True
    else: new_persona['is_presencial'] = False
    
    if new_persona['remoto'].tolist()[0] == 'Si':
        new_persona['is_remoto'] = True
    else: new_persona['is_remoto'] = False
    
    # parches
    if new_persona['actividad'].tolist()[0] == 'Sin Información':
        # new_persona['actividad'] = 'sin información'
        new_persona['actividad'] = 'sin informaciÃ³n'
    
    if new_persona['sexo'].tolist()[0] == 'Sin Información':
        # new_persona['sexo'] = 'sin información'
        new_persona['sexo'] = 'sin informaciÃ³n'
        
    ########################################################################################################################
    
    # print('\n','Resultados')
    print(new_persona ['loc_region'], new_persona ['loc_provincia'],  new_persona ['loc_comuna'],
          new_persona['is_nombre'], new_persona['is_apellido1'], new_persona['is_apellido2'], 
          new_persona['is_nombrecompleto'], new_persona['is_correo'], new_persona['is_direccion'],
          new_persona['is_telefono'],  new_persona['is_actividad'],  new_persona['is_estado_civil'],
          new_persona['is_fnac'], new_persona['is_celular'],
         new_persona['medio'], new_persona['sexo'], new_persona['actividad'], new_persona['tipo cliente'],
         new_persona['is_recontacto'], new_persona['is_presencial'], new_persona['is_remoto'])
    
    new_persona =  new_persona[['actividad', 'is_apellido1', 'is_apellido2','is_celular', 'is_direccion', 'is_fnac', 'is_nombre',
                                 'is_nombrecompleto', 'is_nrofam', 'is_presencial', 'is_profesion',
                                 'is_recontacto', 'is_remoto', 'is_telefono', 'loc_comuna',
                                 'loc_provincia', 'loc_region', 'medio_inicial', 'sexo']]
    return new_persona