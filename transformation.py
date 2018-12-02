import pandas as pd
import numpy as np

from chile import provincias

def is_nrofam(x):
    if x == 'Sin Información':
        return False
    else:
        return True
    
def transform_persona_is(df_cliente_nuevo):
    new_persona = df_cliente_nuevo
    new_persona = transform_df_lower_accent(new_persona)
    # print(new_persona)
    ###############################################################################################################
    
    new_persona['medio_inicial'] = new_persona['medio']
    ###############################################################################################################
    new_persona['is_nrofam'] = [ is_nrofam(x) for x in new_persona['nrogrupofamiliar'] ]
    
    #REGION#######################################################################################################
    new_persona.loc_region = []
    new_persona['loc_region'] = new_persona['region'].replace(
        {'viii region del bio-bio':'bio-bio',
         'xiii region metropolitana de santiago':'metropolitana'}
    )
    new_persona['loc_region'] = new_persona['loc_region'].replace(
        ['ii region de antofagasta',
        'iv region de coquimbo', 
        'vii region del maule',
        'x region de los lagos',
        'v region de valparaiso',
        'vi region del libertador general bernardo o higgins',
        'xiv region de los rios',
        'xi region de aysen del general carlos ibanez del campo',
        'i region de tarapaca', 
        'ix region de la araucania',
        'xii region de magallanes y de la antartica chilena',
        'xv region de arica y parinacota',
         'xiv region de los rios',
        'iii region de atacama'],'otro'
    )

    
    #PROVINCIA#######################################################################################################
    new_persona['loc_provincia'] = new_persona['provincia'].replace(
        {'concepcion':'concepcion',
         'santiago':'santiago'}
    )
    
    provincias_l = []
    for key in provincias.keys():
        provincias_l.extend(provincias[key])

    new_persona['loc_provincia'] = [x if x in provincias_l else 'otro' \
            for x in new_persona['loc_provincia'].tolist()]

    #COMUNA#######################################################################################################
    comunas_l = ['Concepcion',   'Coronel',  'Chiguayante',  'Florida',  'Hualqui',  
     'Lota',  'Penco',  'San Pedro de la Paz',  'Santa Juana',  
     'Talcahuano',  'Tome',  'Hualpen',
    'Santiago',  'Cerrillos',  'Cerro Navia',  'Conchali',  'El Bosque',  
     'Estacion Central',  'Huechuraba',  'Independencia',  'La Cisterna',  'La Florida',  'La Granja',  
     'La Pintana',  'La Reina',  'Las Condes',  'Lo Barnechea',  'Lo Espejo',  'Lo Prado',  'Macul',  'Maipu',  
     'nunoa',  'Pedro Aguirre Cerda',  'Peñalolén',  'Providencia',  'Pudahuel',  'Quilicura',  
     'Quinta Normal',  'Recoleta',  'Renca',  'San Joaquin',  'San Miguel',  'San Ramon',  'Vitacura']
    comunas_l = [x.lower() for x in comunas_l]

    new_persona['loc_comuna'] = [x if x in comunas_l else 'otro' for x in new_persona['comuna'].tolist()]
    
    #IS #####################################################################################################################
    new_persona['is_nombre'] = ~new_persona['nombre'].isnull()
    new_persona['is_apellido1'] = ~new_persona['apellido1'].isnull()
    new_persona['is_apellido2'] = ~new_persona['apellido2'].isnull()
    new_persona['is_nombrecompleto'] = ~new_persona['nombre completo'].isnull()
    new_persona['is_correo'] = ~new_persona['correo'].isnull()
    new_persona['is_direccion'] = ~new_persona['direccion'].isnull()
    new_persona['is_telefono'] = ~new_persona['telefono'].isnull()
    new_persona['is_actividad'] = ~new_persona['actividad'].isnull()
    new_persona['is_estado_civil'] = ~new_persona['estado civil'].isnull()
    new_persona['is_fnac'] = ~new_persona['fecha nacimiento'].isnull()
    new_persona['is_celular'] = ~new_persona['celular'].isnull()
    new_persona['is_profesion'] = ~new_persona['trabajo'].isnull()
    ########################################################################################################################
    
    new_persona['is_recontacto'] = False
    
    if new_persona['presencial'].tolist()[0] == 'Si':
        new_persona['is_presencial'] = True
    else: new_persona['is_presencial'] = False
    
    if new_persona['remoto'].tolist()[0] == 'Si':
        new_persona['is_remoto'] = True
    else: new_persona['is_remoto'] = False
    
    ########################################################################################################################
    # print('BLA')
    # print('\n','Resultados')
    # print(new_persona ['loc_region'], new_persona ['loc_provincia'],  new_persona ['loc_comuna'],
    #       new_persona['is_nombre'], new_persona['is_apellido1'], new_persona['is_apellido2'], 
    #       new_persona['is_nombrecompleto'], new_persona['is_correo'], new_persona['is_direccion'],
    #       new_persona['is_telefono'],  new_persona['is_actividad'],  new_persona['is_estado_civil'],
    #       new_persona['is_fnac'], new_persona['is_celular'],
    #      new_persona['medio'], new_persona['sexo'], new_persona['actividad'], new_persona['tipo_cliente'],
    #      new_persona['is_recontacto'], new_persona['is_presencial'], new_persona['is_remoto'])
    
    new_persona =  new_persona[[
        'actividad', 'is_apellido1', 'is_apellido2','is_celular', 
        'is_direccion', 'is_fnac', 'is_nombre',
        'is_nombrecompleto', 'is_nrofam', 'is_presencial', 'is_profesion',
        'is_recontacto', 'is_remoto', 'is_telefono', 'loc_comuna',
        'loc_provincia', 'loc_region', 'medio_inicial', 'sexo']]
    return new_persona

