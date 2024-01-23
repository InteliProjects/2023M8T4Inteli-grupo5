# Estrutura de Ingestão de dados com Armazenamento

## Identificação das Fontes de Dados e suas características

Neste contexto, é essencial compreender a natureza das diferentes bases de dados, classificando-as entre públicas e privadas, a fim de otimizar seu uso e garantir conformidade com regulamentos de privacidade.

### **Fontes Principais:**

**Dados Públicos:**

1. **Base POF - 500 MB (CSV, XLS)**
    - Utilização de 11 tabelas
    - Frequência de utilização: de acordo com o conjunto de dados que utilizaremos, a sua frequência de atualização é anual (*aproximadamente*)
2. **Base IBGE - 3 GB (CSV)**
    - A princípio, com utilização de duas tabelas
        - Prioridade para *Índice Nacional de Preços ao Consumidor*; *O PIB por município.*
    - Frequência de utilização: anual
3. **Base CNPJ - 4,6 GB (CSV)**
    - Utilização de 5 tabelas
    - Frequência de utilização: frequência será anual, tendo em consideração o tempo de pesquisa atribuído
4. **Base Dados Geográficos Brasileiros - Tamanho Não identificado (base de dados não operante - CSV)** 
    - Tabelas ainda não utilizadas
    - Importância que deve ser considerada para sua utilização: Os dados geográficos brasileiros foram selecionados para entender
    as demandas regionais.
    - Frequência de atualização: trimestralmente
5. **Base de Dados** **Pesquisa Nacional por Amostra de Domicílios Contínua - Tamanho Não identificado - (PNAD-C) - CSV**
    - Tabelas ainda não utilizadas
    - Importância que deve ser considerada para sua utilização: inferência da situação social das famílias brasileiras
    - Frequência de atualização: não listada

**Dados Privados:**

- A princípio serão fornecidos dados fictícios simulando a base de vendas de um distribuidor (conforme categorias, produtos, canais de venda, data) em tempo real, com base nas informações que o parceiro possuem. Serão disponibilizados por meio da API disponibilizada. Estes dados nos darão um embasamento maior e agregarão às outras fontes de dados.

## Seleção dos serviços da AWS

A escolha dos serviços desempenha um papel crucial na construção de uma infraestrutura de armazenamento eficiente e segura na nuvem. Ao abordar a necessidade de armazenamento de dados e a criação de um datalake inicial, a opção pelo Amazon S3 destaca-se como a melhor escolha em termos estratégicos. 

Ao optar pelo S3 para o armazenamento na nuvem, há maior capacidade de dimensionar verticalmente conforme as demandas crescentes de dados (tendo em vista que estaremos utilizando diversas fontes de dados de entrada). O serviço oferece uma solução confiável e durável para armazenamento de objetos, garantindo a integridade e disponibilidade dos dados. Além disso, a simplicidade na configuração e administração do Amazon S3 torna o processo de gerenciamento de dados mais eficiente e acessível.

### Segurança de dados:

 A segurança é outro aspecto fundamental para todo o fluxo que o grupo evidencia, e o S3 oferece recursos avançados de controle de acesso e criptografia para proteger os dados armazenados, que podem ser “setados” nas configurações iniciais de cada bucket

- Amazon Key Management System (KMS) → Há possibilidade de implementação do serviço KMS nos buckets de armazenamento. Neste caso, como estrutura acadêmica não implementamos a partir da limitação do uso dos serviços no Labs. No entanto é um aspecto de vital importância na construção de uma infraestrutura segura e eficiente. O KMS desempenha um papel crucial na gestão de chaves de criptografia, fornecendo uma camada adicional de segurança para os dados armazenados na nuvem.
- Virtual Private Cloud (VPC) **→** A VPC oferece a capacidade de criar segmentos na nuvem da AWS, permitindo o controle de acesso aos serviços utilizados. Isso inclui a implementação de restrições de acesso e regras de segurança, proporcionando uma camada adicional de proteção à solução.

## Processo de Ingestão de Dados e Mapa Mental dos Buckets

Nesta etapa da arquitetura, a Ingestão de Dados, compreende duas abordagens principais:

