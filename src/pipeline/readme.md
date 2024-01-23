# Pipeline de Dados: ETL, Modelo de Regressão e Gráficos de Importância de Recursos

Este projeto consiste em um pipeline de dados completo que inclui um processo de Extração, Transformação e Carga (ETL) para dados de CNPJ, POF, BACEN, DENSIDADE e ANVISA, um modelo de regressão usando o algoritmo RandomForestRegressor e a geração de um gráfico de importância de recursos.

## Pré-requisitos
Antes de executar este projeto, você precisa instalar as dependências necessárias. As dependências estão listadas no arquivo `requirements.txt`. Para instalá-las, execute o seguinte comando no terminal:
```bash
pip install -r requirements.txt
```
## Configuração
Você precisa fornecer suas credenciais da AWS e do Redshift para que o script possa carregar os dados transformados no seu bucket S3 e se conectar ao banco de dados, respectivamente. Substitua 'aws_access_key_id', 'aws_secret_access_key', 'bucket_name', 'aws_session_token', 'host', 'port', 'user', 'password' e 'database' pelos seus valores reais no código.

## Execução
Para executar o pipeline completo, você precisará executar três scripts em sequência:

1. api_etl.py - Este script executa o ETL para dados de vendas. Ele busca dados de uma API, transforma os dados e, em seguida, os carrega em um bucket AWS S3.

2. base_etl.py - Este script processa arquivos CNPJ, POF, BACEN, DENSIDADE(IBGE) e ANVISA. Portanto, você precisará modificar o caminho do arquivo no código para cada arquivo que deseja processar e executar o script novamente.

3. modelo.py - Este script executa um modelo ensemble usando o algoritmo RandomForestRegressor. Ele se conecta a um banco de dados Redshift, executa uma consulta SQL, transforma o resultado em um DataFrame pandas e, em seguida, treina o modelo de regressão. Além disso, ele gera um gráfico de importância de recursos que é salvo localmente.

Para executar cada script, navegue até o diretório que contém o script e execute o seguinte comando:
```bash
python <nome_do_script>.py
```
Substitua <nome_do_script> pelo nome do script que você deseja executar (api_etl, base_etl ou modelo).

## Gráfico de Importância de Recursos
O script modelo.py gera um gráfico de importância de recursos que mostra a importância de cada recurso no modelo de regressão. Este gráfico é salvo localmente como um arquivo PNG. Você pode encontrar este arquivo no mesmo diretório do script. Por favor, note que cada vez que você executa o script, o gráfico de importância de recursos é atualizado.

