import os
import time, timeit
from textwrap import dedent

import dash
import dash_core_components as dcc
import dash_html_components as html
import numpy as np
import pandas as pd
from dash.dependencies import Input, Output, State, Event

import copy
from sklearn.externals import joblib
import utils.dash_reusable_components as drc
from modales import modal_nuevo_cliente

from app import app
import data_manager as dm
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 

from chile import regiones, provincias, comunas
from transformation import transform_persona_is, add_persona_new_comp_cot, \
transform_prospect_display_text, transform_df_lower_accent
from app import format_rut, indicator

layout = [
    modal_nuevo_cliente(),
    # add button
    html.Div(
        className="row",
        style={"text-align":'center', 'margin-bottom':'10px'},
        children=[
            # html.Button('Agregar Cliente',className='add', id='new_case'),
            html.Span(
                "Agregar Cliente",
                id="new_case",
                n_clicks=0,
                className="button button--secondary add",
            ), 
        ]
    ),
    # tables row div
    html.Div(
        [
            #Panel de Informacion
            html.Div(
                style={
                    "border":"1px solid #C8D4E3",
                    "border-radius": "3px",
                    "background-color": "white",
                    "vertical-align":"middle"
                },
                className='four columns', 
                children=[
                    html.H6('Información Personal', style={"text-align":"center"}),
                    drc.Card(style={'overflow-y':'scroll', 'height':'400px'} ,children=[
                        html.Ul(id='nc_personal_info' ,children=[
                            html.Li('Busca un rut'),
                        ])
                    ])
            ]),
            #Panel de Informacion Cotizaciones
            html.Div(
                style={
                    "border":"1px solid #C8D4E3",
                    "border-radius": "3px",
                    "background-color": "white",
                    "vertical-align":"middle"
                },
                className='four columns', 
                children=[
                    html.H6('Información Cotizaciones', 
                        style={"text-align":"center"}),
                    drc.Card(
                        style={'overflow-y':'scroll', 'height':'400px'},
                        children=[
                        html.Ul(id='nc_historical_info', 
                            children=[
                                html.Li('Busca un rut'),
                        ])
                    ])
            ]),
            #Paneles de Ranking
            html.Div(className='four columns',
                style={
                    "border":"1px solid #C8D4E3",
                    "border-radius": "3px",
                    "background-color": "white",
                    "vertical-align":"middle",
                    "text-align":"center"
                }, children=[
                html.Div(className='row', 
                    children=[
                        html.H6('Compra'),
                        html.H3('0.00', id='indicator_nuevo_cliente_compra'),
                ]),
            ]),
            html.Div(className='four columns',
                style={
                    "border":"1px solid #C8D4E3",
                    "border-radius": "3px",
                    "background-color": "white",
                    "vertical-align":"middle",
                    "text-align":"center"
                }, children=[
                html.Div(className='row', 
                    children=[
                        html.H6('Negocio'),
                        html.H3('0.00', id='indicator_nuevo_cliente_negocio'),
                ]),
            ]),
            html.Div(className='four columns', children=[
                    html.P('* Valoración asignada en relación a la disposiciones de la persona a entregar datos personales')
                ])
        ],
        className="row",
        style={"marginTop": "5px", "max height": "200px"},
    ),
]

######################################################################################################################
@app.callback(
    Output('nc_personal_info', 'children'),
    [Input('submit_new_case', 'n_clicks'),
    Input('personas_bd', 'children')],
    [
    State('new_case_rut','value')],
)
def personal_info_callback(n_clicks, personas_bd, rut):
    print('personal_info_callbacks')
    print("-",rut)
    if n_clicks > 0:
        personas_bd = pd.read_json(personas_bd, orient='split')

        existe_persona = personas_bd[personas_bd['rut_original'] == rut][dm.personal_info]
        if existe_persona.shape[0] > 0:
            print('Persona Existe')
        else:
            print('Persona No Existe')
            return 0

        data = []
        for index, value in existe_persona.iloc[0].iteritems():
            string = '{}:        {}'.format(index,value)
            data.append(html.Li(string))
        
        return data

    return [html.Li('Agrega un cliente')]
@app.callback(
    Output('nc_historical_info', 'children'),
    [Input('submit_new_case', 'n_clicks'),
    Input('personas_bd', 'children')],
    [
    State('new_case_rut','value')],
)
def historial_info_callback(n_clicks, personas_bd, rut):
    print('historial_info_callback')
    print("-",rut)
    if n_clicks > 0:
        personas_bd = pd.read_json(personas_bd, orient='split')

        existe_persona = personas_bd[personas_bd['rut_original'] == rut][dm.no_is_time_price]
        if existe_persona.shape[0] > 0:
            print('Persona Existe')
        else:
            print('Persona No Existe')
            return 0

        data = []
        for index, value in existe_persona.iloc[0].iteritems():
            string = '{}:        {}'.format(index,value)
            data.append(html.Li(string))
        
        return data

    return [html.Li('Agrega un cliente')]
