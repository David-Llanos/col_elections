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

cax=pd.read_csv('agregados/cax_eleccion_partido.cvs')
cax=cax.sort_values(by=['anio'])





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
    Input('camext_eleccion', 'value'),
    Input('camext_partido', 'value'),
    Input('camext_anio', 'value')
   )
def mostrar_tabla_camara_2018(ele,par, anio):

    cax2=cax.loc[(cax.eleccion.isin (ele)) & (cax.partido.isin (par)) & (cax.anio.isin (anio))]
    
    fig = px.line(cax2, x='anio', y='votos', color='partido', markers=True,
              title="Total votos globales por anio, circunscripcion y partido"
              )
    fig.update_layout(legend=dict(
    yanchor="top",
    y=1.4,
    xanchor="left",
    x=0.5
))

    camara_ext_table=dt.DataTable(
                            columns=[{"name": i, "id": i} for i in cax2.columns],
                            data=cax2.to_dict('records'),
                            sort_action='native',
                            filter_action='native',
                            style_table={'overflowX': 'auto'},
                            page_size=10
                            )
    return [camara_ext_table, fig]


if __name__ == '__main__':
    app.run_server(debug=True, dev_tools_hot_reload=True)