# Transforma los datos de las multiples cotizaciones a datos de comportamiento por
# cliente
def add_persona_new_comp_cot(df):
    comp_cot = {
        'is_descuento': [False],
        'valid_rut': [True],
        'mean_cot_bod' : [0],
        'mean_cot_depto': [0], 
        'mean_cot_esta' : [0], 
        'mean_cot_estu': [0], 
        'nro_cot_bod' : [0], 
        'nro_cot_depto' : [0], 
        'nro_cot_esta' : [0],
        'nro_cot_estu' : [0], 
        'nro_proyectos' : [0], 
        'precio_cotizacion_media' : [0],
        'precio_cotizacion_median' : [0], 
        'precio_cotizacion_std' : [0], 
        'tiempo_cotizacion_media' : [0], 
        'tiempo_cotizacion_median' : [0],
        'tiempo_cotizacion_std' : [0],   
        'altos del valle' : [0],
        'edificio urban 1470' : [0], 
        'san Andres del valle':[0], 
        'edificio mil610': [0],
        'edificio junge': [0]
    }

    df = df.assign(**comp_cot)

    return df

def trasnform_persona_info(df):
    new = {
        "apellido1" : [df['apellido1'].tolist()],
        "apellido2" : [df['apellido2'].tolist()],
        "celular" : [df['celular'].tolist()],
        "correo"  : [df['corre electronico'].tolist()],
        "direccion" :   [df['direccion'].tolist()],
        "edad " : [df['apellido 1'].tolist()],
        "trabajo" : [df['apellido 1'].tolist()],
        }


def transform_prospect_display_text(t_proba_value):
    if t_proba_value >= 0.90:
        return 'Muy buen prospecto'
    elif t_proba_value >= 0.80:
        return 'Buen prospecto'
    elif t_proba_value >= 0.60:
        return ' Prospecto regular'
    elif t_proba_value >= 0.50 :
        return 'Indeciso'
    elif t_proba_value >= 0.0:
        return 'Mal prospecto'

def transform_df_lower_accent(df):
    print("transform_df_lower_accent")
    cot_mod = df
    for column in cot_mod.columns:
        if cot_mod[column].dtype == object:
            cot_mod[column] = cot_mod[column].str.lower()
            cot_mod[column].replace({
                    'á':'a', 
                    'é':'e', 
                    'í':'i', 
                    'ó':'o', 
                    'ú':'u', 
                    'ñ':'n', '\xa0':''}, regex=True, inplace=True)
            # cot_mod[column].replace(['sin informacion', '', '.', '-', '*', '..', '...', '....'], np.nan, inplace=True)
    # print(cot_mod)
    return cot_mod