##########################################################################################################
# MODAL BASIC
@app.callback(
    Output("new_case", "n_clicks"),
    [Input("cases_modal_close", "n_clicks"), # cierra modal
    Input("submit_new_case", "n_clicks")],  # submit modal
)
def close_modal_callback(n, n2):
    # print('close_modal_callback', n, n2)
    return 0

@app.callback(Output("cases_modal", "style"), 
    [Input("new_case", "n_clicks")])
def display_cases_modal_callback(n):
    # print('display_cases_modal_callback', n)
    if n > 0:
        print('Open Modal')
        return {"display": "block"}
    print('Close Modal')
    return {"display": "none"}

######################################################################################################################
@app.callback(
    Output("personas_bd", "children"),
    [Input('submit_new_case', 'n_clicks')],
       [
        State("new_case_tipo", "value"),
        State("new_case_rut", "value"),
        State("new_case_giro", "value"),
        State("new_case_razonsocial", "value"),
        State("new_case_nombre", "value"),
        State("new_case_apellidopaterno", "value"),
        State("new_case_apellidomaterno", "value"),
        State("new_case_rutcontacto", "value"),
        State("new_case_nombrecontacto", "value"),
        State("new_case_apellidocontacto", "value"),
        State("new_case_telcontacto", "value"),
        State("new_case_celcontacto", "value"),
        State("new_case_email", "value"),
        State("new_case_dirección", "value"),
        State("new_case_numero", "value"),
        State("new_case_depto", "value"),
        State("new_case_region", "value"),
        State("new_case_provincia", "value"),
        State("new_case_comuna", "value"),
        State("new_case_rangoedad", "value"),
        State("new_case_sexo", "value"),
        State("new_case_nacionalidad", "value"),
        State("new_case_estadocivil", "value"),
        State("new_case_nrogrupofamiliar", "value"),
        State("new_case_actividad", "value"),
        State("new_case_cargo", "value"),
        State("new_case_situacionlaboral", "value"),
        State("new_case_empleador", "value"),
        State("new_case_antiguedadlaboral", "value"),
        State("new_case_fechanacimiento", "value"),
        State("new_case_presencial", "value"),
        State("new_case_remoto", "value"),
        State("new_case_medioinicial", "value"),
        State("personas_bd", "children")
        ]
    # [Event('submit_new_case', 'n_click')]
)
def add_cliente_callback(n_clicks,
    tipo, rut, giro, razonsocial, nombre, apellidopaterno, apellidomaterno, rutcontacto, nombrecontacto,
    apellidocontacto, telcontacto, celcontacto, email, direccion, numero, depto, region, provincia,
    comuna, rangoedad, sexo, nacionalidad, estadocivil, nrogrupofamiliar, actividad, cargo, situacionlaboral,
    empleador, antiguedadlaboral, fechanacimiento, presencial, remoto, medio, 
    personas_bd
):
    print('add_cliente_callback')
    print('-submit_new_case n_clicks', n_clicks)
    if n_clicks > 0:
        personas_bd = pd.read_json(personas_bd, orient='split')
   
        #CHECK BD #############################################################################
        existe_persona = personas_bd[personas_bd['rut_original'] == rut]
        
        if existe_persona.shape[0] > 0:
            print("-La persona ya existe en la bd")
            return personas_bd.to_json(date_format='iso', orient='split')

        #TRANSFORM #############################################################################
        direccion = direccion + ' ' + str(numero) + ' '+ str(depto)
        nombre_completo = nombre + ' ' + apellidopaterno + ' ' + apellidomaterno

        save = ['apellido1','apellido2','celular','compra','negocio',
            'correo','direccion','edad', 'trabajo', 'rut', 'rut_original',
            'max_rango_edad', 'tipo_cliente', 'nombre'
            ]
        
        new = {
            #Info Personal
            'actividad' : [actividad], 
            'apellido1' : [apellidopaterno], #5
            'apellido2' : [apellidomaterno], #6
            'celular' : [celcontacto], #12
            'compra': [False],
            'negocio': [False],
            'correo' : [email],
            'direccion' : [direccion], #14
            'edad' : [rangoedad], #18
            'trabajo' : [cargo], 
            'situacion laboral' : [situacionlaboral],
            'empleador' : [empleador], 
            'region' : [region], #15
            'provincia' : [provincia], #16
            'comuna' : [comuna], #17
            'sexo' : [sexo], #19
            'max_rango_edad': [0],
            'tipo_cliente':[tipo], #1
            'rut':[rut], #2
            'rut_original':[rut],
            'giro' : [giro], #3
            'nombre' : [nombre], #4
            'nombre completo' : [nombre_completo], #7
            'rutcontacto' : [rutcontacto], #8
            'nombrecontacto' : [nombrecontacto], #9
            'apellidocontacto' : [apellidocontacto],  #10
            'telefono' :[ telcontacto], #11
            'nacionalidad' : [nacionalidad], #20
            'estado civil' : [estadocivil], #21
            'nrogrupofamiliar' : [nrogrupofamiliar], 
            'antiguedadlaboral': [antiguedadlaboral], 
            'fecha nacimiento' : [fechanacimiento], 
            'presencial' : [presencial], 
            'remoto' : [remoto], 
            'medio' : [medio]
            }
        
        df = pd.DataFrame.from_dict(new)
        tmp = df[save]
        df = transform_persona_is(df)
        df2 = add_persona_new_comp_cot(df)
        df2 = df2.assign(**tmp)
        df2 = transform_df_lower_accent(df2)
        # ADD TO BD #########################################################################################
        try:
            personas_bd = personas_bd.append(df2, ignore_index=True)
            print("-Se agrego nueva persona a BD: {}".format(rut), personas_bd.shape[0])
        except:
            print('-No se pudo agregar a la persona a la BD')
        
        # print("PERSONAS BD", personas_bd.shape)
        return personas_bd.to_json(date_format='iso', orient='split')
    return personas_bd


