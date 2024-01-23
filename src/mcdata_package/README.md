# MCDATA_PACKAGE

MCDATA_PACKAGE é um pacote Python para facilitar o envio de arquivos para o S3, transformar arquivos CSV e RDS para Parquet, realizar limpeza simples dos dados e guardar dicionários de siglas governamentais.

## Instalação

Você pode instalar o pacote MCDATA_PACKAGE usando pip:

!pip install mcdata-package


## Uso

Aqui estão alguns exemplos de como você pode usar o pacote MCDATA_PACKAGE:

### Transformar arquivos CSV e RDS para Parquet
A seção transformar do pacote MCDATA_PACKAGE fornece funções para converter arquivos CSV e RDS para o formato Parquet. O Parquet é um formato de arquivo colunar que oferece alta performance, compactação e interoperabilidade.

from mcdata.transformar import csv_to_parquet, rds_to_parquet
<br></br>
csv_to_parquet('/path/to/csv_file.csv', '/path/to/parquet_file.parquet') 
<br></br>
rds_to_parquet('/path/to/rds_file.rds', '/path/to/parquet_file.parquet')
<br></br>
Caso exista algum tipo de separador diferente:
<br></br>
csv_to_parquet('/path/to/csv_file.csv', '/path/to/parquet_file.parquet', delimiter = ';') 


Neste exemplo, csv_to_parquet e rds_to_parquet são funções que convertem arquivos CSV e RDS, respectivamente, para o formato Parquet. /path/to/csv_file.csv e /path/to/rds_file.rds são os caminhos para os arquivos CSV e RDS que você deseja converter, respectivamente. /path/to/parquet_file.parquet é o caminho onde o arquivo Parquet convertido será salvo.

### Manipular tabelas
A seção tabela do pacote MCDATA_PACKAGE fornece uma classe para manipular tabelas pandas. A classe ManiularTabela possui um método process_table que realiza várias operações de limpeza de dados em um DataFrame pandas.

import pandas as pd 
from mcdata.tabela import ManipularTabela

<br></br>
df = pd.read_csv('/path/to/csv_file.csv') 
<br></br>
manipulator = ManipularTabela(df) 
<br></br>
processed_df = manipulator.process_table(remove_duplicates=True, null_value_replacement='Unknown', column_mapping={'OldColumnName': 'NewColumnName'}, column_value_mapping={'ColumnName': {OldValueName: 'NewValueName'}})
<br></br>
processed_df_dates_converted = convert_dates(df)
<br></br>
processed_df_dates_converted_encoded = encode_columns(df)

Neste exemplo, df é um DataFrame pandas que você deseja manipular. remove_duplicates=True remove todas as linhas duplicadas do DataFrame, null_value_replacement='Unknown' substitui todos os valores nulos por 'Unknown', column_mapping={'OldColumnName': 'NewColumnName'} renomeia a coluna 'OldColumnName' para 'NewColumnName', e column_value_mapping={'ColumnName': {OldValueName: 'NewValueName'}} substitui todos os 'OldValueName' na coluna 'ColumnName' por 'NewValueName'.

Por favor, note que remove_duplicates, null_value_replacement, column_mapping e column_value_mapping são parâmetros opcionais. Se você não fornecer um desses parâmetros, o método process_table não realizará a operação correspondente.

A função convert_dates percorre todas as colunas do DataFrame e verifica se o tipo de dados da coluna é 'object' ou 'datetime64[ns]'. Se for "verdade", a função tenta converter a coluna para o formato de data e hora usando a função pd.to_datetime do pandas. Se ocorrer um erro durante a conversão (por exemplo, se a coluna contiver um valor que não possa ser convertido em uma data), a função simplesmente passa e não faz nada com esse valor. A função então retorna o DataFrame modificado

Já a função encode_columns é usada para codificar todos os valores de texto em um DataFrame para UTF-8. Isso é feito usando a função applymap do pandas, que aplica uma função a cada elemento do DataFrame. A função encode('utf-8') é usada para codificar cada valor de texto em UTF-8. Em seguida, a função replace é usada para substituir todos os caracteres não alfanuméricos (ou seja, caracteres que não são letras ou números) por uma string vazia. A função então retorna o DataFrame modificado.

### Obter dicionários de siglas governamentais
A seção dicionários do pacote MCDATA_PACKAGE fornece funções para retornar siglas de DataFrame gorvenamentais.

from mcdata.dicionarios import uf
<br></br>
state_mapping = uf()

### Enviar arquivos para o S3
from mcdata.s3 import S3Uploader
<br></br>
uploader = S3Uploader('YOUR_ACCESS_KEY', 'YOUR_SECRET_KEY', 'YOUR_BUCKET_NAME')
<br></br>
uploader.upload_file('/path/to/file')

Neste exemplo, YOUR_ACCESS_KEY e YOUR_SECRET_KEY são suas credenciais da AWS e YOUR_BUCKET_NAME é o nome do seu bucket. /path/to/file é o caminho para o arquivo que você deseja enviar para o S3.

Por favor, note que você deve substituir 'YOUR_ACCESS_KEY', 'YOUR_SECRET_KEY', 'YOUR_BUCKET_NAME' e '/path/to/file' pelas suas credenciais da AWS, o nome do seu bucket e o caminho para o arquivo, respectivamente.

Além disso, se você estiver usando uma sessão temporária, você pode adicionar um aws_session_token ao instanciar a classe S3Uploader:
uploader = S3Uploader('YOUR_ACCESS_KEY', 'YOUR_SECRET_KEY', 'YOUR_SESSION_TOKEN', 'YOUR_BUCKET_NAME')

## Licença

Este projeto é licenciado sob a Licença MIT - por favor, veja [LICENSE](LICENSE) para mais detalhes.

