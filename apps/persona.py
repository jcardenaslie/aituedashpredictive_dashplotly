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

from app import app
import data_manager as dm
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 

from chile import regiones, provincias, comunas
from app import format_rut, indicator
from modales import modal_agregar_cotizacion
from transformation import transform_prospect_display_text

layout = [
        modal_agregar_cotizacion(),
        #Controles
        html.Div(className='row',children=[
            html.Div(className='six columns', children=[
                html.P('Buscar Rut:'),
                dcc.Input(
                    id='input_buscar_persona',
                    placeholder='ejemplo: 0000000-0',
                    type='text',
                    value='',
                    style={'width':'100%'}
                )
            ]),
            html.Div(className='three columns', children=[
                html.P('Proyecto:'),
                dcc.Dropdown(id='dropdown_modelo' ,
                    options=[
                        {'label': 'San Andres del Valle', 'value': 'sdv'},
                    ],
                    value='sdv'
                )]
            ),
            
        ]),

        html.Div(className='row', style={"text-align":'right', 'margin-top':'10px'},children=[
            html.Div(className='six columns ',
                style={"text-align":'right'}, 
                children=[
                    html.Button('Consultar',className='add', id='button_search'),
            ]),
            html.Div(
                className="six columns",
                style={"text-align":'left'},
                children=[
                    html.Span(
                        "Agregar Cotización",
                        id="new_cot",
                        n_clicks=0,
                        className="button button--secondary add",
                    ), 
                ]
            ),
        ]),
  
        html.Div(className='row', style={"margin-top":'10px'},children=[
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
                        html.Ul(id='list_personal_info' ,children=[
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
                        html.Ul(id='list_cotizaciones_info', 
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
                        html.H3('0.00', id='rank_compra'),
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
                        html.H3('0.00', id='rank_negocio'),
                ]),
            ]),
            html.Div(className='four columns', children=[
                    html.P('* Valoración asignado en base al comportamiento del cliente en sus cotizaciones, numero de veces que cotizo, tiempo entre cotizaciones, numero de viviendas, numero de veces que cotizo en un proyecto, etc..')
                ])
        ]),
]

##########################################################################################################
# MODAL NUEVA COTIZACION BASIC
@app.callback(
    # boton agregar
    Output("new_cot", "n_clicks"),
    [Input("new_cot_modal_close", "n_clicks"), # boton cerrar modal
    Input("submit_new_cot", "n_clicks")], # boton enviar form
)
def close_modal_callback(n, n2):
    return 0

@app.callback(
    Output("new_cot_modal", "style"), # el modal mismo
    [Input("new_cot", "n_clicks")] # boton agregar cot
    )
def open_new_cot_modal_callback(n):
    if n > 0:
        return {"display": "block"}
    return {"display": "none"}

################################################################################################
# MODAL NUEVA COTIZACION SUBMIT
# @app.callback(
#     Output("cot_all_bd", "children"),
#     [Input('submit_new_cot', 'n_clicks')],
#        [
#         State("new_cot_medio", "value"),
#         State("new_cot_tipodemedio", "value"),
#         State("new_cot_proyecto", "value"),
#         State("new_cot_etapa", "value"),
#         State("new_cot_presencial", "value"),
#         State("new_cot_remoto", "value"),
#         State("new_cot_productos", "value"),
#         State("new_cot_descuento", "value"),
#         State("new_cot_fecha", "value"),
#         State("new_cot_totalproductos", "value"),
#         State("new_cot_valorfinalventa", "value"),
#         State("cot_all_bd", "children"),
#         State("personas_bd_bd", "children"),
#         State("input_buscar_persona", "value"),
        
#         ]
#     # [Event('submit_new_case', 'n_click')]
# )
# def add_cotization(n_clicks, medio, tipomedio, proyecto, etapa, presencial,
#     remoto, productos, descuento, fecha, totalproductos, valorventafinal,
#     cot_all_bd, persona_bd, persona
#     ):

#     if n_clicks > 0:
#         # print(n_clicks, medio, tipomedio, proyecto, etapa, presencial,
#         #     remoto, productos, descuento, fecha, totalproductos, valorventafinal,
#         #     cot_all_bd, persona_bd, persona)
        
