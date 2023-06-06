from dash import dcc, html
import dash_bootstrap_components as dbc
import plotly.graph_objects as go

from phik.binning import bin_data

def generate_heatmap_grapf(df_sintomas):
    
    # Remova a coluna "EVOLUCAO_CASO"
    df_sintomas = df_sintomas.drop('EVOLUCAO_CASO', axis=1)

    data_types = {'NOSOCOMIAL': 'interval',
             'AVE_SUINO':'interval',
             'FEBRE':'ordinal',
             'TOSSE':'interval',
             'GARGANTA':'categorical',
             'DISPNEIA':'categorical',
             'DESCONFORTO_RESPIRATORIO':'categorical',
             'SATURACAO':'categorical'}

    interval_cols = [col for col, v in data_types.items() if v=='categorical' and col in df_sintomas.columns]

    # bin the interval variables
    data_binned, binning_dict = bin_data(df_sintomas, cols=interval_cols, retbins=True)
    data_binned

    phik_overview = df_sintomas.phik_matrix(interval_cols=interval_cols)

    # PLOTLY
    fig = go.Figure(data=go.Heatmap(
        z=phik_overview.values,
        x=phik_overview.columns,
        y=phik_overview.index,
        colorscale='Blues',
        zmin=0,
        zmax=1
    ))

    fig.update_layout(
        title="Correlação φK",
        xaxis=dict(title="Sintomas"),
        yaxis=dict(title="Sintomas"),
        autosize=False,
        width=900,
        height=850,
        font=dict(size=14)
    )

    heatmap_html = dbc.Col(children=[
        html.H4(children='Heatmap - Sintomas', style={'textAlign': 'center'}),
        html.Div([
            dcc.Graph(
                id='heatmap-graph',
                figure=fig,
            )
        ])
    ])
    return heatmap_html
    