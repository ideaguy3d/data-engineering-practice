from dash import Dash, dcc, html
from dash.dependencies import Input, Output
import plotly

app = Dash(__name__)

app.layout = html.Div([
    html.H1('Hello Dash'),
    html.Div(id='output-div'),
    dcc.Dropdown(
        options=['Red', 'Blue', 'Green'],
        id='input-dropdown',
        value='Red'
    ),
    dcc.Graph(id='output-graph')
])

# @app.callback(Output(), Input())
# def interactive_chart(input):
#     return output


if __name__ == '__main__':
    app.run_server(port=8080, host='localhost', debug=True)

# eof
