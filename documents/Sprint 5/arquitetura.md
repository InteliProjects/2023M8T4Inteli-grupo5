# Arquitetura AWS Cloud com Metabase e Redshift

## Descrição
A arquitetura apresentada na imagem descreve um sistema que utiliza serviços da AWS Cloud para processar, armazenar e visualizar dados.

## Componentes

### Lado Esquerdo: Coleta de Dados
- **CSV/API Cliente & Base de Dados**: Os dados são coletados de clientes CSV/API e uma base de dados.
- **Python Script**: Scripts Python são usados para processar os dados coletados.
- **TLS**: O protocolo TLS é usado para garantir a segurança na transmissão dos dados.
- **AWS IAM**: Identidade e gerenciamento de acesso para controlar o acesso aos recursos da AWS.

### Centro: Armazenamento e Processamento
- **Bucket Amazon S3**: Um bucket S3 é usado para armazenar os dados processados.
- **AWS Lambda**: Uma função Lambda é acionada para processar os dados no bucket S3.

### Lado Direito: Visualização dos Dados
- **Redshift**: Utilizado como um data warehouse para armazenar os dados que serão analisados.
- **Metabase** (dentro do VPC): Uma ferramenta de visualização de dados que se conecta ao Redshift para criar dashboards e relatórios.

### Inferior: Monitoramento
- **CloudWatch**: Usado para monitorar as métricas e logs do sistema.

## Fluxo dos Dados
1. Os scripts Python coletam os dados do cliente CSV/API e da base de dados, usando TLS como protocolo seguro, sendo gerenciado pelo AWS IAM.
2. Os scripts enviam os dados processados ao bucket Amazon S3.
3. Uma função AWS Lambda é acionada, possivelmente realizando mais transformações ou carregando os dados no Redshift.
4. O Metabase dentro do VPC acessa o Redshift via TLS, permitindo a criação visualizações interativas dos dados.
5. O CloudWatch monitora todo o sistema garantindo performance, disponibilidade, e segurança.

