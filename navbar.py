import dash_bootstrap_components as dbc 
from dash import dcc

def Navbar():
    navbar = dbc.Nav(children=[
               dbc.NavItem(dcc.Link('CAMARA EXTERIOR', href='/camaraext',
               style={'color':'white', 'font-size': '16px'}
               )),
               dbc.NavItem(dcc.Link('CAMARA', href='/camara',
               style={'color':'white', 'font-size': '16px'}
               )),
               dbc.NavItem(dcc.Link('SENADO', href='/senado',
               style={'color':'white', 'font-size': '16px'}
               )),
    ],
    pills=True,
    #card=True,
    #justified=False,
    fill=True,
    #sticky='top',
    #fixed='top',
    horizontal=True,
    )
    return navbar