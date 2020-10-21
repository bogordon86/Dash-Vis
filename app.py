import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd

external_stylesheets = ['\~Users\gordo\Desktop\Data_Analysis\Dash_Vis\assets\bootstrap.min.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([

dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Page 1", href="#")),
        dbc.DropdownMenu(
            children=[
                dbc.DropdownMenuItem("More pages", header=True),
                dbc.DropdownMenuItem("Page 2", href="#"),
                dbc.DropdownMenuItem("Page 3", href="#"),
            ],
            nav=True,
            in_navbar=True,
            label="More",
        ),
    ],
    brand="Analytics",
    brand_href="#",
    color="primary",
    dark=True,
)
])
html.Div(
    children=html.Div([
        html.H5('Analytics'),
        html.Div('''
            Building a dash app with custom css 
        ''')
    ])
)
if __name__ == '__main__':
    app.run_server(debug=True)