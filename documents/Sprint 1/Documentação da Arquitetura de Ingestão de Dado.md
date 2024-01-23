# Documentação da Arquitetura de Ingestão de Dados do Parceiro

Segue artefato acadêmico de documentação e explicação da arquitetura proposta pelo time M&C Solutions.

## Tipos de dados fornecidos pelo parceiro e suas características.

**Formato dos Dados de Entrada** Os dados vem de forma não estruturados, com diferentes formatos de arquivos, desde CSV até arquivos em texto.

## **Requisitos do pipeline de dados:**

- **Fontes de Dados:**
    - Dados de censos/pesquisas do governo (CSV)
    - Informações de CNPJs (CSV)
    - Dados fornecidos pelo parceiro solicitante da análise (API da Integration)
- **Volume de Dados:**
    - Há variação no volume de dados devido às contribuições do parceiro e ao crescimento contínuo ao longo dos anos nos dados governamentais e de CNPJs
    - Planejamento para suportar um volume de dados médio até 10GB
- **Velocidade de Ingestão:**
    - A Transmissão dos dados será via streaming
    - Processamento dos fluxos durante a visualização das informações do infográfico
- **Transformação e Processamento:**
    - Dados recebidos em formato não estruturado
    - Transformação em tabelas estruturadas durante o processamento (principalmente no processo de ETL)
    - Limpeza, remoção de dados indesejáveis (de início apenas os dados estrangeiros foram salientados como necessidade de remoção), reestruturação do formato dos dados
- **Armazenamento:**
    - Armazenamento dos dados a partir de Amazon S3 e do AWS Redshift
    - Há possibilidade de portabilidade para outras plataformas de nuvem, usando serviços de código aberto
- **Segurança:**
    - Utilização do Amazon TLS
    - Utilização do AWS VPC que fornece um ambiente de rede virtual seguro e isolado
- **Escalabilidade:**
    - Gerenciamento eficaz de requisições mesmo com grandes volumes de dados, graças à utilização de serviços que permitem e garantem o desempenho a partir das regras de negócio.

## Arquitetura Completa

