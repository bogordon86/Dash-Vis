from app import app
from app import server
from plotly.subplots import make_subplots
import dash_html_components as html
import dash_core_components as dcc

app.layout = html.Div([html.H1('Covid-19 Daily Summary',
                               style={
                                      'textAlign': 'center',
                                      "background": "blue"}),
                       dcc.Graph(
                           id='graph-1',
                           figure={
                               'data': [
                                   {'x': [10/7/2020, 10/8/2020, 10/9/2020, 10/10/2020, 10/11/2020, 10/12/2020, 10/13/2020], 'y': [509, 1844, 1114, 1256, 811, 854, 1235], 'type': 'line', 'name': 'increase'},
                                   {'x': [10/7/2020, 10/8/2020, 10/9/2020, 10/10/2020, 10/11/2020, 10/12/2020, 10/13/2020], 'y': [153691, 155535, 156649, 157905, 158716, 159570, 160805], 'type': 'line', 'name': 'total'}
                               ],
                               'layout': {
                                   'title': 'Virginia Daily Cases',
                                     }
                                 }
                            ),

                            ], style={
                                "background": "#000080"}
                         )

if __name__ == '__main__':
    app.run_server(debug=True)