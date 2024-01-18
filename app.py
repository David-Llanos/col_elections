import dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
from navbar import Navbar
from camaraext import CAMARAEXT
from camara import CAMARA
from senado import SENADO
import dash_bootstrap_components as dbc
from dash import dash_table
import pandas as pd
import numpy as np
import plotly.express as px
from dash import dash_table as dt
from datetime import datetime
import getpass
import json
import sys

import pandas as pd 
ca=pd.read_stata('data/2018_Camara.dta')
cam_cols=['ano', 'tipo_eleccion', 'fecha_eleccion',
       'departamento', 'codmpio', 'municipio', 'circunscripcion',
       'codigo_partido', 'codigo_lista', 'primer_apellido', 'segundo_apellido',
       'nombres', 'votos', 'curules']
ca2=ca[cam_cols]


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.CERULEAN])

app.config.suppress_callback_exceptions=True

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])


@app.callback(Output('page-content', 'children'),
              Input('url', 'pathname'))
def render_content(pathname):
    if  pathname == '/camara':
        return CAMARA()
    elif  pathname == '/senado':
        return SENADO()    
    # elif  pathname == '/catalogos':
    #     return presidencia()
    # elif pathname == '/ingresos':
    #     return gobernacion()
    # elif pathname == '/resultados':
    #     return alcaldia()
    else:
        return CAMARAEXT()
    

@app.callback(
    Output('tabla_camara_ext', 'children'),
    Output('grafica_votos_camara_ext', 'figure'),
    Input('camext_circunscripcion', 'value'),
    Input('camext_anio', 'value')
   )
def mostrar_tabla_camara_2018(cir, anio):


    ca3=ca2.loc[ (ca2.circunscripcion==cir) &
                 ( ca2.ano==anio) ]

    camara_ext_table=dt.DataTable(
                            columns=[{"name": i, "id": i} for i in ca3.columns],
                            data=ca3.to_dict('records'),
                            sort_action='native',
                            filter_action='native',
                            style_table={'overflowX': 'auto'},
                            page_size=10
                            )
    fig= px.bar(ca3, x='codigo_lista', y='votos')
    return [camara_ext_table, fig]


if __name__ == '__main__':
    app.run_server(debug=True, dev_tools_hot_reload=True)



