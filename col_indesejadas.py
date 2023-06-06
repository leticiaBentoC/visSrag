def generate_col_indesejadas():
    # Itens que serão excluídos do array
    itens_indesejados = [
        # DATAS
        'DATA_NOTIFICACAO', 'DATA_PRIMEIROS_SINTOMAS', 'DATA_NASCIMENTO', 'DATA_INTERNACAO', 'DATA_COLETA', 'DATA_RESULTADO_PCR', 'DATA_ALTA_OBITO', 
	    'DATA_ENCERRAMENTO', 'DATA_DIGITACAO', 'SEMANA_NOTIFICACAO', 'SEMANA_PRIMEIROS_SINTOMAS',
        # PACIENTE
        'SEXO', 'IDADE', 'IDADE_GESTACIONAL', 'RACA', 'ESCOLARIDADE', 'ESTRANGEIRO', 'VACINA_COVID', 'INFO_VACINA_COVID' 'TIPO_IDADE','COD_IDADE',
        # REGIÃO
	    'UF', 'ID_REGIONAL', 'CODIGO_REGIONAL', 'ID_MUNICIPIO', 'CODIGO_MUNICIPIO', 'ID_UNIDADE_SAUDE', 'CODIGO_UNIDADE_SAUDE', 'ID_PAIS', 'CODIGO_PAIS', 
	    'SIGLA_UF', 'ID_RESIDENCIA_PACIENTE', 'CODIGO_RESIDENCIA_PACIENTE', 'ID_MUNICIPIO_RESIDENCIA', 'CODIGO_MUNICIPIO_RESIDENCIA', 'ZONA', 
	    'UF_INTERNACAO', 'ID_REGIONAL_INTERNACAO', 'CODIGO_REGIONAL_INTERNACAO', 'ID_MUNICIPIO_INTERNACAO', 'CODIGO_MUNICIPIO_INTERNACAO',
        # INTERNAÇÃO
        'HOUVE_INTERNACAO', 'UTI', 'SUPORTE_VENTILATORIO', 'CASO_FINAL', 'CRITERIO_ENCERRAMENTO', 
        # SINTOMAS
        'FATOR_RISC',
        # EXAMES
        'RESULTADO_RAIOX', 'COLETOU_AMOSTRA', 'TIPO_AMOSTRA', 'RESULTADO_PCR', 'RESULTADO_TOMOGRAFIA', 'RESULTADO_ANTIGENICO'
    ]
    return itens_indesejados