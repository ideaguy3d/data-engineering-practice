from dash import Dash, dcc, html
from dash.dependencies import Input, Output
import plotly

app = Dash(__name__)
app.layout = html.Div([
    html.H1('Hello Dash'),
    html.Div(id='output-div'),
    dcc.Dropdown(),
    dcc.Graph(id='output-graph')
])

app.run(debug=True, port=8000)
