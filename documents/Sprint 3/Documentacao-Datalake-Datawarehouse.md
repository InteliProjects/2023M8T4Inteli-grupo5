# Documentação Data Lake/Data Warehouse Alimentado pelo ETL

Neste documento explicaremos um pouco sobre o processo de inserção e formatação dos dados dentro do Datawarehouse. Cada uma das seções explicará um tópico específico deste processo contínuo desenvolvido na Sprint 3. 

# Fontes de dados

A razão para a escolha das fontes de dados utilizadas é a construção da possibilidade de se gerar uma visão abrangente e detalhada sobre o poder aquisitivo de diferentes regiões, sobre diferentes canais de venda ao redor do país e sobre os mercados e suas dinâmicas em cada lugar. Essas fontes devem permitir juntas a construção de análises úteis para a consultoria que trabalha com Go To Market e para a qual seria valioso comparar informações relacionadas a estes assuntos. Segue descrição das fontes de dados utilizados:

**Dados da ANVISA →** possibilita a análise de poder aquisitivo por região, uma vez que exerce a vigilância sanitária sobre produtos e serviços no âmbito nacional. Duas tabelas foram utilizadas: uma de dados abertos sobre alimentos e uma sobre petições alimentícias.  Estes dados possibilitam a construção de uma visão sobre hábitos de consumo e sobre outros aspectos relacionados a alimentos em diferentes regiões.

**Dados do Bacen →** O BACEN permite o acesso a informações sobre taxa selic, inflação e o valor da moeda em dólar. A coleta destes dados é essencial para que sejam traçadas visões gerais sobre a economia nas regiões de diferentes clientes. 

**Dados de CNPJ →** O CNPJ armazena informações cadastrais das pessoas jurídicas e de outras entidades. Estes dados possibilitam um mapeamento granular dos diferentes canais de venda que habitam os mercados em regiões diversas.

**Dados da POF →** O POF (Pesquisa de Orçamentos Familiares) visa analisar as condições de vida da população brasileira a partir da análise de seus orçamentos.

**Dados do IBGE→** Instituto Brasileiro de Geografia e Estatística, analisa o território, a população e como a economia evolui através da produção e do consumo, revelando ainda aspectos de condições de vida das pessoas.

Ambas as fontes, POF e IBGE em geral, possibilitam o acesso a informações relacionadas ao poder aquisitivo de cada região na medida em que apresentam dados sobre a composição dos orçamentos domésticos e sobre as condições de vida da população. 

**Dados coletados com a API →** Por fim, a API do cliente disponibiliza um CSV com todas as vendas realizadas por CNPJ, apresentando a data, o valor e a quantidade atrelados a cada um. Isso é essencial, uma vez que permite uma visualização objetiva das dinâmicas que ocorrem em diferentes mercados, tanto na questão econômica quanto na questão estritamente sobre consumo. É importante salientar que este dados são referentes a uma base de vendas fictícia fornecidas pela Integration.

## Premissa de inclusão das Novas Fontes (Dados do Bacen e Dados da Anvisa)

A partir da revisão da última sprint e feedbacks passados pelo cliente, foi de comum acordo que havia necessidade de pensar diferente e incluir dados que poderiam trazer insights valiosos, e que ainda não foram incluídos e utilizados pela Integration. Neste sentido, trouxemos mais duas fontes de dados, no âmbito financeiro e outros dados referentes a Agência Nacional de Vigilância Sanitária.

### Dados da Anvisa

A ANVISA (Agência Nacional de Vigilância Sanitária) disponibiliza dados abertos relacionados à petição de alimentos e dados referentes a alimentos e seus termos regulatórios. Esses dados podem ser valiosos para empresas no setor alimentício ao tomar decisões estratégicas, especialmente no contexto de go-to-market (inserido na presença da Integration e os insights tirados). Abaixo estão alguns pontos-chave que destacam a importância desses dados e seu impacto nas estratégias de go-to-market:

1. **Segurança Alimentar e Conformidade:** Os dados de petição de alimentos da ANVISA podem fornecer informações sobre a conformidade de produtos alimentícios com regulamentações e padrões de segurança alimentar. 
    1. Empresas podem utilizar esses dados para garantir que seus produtos atendam aos requisitos regulatórios, evitando problemas legais e protegendo a reputação da marca.
