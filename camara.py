import  dash
from dash import html
from dash import dcc
import dash_bootstrap_components as dbc 
from navbar import Navbar


nav = Navbar()

body = dbc.Container([ 

    dbc.Row([
        html.H1(r'camara')
        
    ])

])

def CAMARA():
    layout = html.Div([
        nav,
        body
    ])
    return layout

app = dash.Dash(__name__)

app.layout=CAMARA()
if __name__ == '__main__':
    app.run_server()