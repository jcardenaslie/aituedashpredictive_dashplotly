import os
import time, timeit
from textwrap import dedent

import dash
import dash_core_components as dcc
import dash_html_components as html
import numpy as np
import pandas as pd
from dash.dependencies import Input, Output, State

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
            "left_cases_indicator",
        ),
        indicator(
            "#119DFF",
            "Compra",
            "middle_cases_indicator",
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


# add new opportunity to salesforce and stores new df in hidden div
# @app.callback(
#     Output("opportunities_df", "children"),
#     [Input("submit_new_case", "n_clicks")],
#     [
#         State("new_case_tipo", "value"),
#         State("new_case_rut", "value"),
#         State("new_case_giro", "value"),
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
#     n_clicks, tipo, rut, giro, nombre, apellidopaterno, apellidomaterno, rutcontacto, nombrecontacto,
#     apellidocontacto, telcontacto, celcontacto, email, direccion, numero, depto, region, provincia,
#     comuma, rangoedad, sexo, nacionalidad, estadocivil, nrogrupofamiliar, actividad, cargo, situacionlaboral,
#     empleador, antiguedadlaboral, fechanacimiento, presencial, remoto, medio
# ):
#     df = transform(tipo, rut, giro, nombre, apellidopaterno, apellidomaterno, rutcontacto, nombrecontacto,
#     apellidocontacto, telcontacto, celcontacto, email, direccion, numero, depto, region, provincia,
#     comuma, rangoedad, sexo, nacionalidad, estadocivil, nrogrupofamiliar, actividad, cargo, situacionlaboral,
#     empleador, antiguedadlaboral, fechanacimiento, presencial, remoto, medio)

#     tmp = copy.deepcopy(dm.personas)
#     tmp = tmp.append(df, ignore_index=True)
#     tmp = tmp[dm.is_no_time_price]
#     dummies = pd.get_dummies(tmp)

#     print(dummies.shape)
#     print(dummies.columns)

#     to_predict = dummies.iloc[-1]
#     print(to_predict)
#     return to_predict.to_json(date_format='iso', orient='split')

#     to_predict = to_predict.reshape(1, -1)
#     # print(to_predict.shape)
#     # print(np.isnan(to_predict))
    

#     clf1 = dm.models['negocio_is']
#     print('Negocio')
#     print(clf1.predict(to_predict))
#     print(clf1.predict_proba(to_predict))

#     clf2 = dm.models['compra_is']
#     print('Compra')
#     print(clf2.predict(to_predict))
#     print(clf2.predict_proba(to_predict))
    
#     return 0

@app.callback(
    Output("opportunities_df", "children"),
    [Input("submit_new_case", "n_clicks")],
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
        State("new_case_medioinicial", "value"), #31

    ],
)
def add_opportunity_callback(
    n_clicks, tipo, rut, giro, razonsocial, nombre, apellidopaterno, apellidomaterno, rutcontacto, nombrecontacto,
    apellidocontacto, telcontacto, celcontacto, email, direccion, numero, depto, region, provincia,
    comuma, rangoedad, sexo, nacionalidad, estadocivil, nrogrupofamiliar, actividad, cargo, situacionlaboral,
    empleador, antiguedadlaboral, fechanacimiento, presencial, remoto, medio
):
    # print(n_clicks, tipo, rut, giro, nombre, apellidopaterno, apellidomaterno, rutcontacto, nombrecontacto,
    # apellidocontacto, telcontacto, celcontacto, email, direccion, numero, depto, region, provincia,
    # comuma, rangoedad, sexo, nacionalidad, estadocivil, nrogrupofamiliar, actividad, cargo, situacionlaboral,
    # empleador, antiguedadlaboral, fechanacimiento, presencial, remoto, medio)
    
    df = transform(tipo, rut, giro, nombre, apellidopaterno, apellidomaterno, rutcontacto, nombrecontacto,
    apellidocontacto, telcontacto, celcontacto, email, direccion, numero, depto, region, provincia,
    comuma, rangoedad, sexo, nacionalidad, estadocivil, nrogrupofamiliar, actividad, cargo, situacionlaboral,
    empleador, antiguedadlaboral, fechanacimiento, presencial, remoto, medio)

    # print(df.head())

    tmp = copy.deepcopy(dm.p_for_dummies)
    tmp = tmp.append(df, ignore_index=True)
    tmp = tmp[dm.is_no_time_price]
    dummies = pd.get_dummies(tmp)

    # print(dummies.shape)
    print(dummies.columns)

    to_predict = dummies.iloc[-1]
    print(to_predict.shape, type(to_predict), to_predict.tolist())
    # return to_predict.to_json(date_format='iso', orient='split')

    to_predict = np.array(to_predict.tolist()).reshape(1, -1)
    # print(to_predict.shape)
    # print(np.isnan(to_predict))
    
    set1 = dummies.columns


    clf1 = dm.models['negocio_is']
    print('Negocio')
    print(clf1.predict(to_predict))
    print(clf1.predict_proba(to_predict))

    clf2 = dm.models['compra_is']
    print('Compra')
    print(clf2.predict(to_predict))
    print(clf2.predict_proba(to_predict))
    
    return 0