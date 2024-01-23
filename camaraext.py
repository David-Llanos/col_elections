import  dash
from dash import html
from dash import dcc
import dash_bootstrap_components as dbc 
from navbar import Navbar
import pandas as pd
from listas import partidos, paises
elecciones=['CmaraIndgena', 'CmaraNegritudes', 'CmaraTerritorial']
anios=[2010,2014,2018,2022]

nav = Navbar()

body = dbc.Container([ 
    html.Br(),
    html.H2("Camara en el Exterior", style={'text-align':'center'}),
    html.Br(),
    dbc.Row([
        dbc.Col([
        html.H3(r"Anio"),
        html.Br(),
        dcc.Dropdown(id='camext_anio',
            options=[{'label': i, 'value': i} for i in anios],
            value=anios,
            multi=True
        ),
        ],width=2),


        dbc.Col([
        html.H3(r"Eleccion"),
        html.Br(),
        dcc.Dropdown(id='camext_eleccion',
            options=[{'label': i, 'value': i} for i in elecciones],
            value=elecciones[0:3],
            multi=True
        ),
        ],width=2),

        dbc.Col([
        html.H3(r"Partido"),
        html.Br(),
        dcc.Dropdown(id='camext_partido',
            options=[{'label': i, 'value': i} for i in partidos],
            value=partidos[0:3],
            multi=True,
            searchable=True,
            clearable=False,
            persistence=True,
            persistence_type='local',
            style={'width':'100%'},
            )
        
        ],width=8),

        # dbc.Col([
        # html.H3(r"Pais"),
        # html.Br(),
        # dcc.Dropdown(id='camext_pais',
        #     options=[{'label': i, 'value': i} for i in paises],
        #     value=paises,
        #     multi=True,
        #     searchable=True,
        #     clearable=False,
        #     persistence=True,
        #     persistence_type='local',
        #     style={'width':'100%'},
        #     )
        
        # ],width=6),

        dbc.Col([
            html.Br(),
            html.Br(),
            dcc.Graph('grafica_votos_camara_ext'),
            html.Br(),
            dcc.Graph('grafica_votos_camara_ext_pais'),
            html.Br(),
            dcc.Graph('grafica_votos_camara_ext_pais_puesto'),
            html.Br(),
            html.Div(id='tabla_camara_ext'),
        ],width=12)
    ])

])

def CAMARAEXT():
    layout = html.Div([
        nav,
        body
    ])
    return layout

app = dash.Dash(__name__)

app.layout=CAMARAEXT()
if __name__ == '__main__':
    app.run_server()