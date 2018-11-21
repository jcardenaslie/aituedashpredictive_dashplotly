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
from nuevo_cliente import modal

from app import app
import data_manager as dm
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 

from chile import regiones, provincias, comunas
from transformation import transform
from app import format_rut, indicator

layout = [
    modal(),
    # add button
    html.Div(
            html.Span(
                    "Agregar Cliente",
                    id="new_case",
                    n_clicks=0,
                    className="button button--secondary add",
                    
                ),
                className="twelve columns",
                style={"float": "right"},
    ),

     html.Div([
        indicator(
            "#00cc96",
            "Negocio",
            "indicator_nuevo_cliente_negocio",
        ),
        indicator(
            "#119DFF",
            "Compra",
            "indicator_nuevo_cliente_compra",
        ),

    ]),
    # tables row div
    html.Div(
        [
            html.Div(
                [
                    html.P(
                        "Información Cliente",
                        style={
                            "color": "#2a3f5f",
                            "fontSize": "13px",
                            "textAlign": "center",
                            "marginBottom": "0",
                        },
                    ),
                    html.Div(
                        id="info_cliente",
                        style={"padding": "0px 13px 5px 13px", "marginBottom": "5"},
                    ),
                   
                ],
                className="six columns",
                style={
                    "backgroundColor": "white",
                    "border": "1px solid #C8D4E3",
                    "borderRadius": "3px",
                    "height": "100%",
                    "overflowY": "scroll",
                },
            ),
            html.Div(
                [
                    html.P(
                        "Comportamiento Cotizaciones",
                        style={
                            "color": "#2a3f5f",
                            "fontSize": "13px",
                            "textAlign": "center",
                            "marginBottom": "0",
                        },
                    ),
                    html.Div(
                        id="comp_cotizaciones",
                        style={"padding": "0px 13px 5px 13px", "marginBottom": "5"},
                    )
                ],
                className="six columns",
                style={
                    "backgroundColor": "white",
                    "border": "1px solid #C8D4E3",
                    "borderRadius": "3px",
                    "height": "100%",
                    "overflowY": "scroll",
                },
            ),
        ],
        className="row",
        style={"marginTop": "5px", "max height": "200px"},
    ),
]


##########################################################################################################
# MODAL
@app.callback(
    Output("new_case", "n_clicks"),
    [Input("cases_modal_close", "n_clicks"), Input("submit_new_case", "n_clicks")],
)
def close_modal_callback(n, n2):
    return 0

@app.callback(Output("cases_modal", "style"), [Input("new_case", "n_clicks")])
def display_cases_modal_callback(n):
    if n > 0:
        return {"display": "block"}
    return {"display": "none"}


@app.callback(
    Output("cases_df", "children"),
    [Input("submit_new_case", "n_clicks")],
    [
        State("new_case_account", "value"),
        State("new_case_origin", "value"),
        State("new_case_reason", "value"),
        State("new_case_subject", "value"),
        State("new_case_contact", "value"),
        State("new_case_type", "value"),
        State("new_case_status", "value"),
        State("new_case_description", "value"),
        State("new_case_priority", "value"),
        State("cases_df", "children"),
    ],
)
def add_case_callback(
    n_clicks, account_id, origin, reason, subject, contact_id, case_type, status, description, priority, current_df
    ):
    if n_clicks > 0:
        query = {
            "AccountId": account_id,
            "Origin": origin,
            "Reason": reason,
            "Subject": subject,
            "ContactId": contact_id,
            "Type": case_type,
            "Status": status,
            "Description": description,
            "Priority": priority,
        }

        sf_manager.add_case(query)
        df = sf_manager.get_cases()
        return df.to_json(orient="split")

    return current_df

##########################################################################################################
# MODAL INPUTS
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

@app.callback(
    Output("nuevo_cliente", "children"),
    [],
    # [Input("submit_new_case", "n_clicks")],
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
        State("new_case_medioinicial", "value")
    ],
    [Event('submit_new_case', 'click')]
)

def add_opportunity_callback(
    tipo, rut, giro, razonsocial, nombre, apellidopaterno, apellidomaterno, rutcontacto, nombrecontacto,
    apellidocontacto, telcontacto, celcontacto, email, direccion, numero, depto, region, provincia,
    comuna, rangoedad, sexo, nacionalidad, estadocivil, nrogrupofamiliar, actividad, cargo, situacionlaboral,
    empleador, antiguedadlaboral, fechanacimiento, presencial, remoto, medio
):
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
    
    df = pd.DataFrame.from_dict(new)
    return df.to_json(date_format='iso', orient='split')

@app.callback(
    Output("indicator_nuevo_cliente_negocio","children"),
    [Input("nuevo_cliente","children")]
)
def nuevo_cliente_negocio_callback(jsondf):
    df = pd.read_json(jsondf, orient='split')
    #TRANSFORM
    df = transform(df)
        
    tmp = copy.deepcopy(dm.p_for_dummies)
    tmp = tmp.append(df, ignore_index=True)
    tmp = tmp[dm.is_no_time_price]
    dummies = pd.get_dummies(tmp)
    # print(dummies.columns)
    to_predict = dummies.iloc[-1]
    to_predict = np.array(to_predict.tolist()).reshape(1, -1)

    clf1 = dm.models['negocio_is']
    print('Negocio')
    predict = clf1.predict(to_predict)
    predict_proba = clf1.predict_proba(to_predict)

    print(predict, predict_proba[0][1])
    return "%.3f"%predict_proba[0][1]