#         # atributes = ['rut_original', 'nombre', 'apellido1', 'apellido2', 'nombre completo', 'telefono'
#         # 'celular', 'correo', 'direccion', 'region', 'comuna', 'provincia', 'sexo', 'Estado Civil',
#         # 'edad', 'fecha nacimiento', 'tipo_cliente', 'razon social', 'giro', 'nacionalidad'
#         # 'nro grupo familiar', 'situacion laboral', 'empleador', 'antiguedad laboral', 'profesion']

#         # persona = personas_bd[personas_bd.rut == persona]
#         # print(persona)
#     return cot_all_bd
###################################################################################################
#Modal Dropdowns
@app.callback(
    Output('new_cot_tipodemedio', 'options'),
    [Input('new_cot_medio','value')]
    )
def modal_tipo_medio_callback(medio):
    obj = [{"label": value, "value": value} 
        for value in dm.cot_all[dm.cot_all['Medio'] == medio]['Tipo de Medio'].unique()]
    return obj

@app.callback(
    Output('new_cot_etapa', 'options'),
    [Input('new_cot_proyecto','value')]
    )
def modal_etapa_callback(proyecto):
    obj = [{"label": value, "value": value} 
        for value in dm.cot_all[dm.cot_all['Proyecto'] == proyecto]['Etapa'].unique()]
    return obj

@app.callback(
    # Output('productos_shop', 'children'),
    Output('new_cot_productos', 'options'),
    [
        Input('new_cot_etapa','value')
    ],

    )
def modal_productos_callback(etapa ):
    tmp = dm.productos[dm.productos['Etapa'] == etapa]
    tmp = tmp[tmp['Estado'] == 'Disponible']
    labels = tmp['Numero Unidad'].tolist()
    labels2 = tmp['Tipo Unidad'].tolist()
    values = tmp['ID'].tolist()

    obj = [{"label": str(label2) + "/ " + str(label), "value": value} 
        for label, label2, value in zip(labels, labels2, values)]

    return obj

@app.callback(
    Output('new_cot_totalproductos', 'value'),
    [Input('new_cot_productos', 'value'),
    ],
    )
def modal_tipo_medio_callback(productos):
    if isinstance(productos, str):
        productos = [productos]
    tmp = dm.productos[dm.productos['ID'].isin(productos)]
    total = tmp['Precio Lista'].sum()
    return total

@app.callback(
    Output('new_cot_valorfinalventa', 'value'),
    [Input('new_cot_totalproductos', 'value')]
)
def valor_total_venta_callback(total):
    print(total)
    return total
#############################################################################################################################
################## INFO PERSONAL Y COTIZACION DISPLAY
@app.callback(
    Output('list_personal_info', 'children'),
    [Input('button_search', 'n_clicks')],
    [State('dropdown_modelo', 'value'),
    State('input_buscar_persona', 'value'),
    State("personas_bd","children")]
)
def personal_info_callback(n_clicks, modelo, persona, personas_bd):
    if len(persona) <= 3: return [html.Li('Busca un Rut')]
    tmp = pd.read_json(personas_bd, orient='split')
    
    tmp = tmp[tmp['rut_original'] == persona]
    tmp = tmp[dm.personal_info].iloc[0] # personal info es un grupo de columnas

    data = []
    for index, value in tmp.iteritems():
        string = '{}:        {}'.format(index, value)
        data.append(html.Li(string))
    
    return data

@app.callback(
    Output('list_cotizaciones_info', 'children'),
    [Input('button_search', 'n_clicks')],
    [State('dropdown_modelo', 'value'),
    State('input_buscar_persona', 'value'),
    State("personas_bd","children")]
)
def cotizacion_info_callback(n_clicks, modelo, persona, personas_bd):
    if len(persona) <= 3: return [html.Li('Busca un Rut')]
    tmp = pd.read_json(personas_bd, orient='split')
    tmp = tmp[tmp['rut_original'] == persona]
    tmp = tmp[dm.no_is_time_price].iloc[0]

    data = []
    for index, value in tmp.iteritems():
        string = '{}:        {}'.format(index, value)
        data.append(html.Li(string))
    return data
