import os
import time, timeit
from textwrap import dedent

import numpy as np
import pandas as pd

import copy

from sklearn.externals import joblib


start_dm = timeit.default_timer()
################################################################################################
#PREDICTORS
no_is_time_price = [
    'is_recontacto', 'is_remoto', 'is_descuento', 'valid_rut',
    'loc_comuna', 'loc_provincia', 'loc_region', 'sexo', 'tipo_cliente',
    'mean_cot_bod',
    'mean_cot_depto', 'mean_cot_esta', 'mean_cot_estu', 'medio_inicial',
    'nro_cot_bod', 'nro_cot_depto', 'nro_cot_esta',
    'nro_cot_estu', 'nro_proyectos', 'precio_cotizacion_media',
    'precio_cotizacion_median', 'precio_cotizacion_std', 
    'tiempo_cotizacion_media', 'tiempo_cotizacion_median',
    'tiempo_cotizacion_std',   
    'altos del valle',
    'edificio urban 1470', 
    # 'San Andres Del Valle', 
    'edificio mil610',
       'edificio junge']


is_no_time_price = ['actividad', 'is_apellido1', 'is_apellido2',
       'is_celular', 'is_direccion', 'is_fnac', 'is_nombre',
       'is_nombrecompleto', 'is_nrofam', 'is_presencial', 'is_profesion',
       'is_recontacto', 'is_remoto', 'is_telefono', 'loc_comuna',
       'loc_provincia', 'loc_region', 'medio_inicial', 'sexo']



personal_info = [
  'rut', 'nombre', 'apellido1', 'apellido2', 'celular', 'direccion',
  'correo', 'edad', 'trabajo', 'tipo_cliente', 'sexo', 'actividad'
  ]


################################################################################################
# MODEL TEST DATA
start = timeit.default_timer()
X_test_m = pd.read_excel('Data/Test/x_test_negocio_nois.xlsx') # 123KB
y_test_m = pd.read_excel('Data/Test/y_test_negocio_nois.xlsx') # 15KB

X_test_c = pd.read_excel('Data/Test/x_test_compra_nois.xlsx') # 123KB
y_test_c = pd.read_excel('Data/Test/y_test_compra_nois.xlsx') # 14KB

stop = timeit.default_timer()
print('--END READ TEST DATA','Time: ', stop - start)

################################################################################################
#MODELOS
start = timeit.default_timer()
# clf_compra_nois = joblib.load('Data/Models/RFCV2_compra_nois.joblib')
# clf_negocio_nois = joblib.load('Data/Models/LRCV2_negocio_nois.joblib')


# clf_compra_is = joblib.load('Data/Models/LRCV2_compra_is.joblib')
# clf_negocio_is = joblib.load('Data/Models/RFCV2_negocio_is.joblib')

clf_compra_nois = joblib.load('Data/Models/RFCV3_compra_nois.joblib')
clf_negocio_nois = joblib.load('Data/Models/LRCV3_negocio_nois.joblib')
clf_compra_is = joblib.load('Data/Models/RFCV3_compra_is.joblib')
clf_negocio_is = joblib.load('Data/Models/RFCV3_negocio_is.joblib')

models = {}
models['negocio_nois'] = clf_negocio_nois
models['compra_nois'] = clf_compra_nois
models['negocio_is'] = clf_negocio_is
models['compra_is'] = clf_compra_is
stop = timeit.default_timer()
print('--END READ MODELS','Time: ', stop - start)

#################################################################################################
#DATA
start = timeit.default_timer()

proyecto_select = 'San Andres Del Valle'
#personas para hacer get dummies
p_for_dummies = pd.read_csv('Data/personas_cotizacion10.csv', index_col=[0], encoding = "ISO-8859-1") # 
cot_all = pd.read_csv('Data/cotizaciones_all.csv', index_col=[0], encoding = "ISO-8859-1")
#personas que cotizaron en sdv sin haber hecho get dummies
personas = pd.read_csv('Data/personas_filtro.csv', index_col=[0], encoding = "ISO-8859-1")
personas_info = pd.read_csv('Data/personas_cotizacion10.csv', index_col=[0], encoding = "ISO-8859-1") # 

stop = timeit.default_timer()
print('--END READ PERSONAS DATA','Time: ', stop - start)

######################################################################################################
start = timeit.default_timer()
personas['loc_comuna'] = personas['loc_comuna'].astype('category')
personas['loc_provincia'] = personas['loc_provincia'].astype('category')
personas['loc_region'] = personas['loc_region'].astype('category')
personas['tipo_cliente'] = personas['tipo_cliente'].astype('category')
personas['sexo'] = personas['sexo'].astype('category')
personas['medio_inicial'] = personas['medio_inicial'].astype('category')

personas_info['loc_comuna'] = personas_info['loc_comuna'].astype('category')
personas_info['loc_provincia'] = personas_info['loc_provincia'].astype('category')
personas_info['loc_region'] = personas_info['loc_region'].astype('category')
personas_info['tipo_cliente'] = personas_info['tipo_cliente'].astype('category')
personas_info['sexo'] = personas_info['sexo'].astype('category')
personas_info['medio_inicial'] = personas_info['medio_inicial'].astype('category')
personas_info['actividad'] = personas_info['actividad'].astype('category')

stop = timeit.default_timer()
print('--END CHANGE DATA TYPE','Time: ', stop - start)

#################################################################################################
stop_dm = timeit.default_timer()
print('END DATA MANAGER','Time: ', stop_dm - start_dm)