2. **Avaliação da Competição:** Ao analisar as petições de alimentos submetidas por outras empresas do setor, é possível obter insights sobre as estratégias e inovações dos concorrentes. Isso permite que as empresas ajustem suas próprias estratégias de go-to-market para se destacarem no mercado e oferecerem produtos mais alinhados com as demandas dos consumidores.
3. **Desenvolvimento de Produtos:** Os dados de petição de alimentos podem ser uma fonte valiosa para identificar tendências de mercado e demandas dos consumidores. As empresas podem utilizar essas informações para orientar o desenvolvimento de novos produtos que atendam às necessidades específicas do mercado.
4. **Gerenciamento de Riscos:** Acompanhar as petições de alimentos pode ajudar as empresas a identificar potenciais riscos e problemas de segurança alimentar no mercado. Isso permite uma abordagem proativa na gestão de riscos, minimizando impactos negativos na reputação da empresa.
5. **Tomada de Decisões Estratégicas:** Com base nos dados da ANVISA, as empresas podem tomar decisões mais informadas sobre sua presença no mercado. Isso inclui decisões relacionadas à expansão geográfica, ajustes no portfólio de produtos e aprimoramento de estratégias de marketing e distribuição.
6. **Transparência e Confiança do Consumidor:** Utilizar dados de petição de alimentos e seguir as práticas recomendadas pela ANVISA pode aumentar a transparência das operações de uma empresa. Isso, por sua vez, pode fortalecer a confiança dos consumidores, pois eles percebem que a empresa está comprometida com a segurança e conformidade alimentar.

### Dados do Bacen

A inclusão da fonte de dados com informações do Banco Central do Brasil (BACEN), como a taxa Selic, a expectativa de inflação e o preço do dólar, pode proporcionar uma visão mais abrangente e estratégica para o cliente. Aqui estão algumas dessas oportunidades, no contexto do projeto:

1. **Custo de Produção e Impacto Econômico:**
    - **Taxa Selic e Inflação:** A taxa Selic e a expectativa de inflação podem influenciar os custos de produção, financiamento e investimento. Monitorar esses indicadores ajuda as empresas a entenderem os impactos econômicos gerais em suas operações.
2. **Cadeia de Suprimentos e Custos Logísticos:**
    - **Preço do Dólar:** O preço do dólar afeta diretamente os custos de importação de ingredientes e matérias-primas. Uma variação no câmbio pode impactar os custos logísticos e, consequentemente, os preços finais dos produtos.
3. **Decisões de Precificação e Estratégias de Mercado:**
    - **Inflação e Câmbio:** A expectativa de inflação e o preço do dólar podem influenciar as estratégias de precificação. As empresas podem ajustar os preços de acordo com as condições econômicas para manter a competitividade e a rentabilidade.
4. **Investimentos em Pesquisa e Desenvolvimento:**
    - **Taxa Selic:** Mudanças na taxa Selic podem afetar os custos de capital e financiamento para projetos de pesquisa e desenvolvimento. Acompanhar a taxa Selic é crucial para avaliar o ambiente de investimento.
5. **Planejamento Estratégico e Expansão de Mercado:**
    - **Câmbio e Inflação:** Flutuações cambiais e expectativas de inflação podem influenciar as estratégias de expansão para novos mercados. As empresas podem ajustar suas abordagens com base nas condições macroeconômicas.
6. **Gestão de Riscos e Estabilidade Financeira:**
    - **Taxa Selic e Câmbio:** A taxa Selic pode impactar o custo do capital, enquanto as variações cambiais podem representar riscos financeiros. Uma gestão eficaz desses riscos é crucial para a estabilidade financeira.
7. **Compreensão do Consumidor e Estratégias de Marketing:**
    - **Inflação:** A expectativa de inflação pode influenciar o poder de compra dos consumidores. Compreender essas tendências é essencial para ajustar estratégias de marketing e comunicação.

# Etapas do ETL

O ETL (Extração, Transformação e Carga) envolve a coleta de dados de diversas fontes, a aplicação de transformações para garantir qualidade e consistência, e o carregamento dos dados em um destino, neste caso, um data warehouse. O ETL é necessário para a conversão de grandes volumes de dados brutos em informações valiosas, facilitando a inteligência de negócios e a tomada de decisões informadas.

