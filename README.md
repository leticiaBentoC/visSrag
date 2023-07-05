# visSrag

Essa é uma ferramenta de Dashboard, desenvolvida em Python para o Trabalho de Conclusão de Curso, sobre o tema Visualização de Dados aplicada a saúde em casos de Síndrome Respiratória Aguda Grave.
Para testar esse projeto, siga o passo a passo:
1. Criar um fork do repositório: https://github.com/leticiaBentoC/visSrag; 
2. Clonar o seu repositório criado a partir do fork, ou baixar a versão .zip (descompactar no local desejado); 
3. Baixar os datasets (arquivos .csv) dos anos de 2019 a 2023 no portal OpenDATASUS: https://opendatasus.saude.gov.br/organization/47e37a4a-4c0c-4d98-8a76-351826101359?tags=SRAG 
4. Colocar os arquivos dos datasets, dentro do diretório .dados/: 
5. Renomear os arquivos da seguinte forma: srag_2019.csv com os respectivos anos; 
6. Instalar a última versão do Python, compatível com seu Sistema Operacional: https://www.python.org/downloads/; 
7. Abrir o terminal no diretório do projeto e executar o comando: pip install -r requirements.txt, esse comando irá instalar todas as bibliotecas necessárias para que o projeto funcione corretamente; 
8. Abrir o projeto no IDE de sua escolha (indicação VSCode); 
9. Abrir o arquivo app.py e executá-lo pela IDE, caso ocorra algum erro no path dados, ajustar o caminho conforme necessidade (pode variar conforma o sistema operacional); 
10. Quando o terminal apresentar Debug mode: on, significa que a aplicação já está rodando na sua máquina, e para acessá-la, basta pressionar a tecla Ctrl e clicar no link disponível no terminal; 
11. Ele irá abrir o Dashboard no browser padrão, depois de alguns minutos.


Para futuras implementações, basta criar um novo arquivo .py e desenvolver o código para o gráfico desejado e chamá-lo através do arquivo body.py. 
1. Importar o arquivo criado; 
2. Fazer uso em uma variável, passando os parâmetros necessários; 
3. Adicionar a variável no html. 
