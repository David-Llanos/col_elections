import dash_bootstrap_components as dbc 
from dash import dcc

# navbar_style= {
# 'postion':'fixed',
# 'top':0,
# 'left':0,
# 'right':0,
# 'margin-left':'1rem',
# 'margin-right':'1rem',
# 'font-size': '24px',
# 'background-color':'gray',
# 'color':'white'
# }


def Navbar():
    navbar = dbc.Nav(children=[
               dbc.NavItem(dcc.Link('CAMARA EXTERIOR', href='/camaraext',
               style={'color':'darkblue', 'font-size': '16px'}
               )),
               dbc.NavItem(dcc.Link('CAMARA', href='/camara',
               style={'color':'darkblue', 'font-size': '16px'}
               )),
               dbc.NavItem(dcc.Link('SENADO', href='/senado',
               style={'color':'darkblue', 'font-size': '16px'}
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