Explicação mais detalhada:

**Extração**

- A Extração é a primeira fase do processo ETL, onde os dados são coletados de várias fontes que podem variar desde bancos de dados até serviços na nuvem. A extração deve ser projetada de forma a minimizar o impacto no desempenho dos sistemas de origem e deve ser eficiente em termos de recursos para lidar com o volume de dados extraídos dentro do tempo disponível.

**Transformação**

- A Transformação é a segunda fase do ETL. Durante esta etapa, os dados extraídos são limpos, validados e transformados para se adequarem ao esquema do data warehouse de destino. As transformações podem incluir a conversão de tipos de dados ou a aplicação de funções de negócios para calcular métricas de negócios.

**Carga**

- A Carga é a última fase do ETL. Nesta etapa, os dados transformados são carregados no data warehouse de destino. O processo de carga também deve garantir que os dados sejam carregados de forma eficiente e que o data warehouse permaneça disponível e estável durante o processo de carga.

Na nossa solução, a etapa de extração foi realizada a partir do DataLake, especificamente do AWS S3, utilizando os buckets que compõem esse DataLake, como o bucket "grupo-5-mec-solutions-bucket-dados-financeiros-conta-nova". A extração dos dados foi feita diretamente pelo AWS Redshift, permitindo que todas as tabelas localizadas nos buckets possam ser manipuladas e transformadas.

As transformações realizadas nos dados extraídos incluíram a modificação das informações das colunas para torná-las mais visuais e compreensíveis, como a mudança do número do estado para o nome do estado (11 → São Paulo). Outro exemplo foi normalização das colunas, para que todas tabelas com colunas semelhantes em csvs distintos tivessem o mesmo nome.

Mais alguns tratamentos feitos:

