import  dash
from dash import html
from dash import dcc
import dash_bootstrap_components as dbc 
from navbar import Navbar
import pandas as pd
ca=pd.read_stata('data/2018_Camara.dta')

nav = Navbar()

body = dbc.Container([ 

    dbc.Row([
        dbc.Col([
        html.H1("Camara en el Exterior"),
        ],md=12),


        dbc.Col([
        html.H1(r"Circunscripcion"),
        html.Br(),
        dcc.Dropdown(id='camext_circunscripcion',
            options=[{'label': i, 'value': i} for i in ca.circunscripcion.unique()],
            value=ca.circunscripcion.unique()[0],
            multi=False
        ),
        ],md=6),

        dbc.Col([
        html.H1(r"Seleccione Anio"),
        html.Br(),
        dcc.Dropdown(id='camext_anio',
            options=[{'label': i, 'value': i} for i in ca.ano.unique()],
            value=ca.ano.unique()[0],
            multi=False
        ),
        ],md=6),

        dbc.Col([
        html.Br(),
        html.Br(),
        dcc.Graph('grafica_votos_camara_ext'),
        html.Br(),
        html.Div(id='tabla_camara_ext'),
        ],md=12)
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