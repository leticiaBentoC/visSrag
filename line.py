from dash import dcc, html, Input, Output
import plotly.graph_objects as go
import pandas as pd

def generate_line_chart(df, app):    
    df['DATA_ALTA_OBITO'] = pd.to_datetime(df['DATA_ALTA_OBITO'], format='%d/%m/%Y')

    # Filtrar os registros onde "obito" é igual a 1 e agrupar por mês da coluna "data"
    cura = df[df['EVOLUCAO_CASO'] == 1].groupby(pd.Grouper(key='DATA_ALTA_OBITO', freq='M')).size()
    obito = df[df['EVOLUCAO_CASO'] == 2].groupby(pd.Grouper(key='DATA_ALTA_OBITO', freq='M')).size()
    obito_outros = df[df['EVOLUCAO_CASO'] == 3].groupby(pd.Grouper(key='DATA_ALTA_OBITO', freq='M')).size()
    
    # Reindexar as arrays para garantir o mesmo índice
    cura = cura.reindex(obito.index)
    obito_outros = obito_outros.reindex(obito.index)

    df_casos = pd.DataFrame({'mes': obito.index, 'cura': cura.values, 'obito': obito.values, 'obito_outros': obito_outros.values})

    year_list = [2020, 2021, 2022, 2023]
    line = html.Div([
        html.H4(children='Evolução dos Casos', style={'textAlign': 'center'}),
        html.Div("Escolha o ano:"),
        dcc.Dropdown(
            id="years-dropdown",
            value=year_list[:2],
            options=year_list,
            multi=True,
        ),
        dcc.Graph(id="line-chart")
    ])

    @app.callback(
        Output("line-chart", "figure"),
        Input("years-dropdown", "value"),
    )
    def update_graph(years, df_casos=df_casos):

        df_casos['mes'] = pd.to_datetime(df_casos['mes'])
        filtered_df = df_casos[df_casos['mes'].dt.year.isin(years)]

        fig = go.Figure()
        fig.add_trace(go.Scatter(x=filtered_df['mes'], y=filtered_df['cura'], mode='lines+markers', name='Cura'))
        fig.add_trace(go.Scatter(x=filtered_df['mes'], y=filtered_df['obito'], mode='lines+markers', name='Óbito por SRAG'))
        fig.add_trace(go.Scatter(x=filtered_df['mes'], y=filtered_df['obito_outros'], mode='lines+markers', name='Óbito por outras causas'))

        return fig
    
    return line

