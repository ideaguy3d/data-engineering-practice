# %% [markdown]
# # imports

# %%
from dash import Dash, dcc, html, dash_table
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
from dash.exceptions import PreventUpdate
from dash_bootstrap_templates import load_figure_template
import plotly.express as px
import pandas
import numpy as np
import random
from numpy.random import default_rng
import datetime

# %% [markdown]
# # dash app

# %%

df_edu = pandas.read_csv('data/states_all.csv').iloc[:, 1:]
print(df_edu.head())

app = Dash(__name__, external_stylesheets=[dbc.themes.SLATE])

df_edu_chain = (
    df_edu
    .assign(
        Avg_Math=lambda df: df[['AVG_MATH_4_SCORE', 'AVG_MATH_8_SCORE']].mean(axis=1),
        Avg_Reading=lambda df: df[['AVG_READING_4_SCORE', 'AVG_READING_8_SCORE']].mean(axis=1),
    )
)

all_options = {
    "By Subject": [
        {"label": "Math", "value": "Avg_Math"},
        {"label": "Reading", "value": "Avg_Reading"}
    ],
    "By Grade and Subject": [
        {"label": "4th Grade Math", "value": "AVG_MATH_4_SCORE"},
        {"label": "8th Grade Math", "value": "AVG_MATH_8_SCORE"},
        {"label": "4th Grade Reading", "value": "AVG_READING_4_SCORE"},
        {"label": "8th Grade Reading", "value": "AVG_READING_8_SCORE"},
    ],
}

app.layout = dbc.Container([
    html.Div([
        dcc.RadioItems(
            id='report-type-radio',
            options=["By Subject", "By Grade and Subject"],
        ),
        dcc.RadioItems(id="metric-radio"),
        dcc.Graph(id="metric-bar"),
    ])
])


@app.callback(
    Output(component_id="metric-radio", component_property="options"),
    Input(component_id="report-type-radio", component_property="value")
)
def set_metrics_options(selected_report):
    return all_options[selected_report]


@app.callback(
    Output(component_id="metric-radio", component_property="value"),
    Input(component_id="metric-radio", component_property="value")
)
def plot_bar(metric):
    if metric is None:
        raise PreventUpdate

    figure = px.bar(
        (
            df_edu_chain
            .groupby("STATE", as_index=False)
            .agg({metric: "mean"})
            .sort_values(metric, ascending=False)
        ),
        x="STATE",
        y=metric,
    )
    return figure


if __name__ == '__main__':
    # host="127.0.0.1"
    app.run_server(debug=True, host="127.0.0.1", port=8052)

# eof