![Arquitetetura_Grupo5 drawio](https://github.com/2023M7T4-Inteli/grupo1/assets/99264567/eb1b2c01-e4fb-4ee4-b367-ca590c5688f3)

## Descrição do Fluxo de Dados da Arquitetura

O processo começa com o API Gateway recebendo as solicitações de entrada, a partir dos dados do cliente provisionados por uma API própria. Além disso, possuímos outras duas fontes de entrada, dados de pesquisas do governo e informações de CNPJs, que são coletadas, tratadas e processadas incialmente por Scripts em Python, provisionados posteriormente em Lambda Functions para envio dos dados ao datalake.

O datalake de armazenamento utilizado é o Amazon S3, que disponibiliza e provém escalabilidade dos dados para qualquer tipo de consulta ou requisição de serviço, no qual os recursos de gerenciamento são fáceis de usar, e há uma maior organização dos dados, além da possibilidade de configurar controles de acesso para atender a requisitos específicos de negócios.

Para permitir a comunicação segura entre as Lambda Functions e o Amazon S3, temos o AWS Identity and Access Management (IAM). O AWS IAM é o serviço de gerenciamento de identidade e acesso da AWS que permite controlar quem pode acessar seus recursos da AWS e o que eles podem fazer com esses recursos.

Em seguida, o AWS Lambda que já provisionou os códigos permite sua requisição em tempo real e para disponibilidade no S3. Assim, a partir da extração destes dados, o AWS Glue desempenha um papel crucial nessa fase, organizando os dados brutos ao realizar a limpeza e as transformações necessárias (processo de ETL). Posteriormente, ele prepara esses dados para armazenamento.

Após a transformação, os dados são encaminhados para o armazenamento permanente. Eles são armazenados no Amazon Redshift. Para garantir a segurança durante a ingestão, são estabelecidas várias medidas de segurança. A aplicação da comunicação de conexões seguras (TLS) são utilizadas entre todos os componentes do processo. Além disso, políticas rigorosas de controle de acesso são configuradas no Amazon S3 para restringir quem pode acessar os dados. A criptografia é aplicada aos dados usando o AWS KMS, garantindo que permaneçam confidenciais e seguros.

Para monitorar todo o processo, são configurados alarmes no Amazon CloudWatch. Esses alarmes são essenciais para detectar problemas ou gargalos no fluxo de dados, permitindo uma resposta rápida e eficiente para manter o sistema funcionando sem interrupções. Esse fluxo de dados bem organizado e altamente seguro garante que as informações sejam processadas, transformadas, armazenadas e monitoradas de maneira eficaz e confiável.

### Descrição da funcionalidade dos serviços na arquitetura:

Segue descrição dos serviços e sua funcionalidade, contidos na arquitetura: 

1. **API Gateway**: ponto de entrada os dados vindo de API do cliente. Ele lida com as solicitações recebidas e as encaminha para os serviços apropriados.
2. **API Gateway**:  ponto de entrada os dados, que projetará as informações vindas de API do cliente. Ele lidará com as solicitações recebidas e fará o redirecionamento pro datalake (Amazon S3). Em suma, o API Gateway permite que os desenvolvedores criem, publiquem, mantenham, monitorem e protejam APIs em qualquer escala, o que auxilia na escalabilidade do projeto.
3. **Lambda Function**: Uma vez que o API Gateway recebe a solicitação, ele aciona uma função Lambda, e no outro lado de recebimento dos dados, os Scripts gerados em python também serão utilizados no Lambda. O Lambda é um serviço de computação sem servidor que executa seu código em resposta a eventos e gerencia automaticamente os recursos de computação em nuvem.
4. **Amazon S3 Bucket**: A partir disso, as funções Lambda processam as solicitações e armazena os dados em um bucket Amazon S3. O Amazon S3 é um serviço de armazenamento de objetos que oferece alta escalabilidade e é utilizada na arquitetura como datalake para armazenamento, disponibilidade de dados, com alta segurança (a partir das pesquisas realizadas) e desempenho.
5. **Amazon Glue**: Na seção de transformação dos dados, selecionamos o AWS Glue, que receberá os dados do S3. O Amazon Glue é um serviço de ETL totalmente gerenciado (permite alto controle do serviço) que facilita a preparação e o carregamento de dados para análise.
6. **Amazon Redshift Cluster**: Os dados do bucket S3 são então movidos para o AWS Glue e depois desta parte de ETL, serão movidos para um cluster do Amazon Redshift para processamento adicional. O Amazon Redshift é um serviço de armazenamento de dados em nuvem totalmente gerenciado que permite executar consultas SQL de dados, e neste caso será utilizado como nosso datawarehouse
    1. É importante citar que o Redshift roda com Spark “por baixo dos panos” e possui alta eficiência para dados de alto volume e complexidade
7. **Amazon CloudWatch**: Durante todo esse processo, o Amazon CloudWatch monitora os recursos, desde o processo no datalake até o processo de datawarehouse, e coleta e rastreia métricas, arquivos de log e responde a alterações de desempenho em todo o sistema.
8. **Amazon QuickSight**: Finalmente, os dados processados do cluster Redshift são visualizados usando o Amazon QuickSight, um serviço de inteligência empresarial (BI) escalável, sem servidor, incorporável e alimentado por machine learning construído para a nuvem.
9. **Amazon VPC**: Todos esses componentes estão contidos dentro de uma Amazon Virtual Private Cloud (VPC), que fornece um ambiente de rede virtual seguro e isolado.
10. **AWS Identity and Access Management (IAM):** pode ser definido como um serviço da Amazon Web Services (AWS) que permite controlar o acesso aos recursos da AWS de forma segura e escalável. A funcionalidade do AWS IAM é essencial para gerenciar identidades e permissões dentro do ambiente, e neste caso, permitirá o acesso granular a cada uma das aplicações na AWS de nossa arquitetura.

## Canais e Métodos de Ingestão

### API Gateway:

O API Gateway serve como o ponto de entrada do sistema, recebendo solicitações de entrada da API do cliente. Ele é especialmente adequado para lidar com dados em tempo real, onde a frequência é alta e as solicitações são recebidas de maneira contínua. Este canal é projetado para fornecer escalabilidade e segurança para gerenciar o fluxo constante de dados em tempo real.

**Frequência de Dados:** Alta, em tempo real.
**Quantidade de Dados:** Variável, dependendo da interação com os clientes.
**Vantagens:** Alta escalabilidade, segurança integrada, manipulação de dados em tempo real.

### AWS Lambda:

O AWS Lambda é um serviço altamente flexível que desempenha um papel crucial no processamento de dados estáticos e em tempo real. É especialmente valioso quando se lida com dados estáticos, como POF (Pessoa Física) e CNPJ (Cadastro Nacional de Pessoa Jurídica), que têm uma frequência menor e podem ser importados e processados em intervalos programados.

**Frequência de Dados Estáticos:** Baixa a moderada, em intervalos programados.
**Quantidade de Dados Estáticos:** Variável, dependendo do volume de dados programados.
**Frequência de Dados em Tempo Real:** Alta, contínua.
**Quantidade de Dados em Tempo Real:** Variável, dependendo da interação com os clientes.
**Vantagens:** Flexibilidade para processar dados estáticos e em tempo real, controle sobre agendamento e escalabilidade.

## Seleção dos Serviços da AWS para Cada Etapa do Processo de Ingestão

### Coleta e Ingestão Inicial:

### O API Gateway recebe as solicitações de entrada:

- O API Gateway atua como o ponto de entrada para o sistema, recebendo solicitações de entrada da API do cliente. As solicitações são encaminhadas para o próximo estágio do pipeline de dados.

### Processamento com AWS Lambda para Dados Estáticos e em Tempo Real:

- Dados Estáticos: Para dados estáticos (POF e CNPJ), o AWS Lambda pode ser configurado para realizar tarefas programadas, como a importação e processamento de arquivos em intervalos específicos. O Lambda processa esses dados de acordo com as necessidades do negócio, aplicando transformações, validações e preparando-os para armazenamento.
- Dados em Tempo Real: Para dados em tempo real (API do Cliente), o AWS Lambda é configurado para processar as solicitações conforme elas chegam. Ele aplica transformações e operações em tempo real aos dados em movimento, garantindo que eles estejam prontos para armazenamento imediato.

### Transformação e Limpeza:

### AWS Glue para Transformação e Limpeza:

- O AWS Glue desempenha um papel fundamental na etapa de transformação e limpeza dos dados. Ele pode extrair os dados do Amazon S3, aplicar transformações para padronizar, limpar e enriquecer os dados, e então armazená-los diretamente no Amazon Redshift.

### Armazenamento:

### Amazon S3 como Datalake:

- O Amazon S3 é usado como um data lake para receber os dados brutos. Ele fornece um armazenamento escalável e econômico para armazenar os dados em sua forma bruta, sem estruturação.

### Amazon Redshift como Datawarehouse:

- O Amazon Redshift é usado para armazenar os dados preparados e estruturados de forma apropriada para consulta analítica. Os dados processados pelo AWS Glue são carregados no Amazon Redshift para permitir consultas de alto desempenho e análises complexas.

### Aspectos de segurança da Arquitetura

Visando proteger os dados durante o processo de ingestão, utilizaremos recursos específicos: o TLS (Transport Layer Security) e o AWS Key Management Service (KMS), que desempenham papéis na garantia da segurança da comunicação.

O TLS desempenhará um papel no que diz respeito à criptografia. Sua função principal é criptografar os dados enquanto estão em trânsito, o que impede possíveis tentativas de interceptação e assegura a integridade dos dados em todo o percurso, desde a etapa do AWS Glue até o Redshift, por exemplo. Além da criptografia, o TLS também verifica a integridade dos dados, garantindo que nenhuma alteração ocorra durante a transferência.

Para complementar a segurança, vamos fazer uso do AWS Key Management Service (KMS). O KMS pode ser integrado aos serviços que planejamos utilizar e nos permite criar Customer Master Keys (CMKs), que são essenciais para criptografar e decifrar os dados de forma segura. Além disso, o KMS é responsável pela gestão eficiente dessas chaves (CMK). Portanto, o KMS contribui significativamente para a segurança do processo de ingestão de dados, garantindo que as chaves criptográficas utilizadas pelo TLS sejam gerenciadas e protegidas adequadamente. Juntos, o TLS e o KMS se complementam garantindo a integridade e a confidencialidade dos dados durante o trânsito.

Além disso, adotamos o AWS Identity and Access Management (IAM) para aprimorar a segurança em nossa arquitetura. Essa abordagem nos capacita a estabelecer um controle granular sobre as permissões de acesso dos usuários em suas funções específicas, garantindo um ambiente altamente seguro.

## Próximos Passos

Os próximos passos para a Sprint 2 serão a implementação do VPC, estruturação da ingestão de dados usando Lambda, Redshift (Data warehouse), S3 (Data Lake) e Glue (ETL) e configurações do API-Gate. Além disso, será realizado a prototipação da visualização dos dados.

## Referências:

*Exemplos e práticas recomendadas de arquitetura de referência*. (n.d.). Amazon Web Services, Inc. [https://aws.amazon.com/pt/architecture/?cards-all.sort-by=item.additionalFields.sortDate&cards-all.sort-order=desc&awsf.content-type=*all&awsf.methodology=*all&awsf.tech-category=*all&awsf.industries=*all&awsf.business-category=*all](https://aws.amazon.com/pt/architecture/?cards-all.sort-by=item.additionalFields.sortDate&cards-all.sort-order=desc&awsf.content-type=*all&awsf.methodology=*all&awsf.tech-category=*all&awsf.industries=*all&awsf.business-category=*all) 

*O que é pipeline de dados? - Explicação sobre pipeline de dados - AWS*. (n.d.). Amazon Web Services, Inc. [https://aws.amazon.com/pt/what-is/data-pipeline/](https://aws.amazon.com/pt/what-is/data-pipeline/) 

*Monitoramento de aplicações e infraestrutura – Amazon CloudWatch – Amazon Web Services*. (n.d.). Amazon Web Services, Inc. [https://aws.amazon.com/pt/cloudwatch/](https://aws.amazon.com/pt/cloudwatch/) 

*Amazon Redshift – Data Warehouse na nuvem – Amazon Web Services*. (n.d.). Amazon Web Services, Inc. [https://aws.amazon.com/pt/redshift/](https://aws.amazon.com/pt/redshift/) 

*Computação sem servidor - AWS Lambda - Amazon Web Services*. (n.d.). Amazon Web Services, Inc. [https://aws.amazon.com/pt/lambda/features/](https://aws.amazon.com/pt/lambda/features/) 

*What is AWS Glue? - AWS Glue*. (n.d.). [https://docs.aws.amazon.com/glue/latest/dg/what-is-glue.html](https://docs.aws.amazon.com/glue/latest/dg/what-is-glue.html) 

De Souza, I. (2021, February 12). *O que é TLS e quais são as diferenças entre ele e SSL? Descubra agora*. Rock Content - BR. [https://rockcontent.com/br/blog/tls/](https://rockcontent.com/br/blog/tls/) 

*AWS IAM - Identity and Access Management - Amazon Web Services*. (n.d.). Amazon Web Services, Inc. [https://aws.amazon.com/pt/iam/](https://aws.amazon.com/pt/iam/) 

*O que é o IAM? - AWS Identity and Access Management*. (n.d.). [https://docs.aws.amazon.com/pt_br/IAM/latest/UserGuide/introduction.html](https://docs.aws.amazon.com/pt_br/IAM/latest/UserGuide/introduction.html) 

Ka, N. (2021, December 16). A Guide on Designing AWS Data Architectures - narjes ka - Medium. *Medium*. [https://medium.com/@karmeni.narjes.pro/a-guide-on-designing-aws-data-architectures-6a488ef9260c](https://medium.com/@karmeni.narjes.pro/a-guide-on-designing-aws-data-architectures-6a488ef9260c)