![image](https://github.com/2023M8T4Inteli/grupo5/assets/99208930/653be380-ca3b-4ad4-8fa9-ad5a043f4002)

![image](https://github.com/2023M8T4Inteli/grupo5/assets/99208930/7019de0d-27fd-417b-8a80-6e19b8e25a82)

![image](https://github.com/2023M8T4Inteli/grupo5/assets/99208930/df43262a-323c-47b0-9dab-8748c5b3b389)


Por fim, na fase de carga, novamente utilizamos o AWS Redshift para incorporar os dados processados pelo ETL no data warehouse, garantindo assim uma organização ordenada. Este ciclo completo do ETL é fundamental para manter a integridade e a utilidade dos dados, proporcionando uma base robusta para análises avançadas e decisões estratégicas bem fundamentadas.

# Serviços de ETL e armazenamento

Escolhemos o Amazon Redshift como nossa solução principal para ETL  e armazenamento de dados, principalmente devido às suas características orientadas para processamento analítico online (OLAP) e a sua conexão fácil com o AWS S3 (datalake), permitindo uma extração facilitada dos dados. Outro ponto que consideramos foi a escalabilidade dos serviços e sua utilização.

Alguns pontos que também foram importantes para a escolha desse serviço foram:

 **Arquitetura colunar**: Ao contrário de bancos de dados relacionais tradicionais que armazenam dados em linhas, os bancos de dados colunares organizam os dados em colunas e, assim, otimiza as consultas OLAP, pois permite a leitura seletiva das colunas relevantes, minimizando o tempo de busca e aumentando o desempenho geral.

**Computação distribuida**: Em vez de depender de um único sistema centralizado para realizar todas as tarefas, a carga de trabalho é distribuída entre vários dispositivos para melhorar a eficiência, escalabilidade e confiabilidade do sistema como um todo. → “O Redshift é 10 vezes mais rápido do que Hadoop. Em alguns testes de consulta, o banco de dados Redshift supera facilmente o Hadoop ao retornar resultados.” (**5 benefícios em usar o Redshift para Data Warehouse)**

**Monitoramento de clusters**: O Redshift oferece várias ferramentas de monitoramento, permitindo rastrear a integridade e o desempenho dos clusters e bancos de dados (será abordado mais a frente no documento) → “O **[Redshift](https://aws.amazon.com/pt/redshift/)** apresenta algumas ferramentas diferentes de criptografia e segurança que tornam a proteção de depósitos ainda mais fácil.” (**5 benefícios em usar o Redshift para Data Warehouse)**

Essas características fazem do Amazon Redshift a nossa escolha de datawarehouse, proporcionando escalabilidade, desempenho e facilidade de uso.

# Descrição da estrutura do Data Warehouse

O Data Warehouse é uma ferramenta fundamental para organizar e disponibilizar informações para a tomada de decisões estratégicas. Entre as diversas plataformas disponíveis, destaca-se o Amazon Redshift, um sistema de gerenciamento de banco de dados especialmente projetado para armazenar e analisar grandes conjuntos de dados. Ele foi o serviço escolhido para construção do datawarehouse.

Neste contexto, exploraremos a estrutura do Data Warehouse no ambiente OLAP (Online Analytical Processing), onde a ênfase recai sobre a capacidade de analisar dados multidimensionais de maneira eficiente.

Primeiramente, é preciso entender os dois diferentes tipos de processamento que foram considerados na possível agregação na arquitetura de ingestão de dados. O OLAP (Online Analytical Processing) e OLTP (Online Transaction Processing), desempenham papéis distintos e vitais no ecossistema da gestão de informações. Estas duas abordagens, embora compartilhem a mesma base de dados, são orientadas para propósitos específicos, refletindo suas características e funcionalidades únicas.

### OLAP

O OLAP, centrado na análise, é utilizado com a intenção de extrair conhecimento significativo a partir de grandes conjuntos de dados. Sua estrutura multidimensional permite relações entre diferentes variáveis de forma intuitiva, utilizando cubos de dados organizados em dimensões. Esse sistema foi escolhido para ser utilizado no projeto por suas características de inferência mais analítica e fácil processamento de dados complexos e grandes. 

É importante citar que o ambiente em sistemas OLAP é particularmente eficaz para consultas pesadas e relatórios estratégicos, oferecendo uma visão abrangente do desempenho organizacional e padrões no cubo de dados.

### OLTP

Em contraste, o OLTP é otimizado para o processamento eficiente de transações em tempo real. É muito utilizado em ambientes transacionais, como sistemas de gerenciamento de banco de dados operacionais. No contexto deste sistema o foco recai sobre a rapidez e a precisão na execução de operações individuais, como inserção, atualização e exclusão de registros. A normalização é frequentemente aplicada para garantir a integridade dos dados, evitando redundâncias e mantendo a consistência em cenários dinâmicos.

### Mais diferenças

Para entender melhor sua aplicabilidade, é importante diferenciar os conceitos e utilização desses sistemas em arquiteturas de Big Data. Uma das principais distinções reside na maneira como esses sistemas tratam a concorrência de acesso aos dados. Enquanto o OLAP prioriza a leitura simultânea de dados por vários usuários, o OLTP é projetado para lidar com a concorrência de gravação, garantindo a consistência dos dados em ambientes onde múltiplas transações ocorrem simultaneamente. As necessidades de armazenamento e recuperação de dados também diferem substancialmente entre OLAP e OLTP. O OLAP frequentemente emprega estratégias de armazenamento de dados em formato desnormalizado, visando otimizar o desempenho das consultas analíticas. Por outro lado, o OLTP favorece abordagens normalizadas para minimizar o espaço de armazenamento e assegurar a integridade dos dados nas transações diárias.

Com intuito de uma visualização mais intuitivas, representamos as características de cada um dos sistemas, destacando o OLAP que foi o escolhido para a arquitetura de ingestão:

![image](https://github.com/2023M8T4Inteli/grupo5/assets/99208930/67563b70-477e-47fe-a747-0d20ffbcd153)


O Amazon Redshift, oferece também uma abordagem eficiente para a organização de dados em um ambiente analítico. Em sua construção ele faz a formatação dos dados e em sua entrada posiciona-os de maneira relacional, utilizando um sistema de arquivos distribuídos para otimizar o acesso e a manipulação de informações.

### **Organização Relacional:**

A estrutura relacional do Amazon Redshift é fundamentada nos princípios da modelagem dimensional. Os dados são organizados em tabelas, seguindo esquemas como o star schema ou snowflake schema. O star schema, por exemplo, envolve uma tabela fato central, que contém as métricas a serem analisadas, e tabelas de dimensões que fornecem contexto aos dados. Isso simplifica as consultas, permitindo que os usuários explorem relações multidimensionais de maneira eficiente.

As tabelas são distribuídas em "slices" dentro dos nós de processamento do cluster do Redshift. Cada nó é uma unidade de computação independente, e a distribuição das tabelas entre esses nós é projetada para otimizar o desempenho das consultas. O Redshift permite a escolha do método de distribuição mais adequado para cada tabela, oferecendo flexibilidade para adaptar a arquitetura à natureza dos dados e dos padrões de consulta.

### **Sistema de Arquivos Distribuídos:**

Outro característica muito legal do Redshift é seu processamento distribuído. O sistema armazena dados em um sistema de arquivos distribuídos, onde os dados de cada tabela são particionados em blocos e distribuídos entre os nós do cluster. Cada nó é capaz de processar consultas localmente nos dados armazenados em seu próprio espaço de armazenamento, minimizando a necessidade de transferência de dados entre os nós durante a execução de consultas.

A estrutura de coluna do Redshift também desempenha um papel importante na otimização do armazenamento e recuperação de dados. Os dados são armazenados de forma colunar em vez de linha, o que permite a compressão eficiente e a leitura seletiva de colunas durante as consultas, resultando em tempos de resposta mais rápidos (isso pode ser evidenciado nas métricas dos alarmes em cada serviço salientadas no tópico “Proposta de monitoramento e gerenciamento do ETL” desta documentação).

![image](https://github.com/2023M8T4Inteli/grupo5/assets/99208930/0a45c11e-23a4-4f41-98aa-83a5a5a62651)


### Informações do Ambiente

![image](https://github.com/2023M8T4Inteli/grupo5/assets/99208930/3c46beec-8071-454a-979c-2ae08d30caee)


![image](https://github.com/2023M8T4Inteli/grupo5/assets/99208930/2faaff2a-d187-45a2-9b25-376b70e2cd90)


- **Namespace:** aula-afonso
- **ID do Namespace:** 3af09ae1-e265-4a72-b980-796bfef5b657
- **ARN do Namespace:** arn:aws:redshift-serverless:us-east-1:187967616478:namespace/3af09ae1-e265-4a72-b980-796bfef5b657
- **Data de Criação:** 21 de Novembro, 2023, 16:59 (UTC-03:00)
- **Usuário Admin:** admin
- **Nome do Banco de Dados:** dev
- **Armazenamento Utilizado:** 27,2 GB
- **Contagem Total de Tabelas:** 12

### Snapshot

O snapshot como uma cópia de um cluster do Redshift, os snapshots são ferramentas valiosas para a recuperação de dados, backup e manutenção da integridade do ambiente de armazenamento. Esses instantâneos fornecem uma maneira eficaz de preservar o estado consistente dos dados, permitindo que as organizações restaurem clusters a um ponto anterior no tempo em caso de falhas, erros ou necessidades de análise histórica. 

Segue detalhes e comprovação da criação do Snapshot:

![image](https://github.com/2023M8T4Inteli/grupo5/assets/99208930/5a20d9ae-e221-40fa-bf27-4c7c56df94b1)

![image](https://github.com/2023M8T4Inteli/grupo5/assets/99208930/760d13cc-f166-42af-bf35-58fdbffd35b0)

# Views + Tabelas do Redshift

As views para um contexto de definição e estruturação do Datawarehouse desempenham um papel muito importante, agindo como representações virtuais de tabelas derivadas de uma ou mais fontes de dados. Estas views não armazenam dados fisicamente, mas facilitam a consulta e manipulação dos dados de forma simplificada e eficiente.

Segue Organização das Tabelas e Views no Redshift:

![image](https://github.com/2023M8T4Inteli/grupo5/assets/99208930/eb273f45-9e50-481b-b0a5-bfa0226389a0)

## O que é?

As Views em SQL, podem ser definidas como consultas armazenadas que funcionam como tabelas virtuais. Elas são construídas com base em consultas SQL, permitindo aos usuários acessar e manipular dados de maneira simplificada (*Material Didático - IMD*, n.d.).

## Para que serve?

As views têm uma variedade de propósitos em um banco de dados SQL. Elas são utilizadas para simplificar a complexidade do esquema, oferecendo uma camada de abstração sobre as tabelas subjacentes. Além disso, as views são valiosas para a segurança de dados, permitindo a imposição de políticas de restrição de acesso. Elas facilitam a personalização da apresentação dos dados, agregação e resumo, contribuindo para a eficiência na análise e tomada de decisões. As views também desempenham um papel importante na padronização da visualização dos dados, promovendo uma interpretação consistente dentro da organização.

## Benefícios

Um dos principais benefícios das views é a segurança de dados. Elas possibilitam a imposição de políticas de segurança, restringindo o acesso dos usuários apenas às informações pertinentes às suas funções, garantindo assim a integridade e confidencialidade dos dados. Além disso, as views permitem personalização da visualização, permitindo que os usuários organizem e apresentem os dados de acordo com suas necessidades específicas. Isso é particularmente útil em ambientes nos quais diferentes partes da organização precisam interpretar os mesmos dados de maneiras distintas.

A capacidade de agregação e resumo é outra vantagem das views, possibilitando a criação de visualizações que resumem informações, facilitando a identificação de tendências e padrões. Esse recurso é essencial para uma análise eficaz, especialmente em Data Warehouses que lidam com grandes volumes de dados. Além de contribuir para a eficiência na análise, as views também podem ser otimizadas para melhorar o desempenho das consultas, o que é crucial em ambientes de Data Warehouse nos quais a eficiência no acesso aos dados é fundamental. A padronização da apresentação é promovida pela criação de views padronizadas, o que garante uma representação consistente dos dados e facilita a comunicação dentro da organização. Isso cria uma compreensão uniforme da estrutura do banco de dados e dos relacionamentos entre as tabelas.

No âmbito prático, a utilização de views não apenas simplifica a interpretação de dados complexos, mas também suporta a tomada de decisões informadas. Ao fornecer uma visão clara e personalizada dos dados, as views capacitam os usuários a tomar decisões estratégicas com base nas informações disponíveis no Data Warehouse.

Em resumo, as views desempenham um papel fundamental na maximização do valor dos dados armazenados em um Data Warehouse, facilitando a compreensão, análise e utilização eficaz das informações pelos usuários.

## Como foi aplicado?

Dado o contexto do projeto, projetamos algumas views de exemplo para começar a visualizar a correlação e definir algumas premissas iniciais para tomada de decisão na parte da identificação de padrões.

A primeira view criada, foi realizada com o intuito de visualizar relações entre dados de petição de alimentos da ANVISA e dados do Banco Central (BACEN). Neste caso foi criado para que simplificasse a análise em relação a estes dados. Foi construída também para mostrar a relação entre petições de alimentos e indicadores econômicos, como a taxa Selic e o preço do dólar. Isso permite uma visão abrangente no setor alimentício, com insights adicionais como fatores econômicos que impactam as petições e permitem que a empresa adaptem suas estratégias.

### Dados Anvisa vs Dados do Bacen

![image](https://github.com/2023M8T4Inteli/grupo5/assets/99208930/1811616e-845f-4fd5-bb0c-ccd2b62680a9)

Query breakdown:

```sql
CREATE VIEW public.anvisa_bacen_view AS
SELECT
    a.*,
    b.*
FROM
    public.anvisa a
JOIN public.bacen b ON a.data_fim_ocorrencia_grp_etapa = b.data;
```

```sql
CREATE
OR REPLACE VIEW "public"."anvisa_bacen_view" AS
SELECT
   a.num_expediente_peticao,
   a.num_processo_peticao,
   a.s_n_peticao_primaria,
   a.cod_assunto_peticao,
   a.desc_assunto_peticao,
   a.data_situacao_atual_peticao,
   a.desc_situacao_atual_peticao,
   a.data_primeira_finalizacao,
   a.data_finalizacao_atual,
   a.desc_tipo_documento,
   a.desc_area_interesse,
   a.desc_fila_analise,
   a.desc_sub_fila_lista_analise,
   a.desc_grupo_etapa_ciclo_analise,
   a.data_ini_ocorrencia_grp_etapa,
   a.data_fim_ocorrencia_grp_etapa,
   a.ordem_ocorre_grupo_etapa_asc,
   a.ordem_ocorre_grupo_etapa_desc,
   b."data",
   b.usd,
   b.taxa_selic,
   b.taxa_exp_inflacao
FROM
   anvisa a
   JOIN bacen b ON a.data_fim_ocorrencia_grp_etapa = b."data":: timestamp without time zone;
```

Inferências e correlação identificadas por meio da criação da view acima:

![image](https://github.com/2023M8T4Inteli/grupo5/assets/99208930/8daf4337-969b-4984-a187-63099b7a42f2)


*dados de 2005 apenas como exemplificação

Da mesma forma, relacionamos os dados de CNPJ com informações de vendas de uma empresa do setor alimentício provisionados pela API do cliente. A view podem ser utilizada para criar uma visão consolidada que mostra a performance de vendas. Isso facilita a análise de padrões de vendas, identificação de clientes importantes e otimização de estratégias de marketing e distribuição.

### Dados da API do Parceiro vs Dados de CNPJ

![image](https://github.com/2023M8T4Inteli/grupo5/assets/99208930/889fc32a-6c45-464e-bb6d-772cf7d0575f)

Query breakdown: 

```sql
CREATE
OR REPLACE VIEW "public"."cnpj_integration" AS
SELECT
   y.id,
   y.cnpj,
   y.idcategory,
   y.produto,
   y."data",
   y.preco,
   y.quantidade,
   z.cnpj AS cnpj_cnpj2_dados,
   z.nome_fantasia,
   z.sigla_uf
FROM
   parceiro2 y
   JOIN cnpj2_dados z ON y.cnpj = z.cnpj;
```

Inferências e correlação identificadas por meio da criação da view acima:

![image](https://github.com/2023M8T4Inteli/grupo5/assets/99208930/60c26558-2a38-48cb-8a44-e30504a72c79)


Por fim, é possível inferir que a criação de views oferece uma abordagem flexível e poderosa para visualizar e analisar relações entre dados, proporcionando uma visão personalizada e eficiente para suportar a tomada de decisões estratégicas.

# Segurança / Privacidade / Conformidade

Para assegurar a integridade, segurança e conformidade regulatória dos dados durante o processo de ELT (Extract, Load, Transform), foram adotadas medidas específicas:

### Segurança dos Dados:
- **Criptografia de Dados em Trânsito:** Utilização de protocolos de criptografia SSL/TLS durante a transferência de dados do Amazon S3 para o Amazon Redshift, garantindo que os dados sejam transmitidos de forma segura.
- **Controle de Acesso:** Implementação de políticas de controle de acesso granulares, baseadas em IAM (Identity and Access Management), para garantir que apenas usuários autorizados possam acessar os dados e realizar operações no Redshift.

![Captura de tela 2023-11-26 225749](https://github.com/2023M8T4Inteli/grupo5/assets/99264567/85318ed7-1438-4a8e-8ac1-f830dcfc3be8)


### Privacidade dos Dados:
- **Dados Públicos ou Fictícios:** Considerando que os dados utilizados são públicos ou fictícios, não foi aplicada a prática de anonimização ou mascaramento de dados, uma vez que não contêm informações identificáveis ou sensíveis.

### Backup de Segurança:
- **Snapshot:** Implementamos um procedimento de criação regular de snapshots dos dados no Amazon Redshift. Isso nos permite manter cópias de segurança dos dados, proporcionando uma camada adicional de segurança em caso de problemas ou necessidade de recuperação.

![Captura de tela 2023-11-26 225533](https://github.com/2023M8T4Inteli/grupo5/assets/99264567/fa4eeb5a-df32-478b-90cf-b2c6aad0b5a7)


Estas medidas foram implementadas considerando as melhores práticas de segurança e conformidade, adequadas ao contexto de dados públicos ou fictícios, assegurando a proteção dos dados e o atendimento aos requisitos regulatórios aplicáveis.


# Proposta de monitoramento e gerenciamento do ETL

No contexto de monitoramento e gerenciamento do processo ETL (Extract, Transform, Load), o Amazon CloudWatch emerge como uma proposta robusta e abrangente. Este serviço desempenha um papel fundamental ao oferecer uma solução eficaz para coleta de métricas, operações e logs relacionados a recursos de aplicativos e infraestruturas. A utilização do CloudWatch não apenas proporciona uma visão unificada dos recursos, mas também permite a identificação e resolução proativa de problemas, otimizando a eficiência da infraestrutura e a manutenção da aplicação. Com isso, assegura-se um monitoramento eficiente para garantir o pleno funcionamento dos serviços selecionados

Segue dashboard criado pelo grupo:

![image](https://github.com/2023M8T4Inteli/grupo5/assets/99208930/3d3aa79c-82f6-49c7-9664-1a2d71b1c614)

# Gráficos

### Total de tabelas:

**Duração das querys e querys por minuto:**

1. **Duração das Queries:**

Mede o tempo que uma consulta leva para ser executada. Ajuda a identificar e otimizar consultas lentas, melhorando a eficiência do banco de dados.

1. **Queries por Minuto:**

Indica o número de consultas executadas por minuto. Revela a carga de trabalho do banco de dados ao longo do tempo, facilitando ajustes de recursos conforme necessário.

Essas métricas são cruciais para manter o desempenho e a eficiência do banco de dados, mesmo sem o uso específico do Amazon CloudWatch. Utilize outras ferramentas de monitoramento ou as métricas internas do seu sistema de gerenciamento de banco de dados.

### **Relatório de querys:**

O CloudWatch geralmente oferece métricas relacionadas ao desempenho, como CPU, I/O de disco, número de conexões e outras métricas específicas do banco de dados. Essas métricas podem ser úteis para avaliar o desempenho geral do banco de dados e identificar possíveis problemas.

### QueryRuntimeBreakdown:

Métricas relacionadas ao desempenho de consultas podem incluir informações sobre o tempo de execução de consultas, detalhes sobre a distribuição do tempo gasto em diferentes componentes da consulta (como processamento no lado do servidor, transferência de dados, etc.) e outros fatores que podem impactar o desempenho geral do sistema.

# Alarmes

No CloudWatch é possível configurar alarmes para casos diversos. Cada alarme contém os parâmetros nome, estado, última atualização de estado, condições e ações. O parâmetro “estado” define se o alarme está desativado, se está “ok” ou se está “em alarme” (caso no qual as condições definidas são detectadas como a situação atual do sistema). 

O parâmetro “ações” permite que ações sejam realizadas quando as condições forem satisfeitas, como enviar um email de alerta para determinados endereços de email. 

1. **Excesso de queries completadas por segundo:**
- **Condições**: QueriesCompletedPerSecond > 0.15 para 1 pontos de dados em 1 dia
- **Utilidade:** Este alarme é útil para monitorar a carga de trabalho do sistema em relação ao número de consultas (queries) que está processando por segundo. Pode ajudar a identificar picos de tráfego inesperados ou avaliar se sua infraestrutura está lidando adequadamente com a demanda.

1. **Tempo excedente de execução:**
- **Condições**: QueryRuntimeBreakdown > 3880 para 1 pontos de dados em 5 minutos
- **Utilidade:** Este alarme é configurado para alertar quando o tempo de execução de uma operação específica excede um limite definido. Por exemplo, se você tem uma função serverless que normalmente leva apenas alguns segundos para ser concluída, um tempo de execução significativamente maior pode indicar problemas de desempenho ou gargalos.

1. **Duração excessiva das queries**
- **Condições**: QueryDuration > 1970000 para 1 pontos de dados em 5 minutos
- **Utilidade:** Este alarme monitora o tempo que as queries levam para serem executadas. Se o tempo de execução de uma consulta exceder a condição definida, o alarme será acionado. Isso é útil para identificar consultas que podem estar afetando o desempenho geral do sistema.

---

## Fontes:

*Material didático - IMD*. (n.d.). [https://materialpublic.imd.ufrn.br/curso/disciplina/3/73/14/2](https://materialpublic.imd.ufrn.br/curso/disciplina/3/73/14/2) 

User. (2023, April 12). *5 benefícios em usar o Redshift para Data Warehouse*. eMaster Cloud E Security. [https://emaster.cloud/data-analytics/5-beneficios-em-usar-o-redshift-para-data-warehouse/](https://emaster.cloud/data-analytics/5-beneficios-em-usar-o-redshift-para-data-warehouse/) 

*Usar alarmes do Amazon CloudWatch - Amazon CloudWatch*. (n.d.). [https://docs.aws.amazon.com/pt_br/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html](https://docs.aws.amazon.com/pt_br/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html)
