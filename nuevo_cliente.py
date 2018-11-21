import dash
import dash_core_components as dcc
import dash_html_components as html
from chile import regiones, provincias, comunas

def modal():
    return html.Div(
        html.Div([
            html.Div([
                # modal header
                html.Div([
                    html.Span(
                        "Agregar Cliente",
                        style={
                            "color": "#506784",
                            "fontWeight": "bold",
                            "fontSize": "20",
                        },
                    ),
                    html.Span(
                        "×",
                        id="cases_modal_close",
                        n_clicks=0,
                        style={
                            "float": "right",
                            "cursor": "pointer",
                            "marginTop": "0",
                            "marginBottom": "17",
                        },
                    ),
                ],
                    className="row",
                    style={"borderBottom": "1px solid #C8D4E3"},
                ),
                # modal form
                html.Div([
                    # left Div
                    html.Div([
                        #Tipo Cliente
                        html.P(
                            "Tipo",
                            style={
                                "textAlign": "left",
                                "marginBottom": "2",
                                "marginTop": "4",
                            },
                        ),
                        html.Div(
                            dcc.Dropdown(
                                id="new_case_tipo",
                                options=[
                                    {"label": "Natural", "value": "Natural"},
                                    {"label": "Jurídico", "value": "Jurídico"},
                                ], value="Natural", clearable=False
                            ),
                        ),
                        #RUT
                        html.P(
                            "*RUT",
                            style={
                                "textAlign": "left",
                                "marginBottom": "2",
                                "marginTop": "4",
                            },
                        ),
                        dcc.Input(
                            id="new_case_rut",
                            placeholder="9999999-9",
                            type="text",
                            value="9999999-9",
                            style={"width": "100%"},
                        ),
                        #Giro
                        html.P(
                        "Giro",
                            style={
                                "textAlign": "left",
                                "marginBottom": "2",
                                "marginTop": "4",
                            },
                        ),
                                        dcc.Input(
                                            id="new_case_giro",
                                            placeholder="giro",
                                            type="text",
                                            value="giro",
                                            style={"width": "100%"},
                                        ),
                                        #Razon Social
                                        html.P(
                                            "Razón Social",
                                            style={
                                                "textAlign": "left",
                                                "marginBottom": "2",
                                                "marginTop": "4",
                                            },
                                        ),
                                        dcc.Input(
                                            id="new_case_razonsocial",
                                            placeholder="razonsocial",
                                            type="text",
                                            value="razonsocial",
                                            style={"width": "100%"},
                                        ),
                                        #Nombre
                                        html.P(
                                            "Nombre",
                                            style={
                                                "textAlign": "left",
                                                "marginBottom": "2",
                                                "marginTop": "4",
                                            },
                                        ),
                                        dcc.Input(
                                            id="new_case_nombre",
                                            placeholder="nombre",
                                            type="text",
                                            value="nombre",
                                            style={"width": "100%"},
                                        ),
                                        #Apellido Paterno
                                        html.P(
                                            "*Apellido Paterno",
                                            style={
                                                "textAlign": "left",
                                                "marginBottom": "2",
                                                "marginTop": "4",
                                            },
                                        ),
                                        dcc.Input(
                                            id="new_case_apellidopaterno",
                                            placeholder="appaterno",
                                            type="text",
                                            value="apaterno",
                                            style={"width": "100%"},
                                        ),
                                        #Apellido Materno
                                        html.P(
                                            "*Apellido Materno",
                                            style={
                                                "textAlign": "left",
                                                "marginBottom": "2",
                                                "marginTop": "4",
                                            },
                                        ),
                                        dcc.Input(
                                            id="new_case_apellidomaterno",
                                            placeholder="apmaterno",
                                            type="text",
                                            value="apmaterno",
                                            style={"width": "100%"},
                                        ),
                                        #Rut Contacto
                                        html.P(
                                            "Rut Contacto",
                                            style={
                                                "textAlign": "left",
                                                "marginBottom": "2",
                                                "marginTop": "4",
                                            },
                                        ),
                                        dcc.Input(
                                            id="new_case_rutcontacto",
                                            placeholder="9999999-9",
                                            type="text",
                                            value="9999999-9",
                                            style={"width": "100%"},
                                        ),
                                        #Nombre Contacto
                                        html.P(
                                            "Nombre Contacto",
                                            style={
                                                "textAlign": "left",
                                                "marginBottom": "2",
                                                "marginTop": "4",
                                            },
                                        ),
                                        dcc.Input(
                                            id="new_case_nombrecontacto",
                                            placeholder="nombrecontacto",
                                            type="text",
                                            value="nombrecontacto",
                                            style={"width": "100%"},
                                        ),
                                        #Apellido Contacto
                                        html.P(
                                            "Apellido Contacto",
                                            style={
                                                "textAlign": "left",
                                                "marginBottom": "2",
                                                "marginTop": "4",
                                            },
                                        ),
                                        dcc.Input(
                                            id="new_case_apellidocontacto",
                                            placeholder="apellidocontacto",
                                            type="text",
                                            value="apellidocontacto",
                                            style={"width": "100%"},
                                        ),
                                        # Telefono De Contacto
                                        html.P(
                                            "Telefono De Contacto",
                                            style={
                                                "textAlign": "left",
                                                "marginBottom": "2",
                                                "marginTop": "4",
                                            },
                                        ),
                                        dcc.Input(
                                            id="new_case_telcontacto",
                                            placeholder="89999999",
                                            type="text",
                                            value="89999999",
                                            style={"width": "100%"},
                                        ),
                                        #Celular de Contacto
                                        html.P(
                                            "*Celular De Contacto",
                                            style={
                                                "textAlign": "left",
                                                "marginBottom": "2",
                                                "marginTop": "4",
                                            },
                                        ),
                                        dcc.Input(
                                            id="new_case_celcontacto",
                                            placeholder="79999999",
                                            type="text",
                                            value="79999999",
                                            style={"width": "100%"},
                                        ),
                                        #Email
                                        html.P(
                                            "*Email",
                                            style={
                                                "textAlign": "left",
                                                "marginBottom": "2",
                                                "marginTop": "4",
                                            },
                                        ),
                                        dcc.Input(
                                            id="new_case_email",
                                            placeholder="tucorreo@correo.cl",
                                            type="email",
                                            value="tucorreo@correo.cl",
                                            style={"width": "100%"},
                                        ),
                                        
                                    ],
                                    className="four columns",
                                    style={"paddingRight": "15"},
                                ),

                                # left Div
                                html.Div(
                                    [
                                        #Direccion
                                        html.P(
                                            "Dirección",
                                            style={
                                                "textAlign": "left",
                                                "marginBottom": "2",
                                                "marginTop": "4",
                                            },
                                        ),
                                        dcc.Input(
                                            id="new_case_dirección",
                                            placeholder="Av. Principal 101",
                                            type="text",
                                            value="Av. Principal",
                                            style={"width": "100%"},
                                        ),
                                        #Numero
                                        html.P(
                                            "Numero",
                                            style={
                                                "textAlign": "left",
                                                "marginBottom": "2",
                                                "marginTop": "4",
                                            },
                                        ),
                                        dcc.Input(
                                            id="new_case_numero",
                                            placeholder="1",
                                            type="number",
                                            value="1",
                                            style={"width": "100%"},
                                        ),
                                        #Depto
                                        html.P(
                                            "Depto",
                                            style={
                                                "textAlign": "left",
                                                "marginBottom": "2",
                                                "marginTop": "4",
                                            },
                                        ),
                                        dcc.Input(
                                            id="new_case_depto",
                                            placeholder="1",
                                            type="number",
                                            value="1",
                                            style={"width": "100%"},
                                        ),
                                        #Región
                                        html.P(
                                            "*Región",
                                            style={
                                                "textAlign": "left",
                                                "marginBottom": "2",
                                                "marginTop": "4",
                                            },
                                        ),
                                        dcc.Dropdown(
                                            id="new_case_region",
                                            options=[
                                                {
                                                    "label": value,
                                                    "value": value,
                                                }
                                                for value in regiones
                                            ],
                                            value='VIII Región del Bío-Bío',
                                        ),
                                        #Provincia
                                        html.P(
                                            "*Provincia",
                                            style={
                                                "textAlign": "left",
                                                "marginBottom": "2",
                                                "marginTop": "4",
                                            },
                                        ),
                                        dcc.Dropdown(
                                            id="new_case_provincia",
                                            options=[
                                                {
                                                    "label": value,
                                                    "value": value,
                                                }
                                                for value in []
                                            ],
                                            value="Concepción",
                                        ),
                                        #Comuna
                                        html.P(
                                            "*Comuna",
                                            style={
                                                "textAlign": "left",
                                                "marginBottom": "2",
                                                "marginTop": "4",
                                            },
                                        ),
                                        dcc.Dropdown(
                                            id="new_case_comuna",
                                            options=[
                                                {
                                                    "label": value,
                                                    "value": value,
                                                }
                                                for value in []
                                            ],
                                            value="Concepción",
                                        ),
                                    ],
                                    className="four columns",
                                    style={"paddingRight": "15"},
                                ),


                                # right Div
                                html.Div(
                                    [
                                        #Rango de Edad
                                        html.P(
                                            "Rango De Edad",
                                            style={
                                                "textAlign": "left",
                                                "marginBottom": "2",
                                                "marginTop": "4",
                                            },
                                        ),
                                        dcc.Dropdown(
                                            id="new_case_rangoedad",
                                            options=[
                                                {
                                                    "label": value,
                                                    "value": value,
                                                }
                                                for value in ['20-30', '31-40', '41-50', '61+', '51-60', 'Sin Información',
                                                              '15-19']
                                            ],
                                            value="Sin Información",
                                        ),
                                        #Sexo
                                        html.P(
                                            "Sexo",
                                            style={
                                                "textAlign": "left",
                                                "marginBottom": "2",
                                                "marginTop": "4",
                                            },
                                        ),
                                        dcc.Dropdown(
                                            id="new_case_sexo",
                                            options=[
                                                {
                                                    "label": "Masculino",
                                                    "value": "Masculino",
                                                },
                                                {
                                                    "label": "Femenino",
                                                    "value": "Femenino",
                                                },
                                                {
                                                    "label": "Sin Información",
                                                    "value": "Sin Información",
                                                },
                                            ],
                                            value="Sin Información",
                                        ),
                                        #Fecha de Nacimiento
                                        html.P(
                                            "Fecha De Nacimiento",
                                            style={
                                                "textAlign": "left",
                                                "marginBottom": "2",
                                                "marginTop": "4",
                                            },
                                        ),
                                        dcc.Input(
                                            id="new_case_fechanacimiento",
                                            placeholder="",
                                            type="date",
                                            value="01-01-1990",
                                            style={"width": "100%"},
                                        ),
                                        #Nacionalidad
                                        html.P(
                                            "Nacionalidad",
                                            style={
                                                "textAlign": "left",
                                                "marginBottom": "2",
                                                "marginTop": "4",
                                            },
                                        ),
                                        dcc.Dropdown(
                                            id="new_case_nacionalidad",
                                            options=[
                                                {   
                                                    "label": value, 
                                                    "value": value
                                                }
                                                for value in ['Chilena', 'Argentina', 'Extranjera', 'Colombiana',
                                                               'Uruguaya', 'Alemana', 'Venezolana', 'Ecuatoriana',
                                                               'Sin Información', 'China', 'Cubana', 'Brasileña', 'Boliviana',
                                                               'Peruana', 'Española']
                                            ],
                                            value="Sín Información",
                                        ),
                                        #Estado Civil
                                        html.P(
                                            "Estado Civil",
                                            style={
                                                "textAlign": "left",
                                                "marginBottom": "2",
                                                "marginTop": "4",
                                            },
                                        ),
                                        dcc.Dropdown(
                                            id="new_case_estadocivil",
                                            options=[
                                                {   
                                                    "label": value, 
                                                    "value": value
                                                }
                                                for value in ['Soltero(a)', 'Casado(a)', 'Sin Información', 'Divorciado(a)', \
                                                                'Separado(a)', 'Viudo(a)', 'Soltero', 'Casado', \
                                                                'Conviviente Civil']
                                            ],
                                            value="Sin Información",
                                        ),
                                        #Nro Grupo Familiar
                                        html.P(
                                            "Nro Grupo Familiar",
                                            style={
                                                "textAlign": "left",
                                                "marginBottom": "2",
                                                "marginTop": "4",
                                            },
                                        ),
                                        dcc.Dropdown(
                                            id="new_case_nrogrupofamiliar",
                                            options=[
                                                {   
                                                    "label": value, 
                                                    "value": value
                                                }
                                                for value in [2, 3, 'Sin Información', 5, 8, 4, 1, 6, 7]
                                            ],
                                            value="Sin Información",
                                        ),
                                        #Actividad
                                        html.P(
                                            "Actividad",
                                            style={
                                                "textAlign": "left",
                                                "marginBottom": "2",
                                                "marginTop": "4",
                                            },
                                        ),
                                        dcc.Dropdown(
                                            id="new_case_actividad",
                                            options=[
                                                {   
                                                    "label": value, 
                                                    "value": value
                                                }
                                                for value in ['Profesional', 'Empleado', 'Independiente (no profesional)',
                                                'Tecnico', 'Estudiante', 'Dueña de casa']
                                            ],
                                            value="Sin Información",
                                        ),
                                        #Cargo
                                        html.P(
                                            "Cargo",
                                            style={
                                                "textAlign": "left",
                                                "marginBottom": "2",
                                                "marginTop": "4",
                                            },
                                        ),
                                        dcc.Input(
                                            id="new_case_cargo",
                                            placeholder="cargo",
                                            type="text",
                                            value="cargo",
                                            style={"width": "100%"},
                                        ),
                                        #Situación Laboral
                                        html.P(
                                            "Situación Laboral",
                                            style={
                                                "textAlign": "left",
                                                "marginBottom": "2",
                                                "marginTop": "4",
                                            },
                                        ),
                                        dcc.Dropdown(
                                            id="new_case_situacionlaboral",
                                            options=[
                                                {   
                                                    "label": value, 
                                                    "value": value
                                                }
                                                for value in ['Dependiente', 'Independiente', 'Sin Información']
                                            ],
                                            value="Sin Información",
                                        ),
                                        #Empleador
                                        html.P(
                                            "Empleador",
                                            style={
                                                "textAlign": "left",
                                                "marginBottom": "2",
                                                "marginTop": "4",
                                            },
                                        ),
                                        dcc.Input(
                                            id="new_case_empleador",
                                            placeholder="empleador",
                                            type="text",
                                            value="empleador",
                                            style={"width": "100%"},
                                        ),
                                        #Antiguedad Laboral
                                        html.P(
                                            "Antiguedad Laboral",
                                            style={
                                                "textAlign": "left",
                                                "marginBottom": "2",
                                                "marginTop": "4",
                                            },
                                        ),
                                        dcc.Input(
                                            id="new_case_antiguedadlaboral",
                                            placeholder="4",
                                            type="number",
                                            value="4",
                                            style={"width": "100%"},
                                        ),
                                        #Presencial
                                        html.P(
                                            "Presencial",
                                            style={
                                                "textAlign": "left",
                                                "marginBottom": "2",
                                                "marginTop": "4",
                                            },
                                        ),
                                        dcc.Dropdown(
                                            id="new_case_presencial",
                                            options=[
                                                {
                                                    "label": 'Si',
                                                    "value": True,
                                                },
                                                {
                                                    "label": 'No',
                                                    "value": False,
                                                },
                                                
                                            ],
                                            value="Si",
                                        ),
                                        #Presencial
                                        html.P(
                                            "Remoto",
                                            style={
                                                "textAlign": "left",
                                                "marginBottom": "2",
                                                "marginTop": "4",
                                            },
                                        ),
                                        dcc.Dropdown(
                                            id="new_case_remoto",
                                            options=[
                                                {
                                                    "label": 'Si',
                                                    "value": True,
                                                },
                                                {
                                                    "label": 'No',
                                                    "value": False,
                                                },
                                                
                                            ],
                                            value="No",
                                        ),
                                        #Presencial
                                        html.P(
                                            "*Medio Inicial",
                                            style={
                                                "textAlign": "left",
                                                "marginBottom": "2",
                                                "marginTop": "4",
                                            },
                                        ),
                                        dcc.Dropdown(
                                            id="new_case_medioinicial",
                                            options=[
                                                {
                                                    "label": value,
                                                    "value": value,
                                                }
                                                for value in ['FINCO', 'INTERNET', 'RECONTACTO', 'RECORRIDO POR EL SECTOR',
                                                   'LETREROS', 'REFERIDOS', 'TV', 'EVENTOS', 'RADIO', 'PRENSA',
                                                   'REVISTAS', 'VOLANTES']
                                                
                                            ],
                                            value="FINCO",
                                        ),
                                       
                                    ],
                                    className="four columns",
                                    style={"paddingLeft": "15"},
                                ),
                            ],
                            style={"marginTop": "10", "textAlign": "center"},
                            className="row",
                        ),

                        # submit button
                        html.Span(
                            "Agregar",
                            id="submit_new_case",
                            n_clicks=0,
                            className="button button--primary add"
                        ),

                    ],
                    className="modal-content",
                    style={"textAlign": "center", "border": "1px solid #C8D4E3"},
                )
            ],
            className="modal",
        ),
        id="cases_modal",
        style={"display": "none"},
)