def get_products(x,word,numeric=False):
    w=0
    try:
        p =str(x)
        arr_p = x.split(',')
        for e in arr_p:
            if word in e:
                w+=1
                break
            elif numeric and ('B' not in e or 'Est' not in e):
                try:
                    int(e)
                    w+=1
                except ValueError:
                    pass
        return w
    except (ValueError,AttributeError):
        try:
            int(x)
            if numeric:
                return 1
            else:
                return 0
        except ValueError:
            return 0

def transform_comp_cot(df):
    
    #Cantidad de productos
    productos = cot_mod['Productos'].tolist()
    depto = []; estacionamiento=[]; bodega = []; estudio = [];nan = 0

    cot_mod['#vivienda'] = [get_products(x,'T',numeric=True) for x in productos]
    cot_mod['#bodega'] = [get_products(x,'Bod') for x in productos]
    cot_mod['#estacionamiento'] = [get_products(x,'Est') for x in productos]
    cot_mod['#estudio'] = [get_products(x,'Estudio') for x in productos]
    cot_mod['#lan'] = [get_products(x,'lan') for x in productos]

    #(UF)Total Productos cotizados
    precio_cotizacion_media = []
    precio_cotizacion_std = []
    precio_cotizacion_median = []
    for group, frame in cot_mod.groupby('RUT'):
        media = float("%.2f" % np.mean(frame['Total Productos'].tolist()))
        std = float("%.2f" % np.std(frame['Total Productos'].tolist()))
        median = float("%.2f" % np.median(frame['Total Productos'].tolist()))
    #     print(group, media, std, median)
        precio_cotizacion_media.append(media)
        precio_cotizacion_std.append(std)
        precio_cotizacion_median.append(median)

    print(len(precio_cotizacion_media))
    print(len(precio_cotizacion_std))
    print(len(precio_cotizacion_median))

    #Tiempo entre cotizaciones
    cot_mod['Fecha Cotizacion'] = pd.to_datetime(cot_mod['Fecha Cotizacion'])
    tiempo_cotizacion_media = []
    tiempo_cotizacion_std = []
    tiempo_cotizacion_median = []

    for group, frame in cot_mod.groupby('RUT'):
        l = frame['Fecha Cotizacion'].tolist()
        l = [x.date() for x in l]
        l = sorted(l, reverse=False)
        d = []
        anterior = l[0]
        if len(l) != 1:
            for i in range(1,len(l)):
                try:
                    dif = abs(int(str(l[i] - anterior).split(' ')[0]))
                except ValueError:
                    d.append(0)
                anterior = l[i]
                d.append(dif)
            
        else:
            d.append(0)
        mean = float( '%.2f'%np.mean(d))
        std = float( '%.2f'%np.std(d))
        median = float( '%.2f'%np.median(d))
        tiempo_cotizacion_media.append(mean)
        tiempo_cotizacion_std.append(std)
        tiempo_cotizacion_median.append(median)

    print(len(tiempo_cotizacion_media))
    print(len(tiempo_cotizacion_std))
    print(len(tiempo_cotizacion_median))   

    # Cotizaciones por proyecto
    rut_dict = dict()
    for index, row in cot_mod.iterrows():
        rut = row['Format Rut']
        pr = row['Proyecto']
        
        if rut not in rut_dict.keys():
            rut_dict[rut] = dict()
            rut_dict[rut]['altos del valle'] = 0
            rut_dict[rut]['edificio urban 1470'] = 0
            rut_dict[rut]['san andres del valle'] = 0
            rut_dict[rut]['edificio mil610'] = 0
            rut_dict[rut]['edificio junge'] = 0
        
        rut_dict[rut][pr] +=1



    rut_proyectos = pd.DataFrame.from_dict(rut_dict,orient='index').reset_index()
    rut_proyectos.head()