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

caxp=pd.read_csv('agregados/cax_eleccion_partido_pais.cvs')
caxp=caxp.sort_values(by=['anio','partido'])

caxpp=pd.read_csv('agregados/cax_eleccion_partido_pais_puesto.cvs')
caxpp=caxpp.sort_values(by=['anio','partido','puesto'])


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
def mostrar_data_camara_exterior(ele,par, anio):

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


@app.callback(
    Output('grafica_votos_camara_ext_pais', 'figure'),
    Input('camext_eleccion', 'value'),
    Input('camext_partido', 'value'),
    Input('camext_anio', 'value'),
    Input('grafica_votos_camara_ext', 'clickData')
   )
def mostrar_grafica_con_click(ele,par, anio, click):

    if click is None:
        raise PreventUpdate
    else:
        x=click['points'][0]['x']
        y=click['points'][0]['y']
        caxp2=caxp.loc[(caxp.eleccion.isin (ele)) & (caxp.partido.isin (par)) & 
                    (caxp.anio == int(x))]
        
        fig = px.bar(caxp2, x='pais', y='votos', color='partido', 
                    title=f"Anio seleccionado: {x}"

                )
        fig.update_layout(legend=dict(
        yanchor="top",
        y=1.4,
        xanchor="left",
        x=0.5
    ))
    
    return fig

@app.callback(
    Output('grafica_votos_camara_ext_pais_puesto', 'figure'),
    Input('camext_eleccion', 'value'),
    Input('camext_partido', 'value'),
    Input('camext_anio', 'value'),
    Input('grafica_votos_camara_ext', 'clickData'),
    Input('grafica_votos_camara_ext_pais', 'clickData'),

   )
def mostrar_grafica_con_segundo_click(ele,par, anio, click1, click2):

    if click1 is None or click2 is None :
        raise PreventUpdate
    else:
        click_anio=click1['points'][0]['x']
        click_pais=click2['points'][0]['x']
        
        caxpp2=caxpp.loc[(caxpp.eleccion.isin (ele)) & (caxpp.partido.isin (par)) & 
                    (caxp.anio == int(click_anio))  & (caxpp.pais==click_pais) ]
        
        fig = px.bar(caxpp2, x='puesto', y='votos', color='partido', 
                    title=f"Anio: {click_anio}, Pais: {click_pais}"

                )
        fig.update_layout(legend=dict(
        yanchor="top",
        y=1.4,
        xanchor="left",
        x=0.5
    ))
    
    return fig




if __name__ == '__main__':
    app.run_server(debug=True, dev_tools_hot_reload=True)