@app.callback(
    Output("indicator_nuevo_cliente_compra","children"),
    [Input("nuevo_cliente","children")]
)
def nuevo_cliente_negocio_callback(jsondf):
    df = pd.read_json(jsondf, orient='split')
    #TRANSFORM
    df = transform(df)
        
    tmp = copy.deepcopy(dm.p_for_dummies)
    tmp = tmp.append(df, ignore_index=True)
    tmp = tmp[dm.is_no_time_price]
    dummies = pd.get_dummies(tmp)

    to_predict = dummies.iloc[-1]
    to_predict = np.array(to_predict.tolist()).reshape(1, -1)

    clf1 = dm.models['compra_is']
    print('Negocio')
    predict = clf1.predict(to_predict)
    predict_proba = clf1.predict_proba(to_predict)

    print(predict, predict_proba[0][1])
    return "%.3f"%predict_proba[0][1]


#######################################################################################################################################
#     @app.callback(
#     Output("opportunities_df", "children"),
#     [Input("submit_new_case", "n_clicks")],
#     [
#         State("new_case_tipo", "value"),
#         State("new_case_rut", "value"),
#         State("new_case_giro", "value"),
#         State("new_case_razonsocial", "value"),
#         State("new_case_nombre", "value"),
#         State("new_case_apellidopaterno", "value"),
#         State("new_case_apellidomaterno", "value"),
#         State("new_case_rutcontacto", "value"),
#         State("new_case_nombrecontacto", "value"),
#         State("new_case_apellidocontacto", "value"),
#         State("new_case_telcontacto", "value"),
#         State("new_case_celcontacto", "value"),
#         State("new_case_email", "value"),
#         State("new_case_dirección", "value"),
#         State("new_case_numero", "value"),
#         State("new_case_depto", "value"),
#         State("new_case_region", "value"),
#         State("new_case_provincia", "value"),
#         State("new_case_comuna", "value"),
#         State("new_case_rangoedad", "value"),
#         State("new_case_sexo", "value"),
#         State("new_case_nacionalidad", "value"),
#         State("new_case_estadocivil", "value"),
#         State("new_case_nrogrupofamiliar", "value"),
#         State("new_case_actividad", "value"),
#         State("new_case_cargo", "value"),
#         State("new_case_situacionlaboral", "value"),
#         State("new_case_empleador", "value"),
#         State("new_case_antiguedadlaboral", "value"),
#         State("new_case_fechanacimiento", "value"),
#         State("new_case_presencial", "value"),
#         State("new_case_remoto", "value"),
#         State("new_case_medioinicial", "value"), #31

#     ],
# )
# def add_opportunity_callback(
#     n_clicks, tipo, rut, giro, razonsocial, nombre, apellidopaterno, apellidomaterno, rutcontacto, nombrecontacto,
#     apellidocontacto, telcontacto, celcontacto, email, direccion, numero, depto, region, provincia,
#     comuma, rangoedad, sexo, nacionalidad, estadocivil, nrogrupofamiliar, actividad, cargo, situacionlaboral,
#     empleador, antiguedadlaboral, fechanacimiento, presencial, remoto, medio
# ):
#     # print(n_clicks, tipo, rut, giro, nombre, apellidopaterno, apellidomaterno, rutcontacto, nombrecontacto,
#     # apellidocontacto, telcontacto, celcontacto, email, direccion, numero, depto, region, provincia,
#     # comuma, rangoedad, sexo, nacionalidad, estadocivil, nrogrupofamiliar, actividad, cargo, situacionlaboral,
#     # empleador, antiguedadlaboral, fechanacimiento, presencial, remoto, medio)
    
#     df = transform(tipo, rut, giro, nombre, apellidopaterno, apellidomaterno, rutcontacto, nombrecontacto,
#     apellidocontacto, telcontacto, celcontacto, email, direccion, numero, depto, region, provincia,
#     comuma, rangoedad, sexo, nacionalidad, estadocivil, nrogrupofamiliar, actividad, cargo, situacionlaboral,
#     empleador, antiguedadlaboral, fechanacimiento, presencial, remoto, medio)

#     # print(df.head())

#     tmp = copy.deepcopy(dm.p_for_dummies)
#     tmp = tmp.append(df, ignore_index=True)
#     tmp = tmp[dm.is_no_time_price]
#     dummies = pd.get_dummies(tmp)

#     # print(dummies.shape)
#     print(dummies.columns)

#     to_predict = dummies.iloc[-1]
#     print(to_predict.shape, type(to_predict), to_predict.tolist())
#     # return to_predict.to_json(date_format='iso', orient='split')

#     to_predict = np.array(to_predict.tolist()).reshape(1, -1)
#     # print(to_predict.shape)
#     # print(np.isnan(to_predict))
    
#     set1 = dummies.columns


#     clf1 = dm.models['negocio_is']
#     print('Negocio')
#     print(clf1.predict(to_predict))
#     print(clf1.predict_proba(to_predict))

#     clf2 = dm.models['compra_is']
#     print('Compra')
#     print(clf2.predict(to_predict))
#     print(clf2.predict_proba(to_predict))
    
#     return 0