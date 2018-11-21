import os, time, copy
from textwrap import dedent

import dash
import dash_core_components as dcc
import dash_html_components as html
import numpy as np
import pandas as pd
from dash.dependencies import Input, Output, State
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn import datasets
from sklearn.svm import SVC

import utils.dash_reusable_components as drc

from sklearn.externals import joblib

from app import app, df_to_table

import data_manager as dm

layout = [
    html.Div(className='row', children=[
        #Controles
        html.Div(
            className='one columns',
            style={
                'min-width': '20.0%',
                'max-height': 'calc(100vh - 85px)',
                'overflow-y': 'auto',
                'overflow-x': 'hidden',
                "backgroundColor": "white",
                "border": "1px solid #C8D4E3",
                "borderRadius": "3px",
                "padding": "20px"
            },
            children=[
                # drc.Card([
                
                # ]),
                drc.NamedDropdown(
                    name='Modelo',
                    id='dropdown-rank-modelo',
                    options=[
                        {'label': 'San Andres del Valle', 'value': 'sdv'},
                    ],
                    clearable=False,
                    searchable=False,
                    value='sdv'
                ),
                drc.NamedDropdown(
                    name='Cotizantes Set',
                    id='dropdown-rank-dataset',
                    options=[
                        {'label': 'Test', 'value': 'test'},
                    ],
                    clearable=False,
                    searchable=False,
                    value='test'
                ),
            ]
        ),
        #Lista Ranking Negocio
        html.Div(
            className="five columns",
            style={
                "backgroundColor": "white",
                "border": "1px solid #C8D4E3",
                "borderRadius": "3px",
                "text-align": "center"
            },
            children=[
                html.H6(
                    "Ranking Negocio",
                ),
                drc.Card(style={"padding":"0px"}, children=[
                    html.Div([
                        html.Div(
                            id="negocio_opportunities",
                            style={
                                "padding": "0px 13px 5px 13px", 
                                "marginBottom": "5", 
                                'fontSize':'1.3rem',
                            },
                        )
                    ],
                        style={
                            "height": "100%",
                            'height':'500px',
                            "overflowY": "scroll",
                        },
                    ),
                ]),  
            ]
        ), 
        #Lista Ranking Negocio
        html.Div(
            className="five columns",
            style={
                "backgroundColor": "white",
                "border": "1px solid #C8D4E3",
                "borderRadius": "3px",
                "text-align": "center"
            },
            children=[
                html.H6(
                    "Ranking Negocio",
                ),
                drc.Card(style={"padding":"0px"}, children=[
                    html.Div([
                        html.Div(
                            id="compra_opportunities",
                            style={
                                "padding": "0px 13px 5px 13px", 
                                "marginBottom": "5", 
                                'fontSize':'1.3rem',
                            },
                        )
                    ],
                        style={
                            "height": "100%",
                            'height':'500px',
                            "overflowY": "scroll",
                        },
                    ),
                ]),  
            ]
        ), 
    ]),
]

#########################################################################################################################
############### LISTAS RANKEADas
@app.callback(
    Output('negocio_opportunities', 'children'),
    [Input('dropdown-rank-dataset','value'),
    Input('dropdown-rank-modelo','value')
    ]
)
def rank_list_negocio_callback(dataset, modelo):
    start_time = time.time()
    personas = dm.personas

    personas_info = dm.personas_info
    X_test_m = dm.X_test_m
    y_test_m = dm.y_test_m


    personas = copy.deepcopy(personas)
    b_personas = copy.deepcopy(X_test_m)
    b_p_negocio = copy.deepcopy(y_test_m)

    b_personas['target'] = b_p_negocio
    b_personas['y_pred'] = dm.models['negocio_nois'].predict(X_test_m)
    b_personas['t_proba'] = dm.models['negocio_nois'].predict_proba(X_test_m)[:,1]
    
    new = personas.merge(b_personas, left_index=True, right_index=True)
    
    new2 = new.merge(personas_info, left_on='rut', right_on='rut', how='left')
    df = new2[['rut', 'nombre','correo','t_proba', 'y_pred','target','nro_cot_depto_y','nro_cot_depto_x']]
    df = df.sort_values(by='t_proba', ascending=False)
    
    df = df.head(30)
    # print('NEGOCIO',df)
    return df_to_table(df)

@app.callback(
    Output('compra_opportunities', 'children'),
    [Input('dropdown-rank-dataset','value'),
    Input('dropdown-rank-modelo','value')
    ]
)

def rank_list_compra_callback(dataset, modelo):

    personas = dm.personas
    personas_info = dm.personas_info
    X_test_m = dm.X_test_m
    y_test_m = dm.y_test_m


    personas = copy.deepcopy(personas)
    b_personas = copy.deepcopy(X_test_m)
    b_p_negocio = copy.deepcopy(y_test_m)


    b_personas['target'] = b_p_negocio
    b_personas['y_pred'] = dm.models['compra_nois'].predict(X_test_m)
    b_personas['t_proba'] = dm.models['compra_nois'].predict_proba(X_test_m)[:,1]
    
    new = personas.merge(b_personas, left_index=True, right_index=True)
    

    new2 = new.merge(personas_info, left_on='rut', right_on='rut', how='left')
    df = new2[['rut', 'nombre','correo','t_proba', 'y_pred','target','nro_cot_depto_y','nro_cot_depto_x']]
    df = df.sort_values(by='t_proba', ascending=False)
    
    df = df.head(30)
    # print('COMPRA',df)
    return df_to_table(df)