####################################################################################################
#### PREDICCION
# @app.callback(
#     Output('rank_compra', 'children'),
#     [Input('button_search', 'n_clicks')],
#     [State('dropdown_modelo', 'value'),
#     State('input_buscar_persona', 'value'),
#     State("personas_bd","children")]
# )

# def compra_rank_callback(n_clicks, modelo, persona, personas_bd):
#     if len(persona) <= 3: return "0.00"

#     tmp = pd.read_json(personas_bd, orient='split')
#     to_predict = tmp[tmp.rut_original == persona]

#     print(to_predict.iloc[0])

#     # return 0
#     predictors = dm.no_is_time_price

#     index = to_predict.index
#     p_personas = tmp[predictors]
#     d_personas = pd.get_dummies(p_personas)

#     print(d_personas.columns)
#     return 0 
#     to_predict = d_personas.loc[index]

#     y_proba = dm.models['compra_nois'].predict_proba(to_predict)
#     y_pred = dm.models['compra_nois'].predict(to_predict)
#     # print('Compra', y_proba, y_pred)
#     p = html.H3('%.4f' % y_proba[:,1])
#     return p

# @app.callback(
#     Output('rank_negocio', 'children'),
#     [Input('button_search', 'n_clicks'),
#     Input('dropdown_modelo', 'value')],
#     [State('input_buscar_persona', 'value')]
# )
# def negocio_rank_callback(click, modelo, rut):
    # if len(rut) <= 3: return "0.00"
    # tmp_personas = copy.deepcopy(dm.personas_info)

    # predictors = dm.no_is_time_price

    # rut = format_rut(rut) 
    
    # to_predict = tmp_personas[tmp_personas.rut == rut]
    # # print(to_predict)
    # index = to_predict.index
    # # target = tmp_personas.negocio
    # p_personas = tmp_personas[predictors]
    # d_personas = pd.get_dummies(p_personas)

    # to_predict = d_personas.loc[index]

    # y_proba = dm.models['negocio_nois'].predict_proba(to_predict)
    # y_pred = dm.models['negocio_nois'].predict(to_predict)
    # # print('Negocio', y_proba, y_pred)
    # p = html.H3('%.4f' % y_proba[:,1])
    # return p
#######################################
@app.callback(
    Output('rank_compra', 'children'),
    [Input('button_search', 'n_clicks'),
    Input('dropdown_modelo', 'value')],
    [State('input_buscar_persona', 'value'),
    State('personas_bd', 'children')]
)
def compra_rank_callback(click, modelo, rut, personas_bd):
    if len(rut) <= 3: return "---"
    tmp = pd.read_json(personas_bd, orient='split')
    persona = tmp[tmp['rut_original'] == rut]
    index = persona.index

    tmp = tmp[dm.no_is_time_price]
    tmp = pd.get_dummies(tmp)
    to_predict = tmp.loc[index]

    y_proba = dm.models['compra_nois'].predict_proba(to_predict)
    y_pred = dm.models['compra_nois'].predict(to_predict)
    p = transform_prospect_display_text(y_proba[:,1])
    p = html.H3('{}'.format(p))
    return p

@app.callback(
    Output('rank_negocio', 'children'),
    [Input('button_search', 'n_clicks'),
    Input('dropdown_modelo', 'value')],
    [State('input_buscar_persona', 'value'),
    State('personas_bd', 'children')]
)
def negocio_rank_callback(click, modelo, rut, personas_bd):
    if len(rut) <= 3: return "---"
    tmp = pd.read_json(personas_bd, orient='split')
    persona = tmp[tmp['rut_original'] == rut]
    index = persona.index

    tmp = tmp[dm.no_is_time_price]
    tmp = pd.get_dummies(tmp)
    to_predict = tmp.loc[index]

    y_proba = dm.models['negocio_nois'].predict_proba(to_predict)
    y_pred = dm.models['negocio_nois'].predict(to_predict)
    p = transform_prospect_display_text(y_proba[:,1])
    p = html.H3('{}'.format(p))
    return p