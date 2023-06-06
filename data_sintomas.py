import pandas as pd

import col_sintomas as cs

def trata_dados_sintomas(df):

    # define o limite de valores ausentes
    limite_ausentes = len(df) * 0.5

    # remove as colunas que contém mais de 50% de valores ausentes
    df = df.dropna(thresh=limite_ausentes, axis=1)

    # renomeia as colunas
    df = df.rename(columns={
        'DT_NOTIFIC': 'DATA_NOTIFICACAO', 'SEM_NOT': 'SEMANA_NOTIFICACAO', 'DT_SIN_PRI': 'DATA_PRIMEIROS_SINTOMAS',
        'SEM_PRI': 'SEMANA_PRIMEIROS_SINTOMAS', 'SG_UF_NOT': 'UF','ID_REGIONA': 'ID_REGIONAL', 'CO_REGIONA': 'CODIGO_REGIONAL',
        'ID_MUNICIP': 'ID_MUNICIPIO', 'CO_MUN_NOT': 'CODIGO_MUNICIPIO', 'ID_UNIDADE': 'ID_UNIDADE_SAUDE', 
        'CO_UNI_NOT': 'CODIGO_UNIDADE_SAUDE', 'CS_SEXO': 'SEXO', 'DT_NASC': 'DATA_NASCIMENTO', 'NU_IDADE_N': 'IDADE',
        'TP_IDADE': 'TIPO_IDADE', 'CS_GESTANT': 'IDADE_GESTACIONAL', 'CS_RACA': 'RACA', 'CS_ESCOL_N': 'ESCOLARIDADE',
        'CO_PAIS': 'CODIGO_PAIS', 'SG_UF': 'SIGLA_UF', 'ID_RG_RESI': 'ID_RESIDENCIA_PACIENTE', 
        'CO_RG_RESI': 'CODIGO_RESIDENCIA_PACIENTE', 'ID_MN_RESI': 'ID_MUNICIPIO_RESIDENCIA', 'CO_MUN_RES': 'CODIGO_MUNICIPIO_RESIDENCIA',
        'CS_ZONA': 'ZONA', 'DESC_RESP': 'DESCONFORTO_RESPIRATORIO', 'OUTRO_SIN': 'OUTROS_SINTOMAS', 'HOSPITAL': 'HOUVE_INTERNACAO',
        'DT_INTERNA': 'DATA_INTERNACAO', 'SG_UF_INTE': 'UF_INTERNACAO', 'ID_RG_INTE': 'ID_REGIONAL_INTERNACAO', 
        'CO_RG_INTE': 'CODIGO_REGIONAL_INTERNACAO', 'ID_MN_INTE': 'ID_MUNICIPIO_INTERNACAO', 'CO_MU_INTE': 'CODIGO_MUNICIPIO_INTERNACAO',
        'SUPORT_VEN': 'SUPORTE_VENTILATORIO', 'RAIOX_RES': 'RESULTADO_RAIOX', 'AMOSTRA': 'COLETOU_AMOSTRA', 'DT_COLETA': 'DATA_COLETA',
        'TP_AMOSTRA': 'TIPO_AMOSTRA', 'PCR_RESUL': 'RESULTADO_PCR', 'DT_PCR': 'DATA_RESULTADO_PCR', 'CLASSI_FIN': 'CASO_FINAL',
        'CRITERIO': 'CRITERIO_ENCERRAMENTO', 'EVOLUCAO': 'EVOLUCAO_CASO', 'DT_EVOLUCA': 'DATA_ALTA_OBITO', 'DT_ENCERRA': 'DATA_ENCERRAMENTO',
        'DT_DIGITA': 'DATA_DIGITACAO', 'DOR_ABD': 'DOR_ABDOMINAL', 'PERD_OLFT': 'PERDA_OLFATO', 'PERD_PALA': 'PERDA_PALADAR',
        'TOMO_RES': 'RESULTADO_TOMOGRAFIA', 'RES_AN': 'RESULTADO_ANTIGENICO', 'ESTRANG': 'ESTRANGEIRO', 'VACINA_COV': 'VACINA_COVID',
        'FNT_IN_COV': 'INFO_VACINA_COVID'
    })
    #colunas = df.columns.tolist()
    
   # Tratamento da data
    df['DATA_ALTA_OBITO'] = df['DATA_ALTA_OBITO'].astype(str)  # Converter para string

    # Verificar e converter para datetime
    df['DATA_ALTA_OBITO'] = pd.to_datetime(df['DATA_ALTA_OBITO'], errors='coerce')
    df['DATA_ALTA_OBITO'] = df['DATA_ALTA_OBITO'].fillna(pd.NaT)
    # Remover a coluna de data com valores nulos
    df = df.dropna(subset=['DATA_ALTA_OBITO'])

    col_sintomas = cs.generate_col_sintomas()
    
    # define os valores como inteiros
    for col in col_sintomas:
        if col in df.columns:
            if df[col].dtype == 'object':
                df[col] = df[col].fillna('').astype(str)
            else:
                df[col] = df[col].fillna(0).astype(int) 

    # guarda as colunas sem adicionar sexo, idade, datas, etc
    colunas_old = col_sintomas[:]

    # troca os valores null para 9 = ignorado
    df = df.fillna(9)

    # adiciona novas colunas par col_sintomas
    novas_colunas = ['SEXO', 'IDADE', 'DATA_PRIMEIROS_SINTOMAS','DATA_INTERNACAO', 'DATA_ALTA_OBITO']
    col_sintomas.extend(novas_colunas) 

    # seta um novo dataset somente com as colunas existentes no dataset importado
    df_sintomas = pd.DataFrame()
    for col in col_sintomas:
        if col in df.columns:
            df_sintomas[col] = df[col]
    return df_sintomas
    # return df[[
    #     'NOSOCOMIAL', 'AVE_SUINO', 'FEBRE', 'TOSSE', 'GARGANTA', 'DISPNEIA', 
    #     'DESCONFORTO_RESPIRATORIO', 'SATURACAO', 'DIARREIA', 'VOMITO', 'OUTROS_SINTOMAS', 'FATOR_RISC', 'HOUVE_INTERNACAO', 
    #     'UTI', 'SUPORTE_VENTILATORIO', 'RESULTADO_RAIOX', 'CASO_FINAL', 'CRITERIO_ENCERRAMENTO', 'EVOLUCAO_CASO', 
    #     'DOR_ABDOMINAL', 'FADIGA', 'PERDA_OLFATO', 'PERDA_PALADAR', 'RESULTADO_TOMOGRAFIA', 'RESULTADO_ANTIGENICO', 
    #     'ESTRANGEIRO', 'VACINA_COVID', 'INFO_VACINA_COVID',  'IDADE', 'SEXO', 'DATA_PRIMEIROS_SINTOMAS',
    #     'DATA_INTERNACAO', 'DATA_ALTA_OBITO']]