- O carregamento dos dados em formato Parquet (convertidos de CSV para Parquet) para a infraestrutura na nuvem.
    - Mais especificamente para Buckets no S3
- A transferência em tempo real dos dados do cliente através da API para o ambiente na nuvem.

Agora, abordaremos detalhadamente o primeiro método de ingestão:

Utilizando scripts em Python, efetua-se o envio de arquivos Parquet para buckets específicos na Amazon S3. 

- Cada fonte de dados possui seu próprio bucket designado
- A representação visual abaixo oferece uma visão organizacional clara do processo de ingestão de dados:

![mapa_mental_ingestao drawio](https://github.com/2023M8T4Inteli/grupo5/assets/99264567/eb2f4200-87d8-4c2a-968e-8e1faf54f9d4)

## Estrutura do Datalake

Para contextualização, o Datalake é basicamente um repositório que armazena grandes volumes de dados brutos, estruturados e não estruturados, em seu formato original. Diferente de um data warehouse, que segue um esquema de dados estruturado, o datalake permite realizar o armazenamento dos dados em sua forma bruta, sem a necessidade de uma estrutura pré-definida.

Isso significa que os dados podem ser coletados e armazenados de diferentes fontes, neste caso das formas especificadas. No contexto do projeto, tendo em vista o recebimento de diferentes fontes de dados, isto nos permite apenas se preocupar com etapas iniciais de pré-processamento. A princípio os dados são enviados em formato CSV e Parquet.

Neste caso, o serviço do datalake selecionado foi o S3 (com buckets específicos para cada uma das fontes).

Segue mapa mental, mais detalhista, do uso das fontes de dados e suas respectivas tabelas dentro do datalake:

![mapa_mental_datalake](https://github.com/2023M8T4Inteli/grupo5/assets/99264567/8b6dfe2d-1c3b-41fd-8d5c-635dcfa07aff)

## Dados carregados no Datalake (Amazon S3)

### Configuração do Bucket:

**Passo 1: Acesse o Console da AWS:**

- Vá para a página inicial da AWS ([https://aws.amazon.com/](https://aws.amazon.com/)), faça login na sua conta e acesse o Console da AWS.

**Passo 2: Navegue até o Amazon S3:**

- No Console da AWS, encontre o serviço "S3" ou digite "S3" na barra de pesquisa e selecione-o.

**Passo 3: Inicie o Processo de Criação:**

- Dentro do painel do Amazon S3, clique no botão "Criar bucket".

**Passo 4: Configure as Opções do Bucket:**

- Preencha as informações necessárias, incluindo um nome **único** para o seu bucket. O nome do bucket deve ser globalmente exclusivo, já que é usado no URL do bucket.
- Escolha, também, a região onde o bucket será armazenado.

**Passo 5: Configure as Propriedades do Bucket:**

- Configure as opções adicionais, como versão do bucket, logging, permissões de bloqueio, entre outros.

![image_720](https://github.com/2023M8T4Inteli/grupo5/assets/99264567/c7fb237f-85b0-432f-81a4-b6aa04ba7d29)

**Passo 6: Configure as Permissões do Bucket:**

- Defina as permissões do bucket, especificando quem pode acessar e modificar o conteúdo do bucket. Você pode configurar políticas de controle de acesso aqui.

![image_720](https://github.com/2023M8T4Inteli/grupo5/assets/99264567/c0d43fc3-2a96-4ec5-bbe9-40801e585dd9)

**Passo 7: Revise as Configurações e Crie o Bucket:**

- Revise todas as configurações feitas para garantir que estejam corretas. Clique em "Criar bucket" para confirmar e criar o novo bucket.

![image_360](https://github.com/2023M8T4Inteli/grupo5/assets/99264567/20a2133f-2223-4231-8cb7-e4a3b752f6d7)

**Passo 8: Acesse o Bucket:**

- Após a criação, você verá seu novo bucket listado no painel do Amazon S3. Clique nele para acessar e começar a gerenciar objetos (arquivos) dentro do bucket.

### Dados alimentados no Datalake (exemplo CNPJ e POF)

Separação dos buckets com base em cada uma das fontes de dados:

![Untitled (1)](https://github.com/2023M8T4Inteli/grupo5/assets/99264567/0f75c565-4375-4a95-bbbf-c698db15ddd8)

Tabelas ***tratadas** e que subidas automaticamente no datalake:

![Untitled (2)](https://github.com/2023M8T4Inteli/grupo5/assets/99264567/db78f218-5ab8-420b-a333-bd5cca53ab08)

*Todo o processo de envio dos dados está sendo feito por meio do script de envio já setado no código, mais especificamente no mcdata_package.

## Processo de Empacotamento

Tendo em vista o escopo do projeto, e processo de utilização das funções e funcionalidades criadas, foi necessário realizar um processo de empacotamentos das funções e criação de uma biblioteca própria para que o cliente possa acessar e utilizar suas funcionalidade. Como contexto, o processo de empacotamento para projetos em Big Data tem como principais objetivos: a eficiência, reusabilidade e escalabilidade nos projetos. 

Sendo assim, o processo foi divido em algumas etapas 

- **Empacotamento de Código:**
    - **Modularização:**
    Para facilitar a manutenção e o desenvolvimento, realizamos a modularização dos códigos em diferentes scripts e com orientação à objetos. Sendo assim, cada script possuía uma(s) função específica, facilitando a compreensão e a colaboração.
        - Especificamente neste caso, adotamos a parte de classes para que haja mais facilidade nessa manipulação das funções
- **Criação da Biblioteca:**
    - **Encapsulamento das Funções:**
    As funções são encapsuladas dentro da biblioteca. Possuindo assim métodos reutilizáveis que podem ser chamados em diferentes partes do projeto, promovendo a reusabilidade do código.
        - Organização Lógica: ****isso facilita a organização lógica do código, agrupando funcionalidades similares.
- **Ferramentas da Biblioteca:**
    - **Setuptools e Pip:** O `setuptools` é uma biblioteca Python que facilita a criação de pacotes Python. Ele é usado para empacotar a biblioteca, e em Python. O arquivo `setup.cfg` é utilizado para configurar os metadados do projeto e definir as instruções sobre como a biblioteca deve ser empacotada e instalada. O `pip` é uma ferramenta usada para instalar pacotes Python. Ele é usado para instalar as dependências necessárias para a biblioteca e para fazer o upload da biblioteca para o PyPI.
    - **PySpark**: O PySpark é a versão Python do Apache Spark, uma estrutura de processamento de dados em paralelo de código aberto. Ele é usado para processar grandes conjuntos de dados e realizar análises complexas. No pacote MCDATA_PACKAGE, o PySpark é usado para transformar arquivos CSV e RDS para o formato Parquet.
    - **Pandas**: O Pandas é uma biblioteca Python que é usada para manipulação e análise de dados. Ela é usada para manipular tabelas de dados no pacote.
    - **Boto3**: O Boto3 é a biblioteca Amazon Web Services (AWS) Software Development Kit (SDK) para Python. Ela é usada para interagir com o serviço de armazenamento de objetos da AWS, o S3.
    - **Twine**: O Twine é uma ferramenta usada para fazer o upload de pacotes Python para o PyPI.
    - **PyPI**: O PyPI (Python Package Index) é um repositório online de software para Python. Ele é usado para distribuir a biblioteca para outros usuários.
- **Distribuição e Versionamento:**
    - **Repositórios e Versionamento:**
    A bibliotecas é distribuída por meio do repositório, PyPI. O versionamento, é gerenciado pelo **`setup.config`**, e garante que diferentes versões da biblioteca possam ser controladas e instaladas conforme necessário.
    
    Para obter mais informações sobre procedimentos e configuração da biblioteca, acesse: 
    
    [https://github.com/2023M8T4Inteli/grupo5/blob/dev/src/mcdata_package/README.md](https://github.com/2023M8T4Inteli/grupo5/blob/dev/src/mcdata_package/README.md)
    
    [https://pypi.org/project/mcdata-package/](https://pypi.org/project/mcdata-package/)