###################################################################################################################
# SHOW RANKS
@app.callback(
    Output("indicator_nuevo_cliente_negocio","children"),
    [Input('submit_new_case', 'n_clicks'),
    Input('personas_bd', 'children')],
    [
    State('new_case_rut','value')],
)
def nuevo_cliente_negocio_callback(n_clicks, personas_bd, rut):
    print('-nuevo_cliente_negocio_callback')
    
    if n_clicks > 0:
        df = pd.read_json(personas_bd, orient='split')
        df = df[dm.is_no_time_price]
        df = df.iloc[[-1]]
        df = transform_df_lower_accent(df)

        tmp = copy.deepcopy(dm.p_for_dummies)
        tmp = tmp.append(df, ignore_index=True)
        #Transform MODEL IS
        tmp = tmp[dm.is_no_time_price]
        dummies = pd.get_dummies(tmp)

        to_predict = dummies.tail()

        clf1 = dm.models['negocio_is']
        predict = clf1.predict(to_predict)
        predict_proba = clf1.predict_proba(to_predict)

        p = predict_proba[0][1]
        p = transform_prospect_display_text(p)
        p = html.H3('{}'.format(p))
        return p
    return "0.00"

@app.callback(
    Output("indicator_nuevo_cliente_compra","children"),
    [Input('submit_new_case', 'n_clicks'),
    Input('personas_bd', 'children')],
    [
    State('new_case_rut','value')],
)
def nuevo_cliente_compra_callback(n_clicks, personas_bd, rut):
    if n_clicks > 0:
        df = pd.read_json(personas_bd, orient='split')
        df = df[dm.is_no_time_price]
        df = df.iloc[[-1]]

        #Transform MODEL IS
        tmp = copy.deepcopy(dm.p_for_dummies)
        tmp = tmp.append(df, ignore_index=True)
        
        #Transform MODEL IS
        tmp = tmp[dm.is_no_time_price]
        dummies = pd.get_dummies(tmp)
        # print(dummies.columns)
        to_predict = dummies.iloc[-1]


        to_predict = np.array(to_predict.tolist()).reshape(1, -1)

        clf1 = dm.models['compra_is']
        # print('Compra')
        predict = clf1.predict(to_predict)
        predict_proba = clf1.predict_proba(to_predict)

        p = predict_proba[0][1]
        p = transform_prospect_display_text(p)
        p = html.H3('{}'.format(p))
        # print(predict, predict_proba[0][1])
        return p
    return '0.00'


##########################################################################################################
# MODAL DROPDOWNS
@app.callback(
    Output('new_case_provincia', 'options'),
    [Input('new_case_region', 'value')]
)
def modal_change_provincia(region):
    obj = [{"label": value, "value": value} for value in provincias[region]]
    return obj

@app.callback(
    Output('new_case_comuna', 'options'),
    [Input('new_case_provincia', 'value')]
)
def modal_change_comuna(provincia):
    obj = [{"label": value, "value": value} for value in comunas[provincia]]
    return obj

#####################################################################################################################

# @app.callback(
#     Output("personas_bd","children"),
#     [Input("nuevo_cliente","children"),],
#     [
#     State("personas_bd","children")],
#     # [Event('submit_new_case', 'click')]
# )
# def personas_bd_add_callback(n_cliente, personas_bd):
#     print(type(n_cliente), type(personas_bd))
#     if n_cliente == None:
#         print('cliente NONE')
#         return personas_bd.to_json(date_format='iso', orient='split')
#     if personas_bd == None: 
#         print('NONE')
#         return n_cliente.to_json(date_format='iso', orient='split')
#     if personas_bd.shape[0] == 0:
#         print('EMPTY')
#         return n_cliente.to_json(date_format='iso', orient='split')

#     # print(personas_bd.shape)
    
#     return 0
#     n_cliente = pd.read_json(nuevo_cliente, orient='split')
#     personas_bd = pd.read_json(personas_bd, orient='split')

#     personas_bd = personas_bd.append(n_cliente, ignore_index=True)

#     return personas_bd.to_json(date_format='iso', orient='split')