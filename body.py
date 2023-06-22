from dash import html
import dash_bootstrap_components as dbc

import data_tratamento_sintomas as dts
import evolution
import line
import geo
import bar
import heatmap
import outlier_significance
import cultural_graph
import media

def generate_body(df, app):

    # Lista de anos
    anos = [2019, 2020, 2021, 2022, 2023]
    df_sintomas = dts.generate_tratamento_sintomas(df)
    
    evolutionCards = evolution.generate_cards(df)
    htmlLine = line.generate_line_chart(df, app, anos)
    htmlGeo = geo.generate_geo_graph(df, app, anos)
    htmlBar = bar.generate_bar_graph(df, app, anos)
    htmlHeatmap = heatmap.generate_heatmap_grapf(df_sintomas)
    htmlOutlier = outlier_significance.generate_outlier_grapf(df_sintomas, app)
    htmlCultural = cultural_graph.generate_cultural_graph(df, app, anos)
    htmlMedia = media.generate_media_graph(df, app, anos)
    
    body = html.Div(
    [
        dbc.Container([evolutionCards], class_name="mb-5 container-fluid"),
        dbc.Container([
            htmlLine, 
            html.Hr()
        ], class_name="mb-5 container-fluid"),
        dbc.Container([
            htmlGeo, 
            html.Hr()
        ], class_name="mb-5 container-fluid"),
        dbc.Container([
            htmlBar, 
            html.Hr()
        ], class_name="mb-5 container-fluid"),
        dbc.Container([
            htmlOutlier,
            html.Hr(),
            htmlHeatmap, 
            html.Hr()
        ], class_name="mb-5 container-fluid"),
        dbc.Container([
            htmlCultural,
            html.Hr()
        ], class_name="mb-5 container-fluid"),
        dbc.Container([
            htmlMedia, 
            html.Hr()
        ], class_name="mb-5 container-fluid"),
        html.Hr(),
    ],
)
    return body