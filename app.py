# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, dcc, html
import dash_bootstrap_components as dbc
import pandas as pd
import locale
locale.setlocale(locale.LC_ALL, '') #pega o local da máquina e seta o locale

import data
import header as h
import body

app = Dash(__name__, external_stylesheets=[dbc.themes.FLATLY, 'styles.css'], title='Visualização de Dados SRAG')

# Faz a leitura dos datasets dos anos de 2020, 2021, 2022 e 2023
# df_0 = pd.read_csv('C:\PROJETOS\TCC\dados\srag_2019.csv', sep = ";", encoding='ISO-8859-1', on_bad_lines='skip', 
#         nrows = 790000, low_memory=False, dayfirst=True,
#         parse_dates=['DT_NOTIFIC', 'DT_SIN_PRI', 'DT_NASC', 'DT_INTERNA', 'DT_COLETA', 'DT_PCR', 'DT_EVOLUCA', 
#                      'DT_ENCERRA', 'DT_DIGITA'])
df_1 = pd.read_csv('C:\PROJETOS\TCC\dados\srag_2020.csv', sep = ";", encoding='ISO-8859-1', on_bad_lines='skip', 
        nrows = 790000, low_memory=False, dayfirst=True,
        parse_dates=['DT_NOTIFIC', 'DT_SIN_PRI', 'DT_NASC', 'DT_INTERNA', 'DT_COLETA', 'DT_PCR', 'DT_EVOLUCA', 
                     'DT_ENCERRA', 'DT_DIGITA'])
df_2 = pd.read_csv('C:\PROJETOS\TCC\dados\srag_2021.csv', sep = ";", encoding='ISO-8859-1', on_bad_lines='skip', 
        nrows = 790000, low_memory=False, dayfirst=True,
        parse_dates=['DT_NOTIFIC', 'DT_SIN_PRI', 'DT_NASC', 'DT_INTERNA', 'DT_COLETA', 'DT_PCR', 'DT_EVOLUCA', 
                     'DT_ENCERRA', 'DT_DIGITA'])
df_3 = pd.read_csv('C:\PROJETOS\TCC\dados\srag_2022.csv', sep = ";", encoding='ISO-8859-1', on_bad_lines='skip', 
        nrows = 790000, low_memory=False, dayfirst=True,
        parse_dates=['DT_NOTIFIC', 'DT_SIN_PRI', 'DT_NASC', 'DT_INTERNA', 'DT_COLETA', 'DT_PCR', 'DT_EVOLUCA', 
                     'DT_ENCERRA', 'DT_DIGITA'])
df_4 = pd.read_csv('C:\PROJETOS\TCC\dados\srag_2023.csv', sep = ";", encoding='ISO-8859-1', on_bad_lines='skip', 
        nrows = 790000, low_memory=False, dayfirst=True,
        parse_dates=['DT_NOTIFIC', 'DT_SIN_PRI', 'DT_NASC', 'DT_INTERNA', 'DT_COLETA', 'DT_PCR', 'DT_EVOLUCA', 
                     'DT_ENCERRA', 'DT_DIGITA'])

# gera o CABEÇALHO
navbar = h.generate_header()

# Junta os datasets em um único dataframe
df_merged = pd.concat([df_1, df_2, df_3, df_4])

# Trata os dados 
df_final = data.trata_dados(df_merged)

# Gera o corpo
htmlBody = body.generate_body(df_final, app)

# LAYOUT
app.layout = html.Div([
    navbar,
    htmlBody,
])

####################################################################################
# CALLBACK

####################################################################################
if __name__ == '__main__':
    app.run_server(debug=True)
