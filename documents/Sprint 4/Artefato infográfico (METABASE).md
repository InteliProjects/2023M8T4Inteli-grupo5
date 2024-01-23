# Visualização de dados na Metabase

A Metabase é uma plataforma que permite, a partir de bases de dados, a criação de gráficos com filtros e com sumarização. Esta plataforma foi utilizada para a geração de um esboço de um infográfico, seguindo algumas diretrizes como clareza nas informações, concisão nos gráficos e atração visual. A geração de cada gráfico foi seguida de uma análise sobre sua eficácia e de uma coleta de informações sobre possíveis melhorias em cada caso e contexto específico.

## Dataframe utilizado

Primeiramente vale ressaltar que a escolha do Dataframe utilizado para as análises tinha como critério a possibilidade do cruzamento de informações sobre canal, categoria e região. Tendo isto em vista, foi realizada a junção (ou um “join”) de diferentes tabelas que estavam presentes no Data Warehouse, como tabelas do CNPJ, que possuem em sua maioria valores sobre região, ou como a tabela da API do cliente, que identifica os produtos e fornece especificações a respeito de cada um.

Por fim, as colunas que foram tornadas disponíveis para uso e que valem ser destacadas aqui são: “produto”, “preço”, “quantidade”, “sigla UF”, “Usd” e “Mês”. A plataforma Metabase torna possível cruzar de diferentes maneiras estas informações, gerando insights e análises relevantes para o cliente.

![image](https://github.com/2023M8T4Inteli/grupo5/assets/99270135/dda2a3ba-0b93-477c-b7e8-2afb97566807)

A plataforma utilizada para dar início ao infográfico permite a criação de dashboards separados, dividindo assim gráficos relacionados a análises distintas na plataforma. Sendo assim, foi feita uma divisão entre gráficos sobre o país inteiro e gráficos relacionados a um UF em específico.

Estes gráficos podem, ainda, servir a propósitos mais específicos do que o exemplo utilizado para a distinção, de análises por UF. Vale ressaltar, portanto, que por hora a distinção estará restrita a estes dois aspectos, mas que pode vir a sofrer alterações e possíveis incrementos, gerando assim uma maior granularidade para os assuntos tratados em cada dashboard.

## Dashboard geral

Em primeira instância, os gráficos para análise do país em geral apresentam diferentes níveis de detalhamento e especificidade. Alguns dos gráficos apresentam informações sobre regiões do Brasil em um mapa em relação a toda a base de dados, sem o uso de filtros específicos.

![image](https://github.com/2023M8T4Inteli/grupo5/assets/99270135/6c42551d-d78d-4b21-8658-6bd4db614c0f)


Consequentemente, outros gráficos podem ser construídos com o objetivo de tornar a análise mais granular, como filtrando o mês sobre o qual se deseja ver as informações.

![image](https://github.com/2023M8T4Inteli/grupo5/assets/99270135/9b8c95bc-eb1b-430c-aea1-54697f6e16b5)

Seguindo a ideia de especificar os gráficos a fim de servir diferentes contextos, o gráfico de linha foi utilizado com um filtro que separa alguns UF específicos e apresenta os resultados com o passar dos meses relacionados a cada um. No caso utilizado, os resultados apresentados foram sobre a venda de um produto específico, portanto, um filtro relacionado a coluna “produtos” também foi aplicado.

![image](https://github.com/2023M8T4Inteli/grupo5/assets/99270135/cfa54d07-88c7-40cb-99b1-2a38448ac8ca)

Esta mesma análise pode ser realizada sem o filtro por UF. A diferença aqui é que o gráfico não pode ser de linha neste caso e deve ser, portanto, uma tabela, que permite uma análise menos intuitiva mas significativamente mais objetiva das informações obtidas a partir da base de dados.

![image](https://github.com/2023M8T4Inteli/grupo5/assets/99270135/7e34a97b-c6a6-4769-b3b6-63d2d7b006d4)


Por fim, sobre o Brasil em geral pode ser feita a análise do impacto do valor do dólar nas vendas ou nos preços de produtos. Esta análise pode ser demonstrada de preferência com um gráfico de linha, onde o valor do dólar é a variável do eixo X.

![image](https://github.com/2023M8T4Inteli/grupo5/assets/99270135/7c003595-c04c-4e03-b8b6-8af7e86c2955)

## Dashboards específicos

Por fim, um dashboard relacionado a um UF em específico pôde ser construído. Em seus gráficos podem ser encontradas análises sobre a venda e sobre o preço de diferentes produtos no estado escolhido (que, neste caso, foi São Paulo).

A fim de possibilitar uma análise eficaz e uma coesão na geração de insights, os gráficos foram feitos com a filtragem de produtos de acordo com suas finalidades. Por exemplo, um cliente que trabalha vendendo bebidas iria se interessar por um gráfico sobre venda de cerveja e refrigerante, assim como um que trabalha com cachorro quente se interessaria por um onde os produtos que têm seus preços demonstrados são batata palha, ketchup e salsicha.

![image](https://github.com/2023M8T4Inteli/grupo5/assets/99270135/176125e8-4ea8-48b9-8098-9af43b7b36ec)

Existem diversas possibilidades de complementações que podem enriquecer estas análises. Por exemplo, uma análise para cada região de um UF seria útil, embora fosse necessária a criação de uma nova coluna na tabela que identificasse a região dentro do próprio estado.

Gráficos que fornecem análises mais gerais como “consumo por dia da semana” ou “contagem de alimentos por categoria” podem ser úteis, mas para a geração de insights os gráficos mais granulares são essenciais, motivo pelo qual estes foram maioria dentre todos apresentados nos dashboards.

![image](https://github.com/2023M8T4Inteli/grupo5/assets/99270135/2171f7cd-2e77-4ac6-ae67-e7c23186582d)

Atualizações ainda devem ser feitas e análises ainda devem ser geradas, porém o que foi gerado já permite que se considere feito ao menos um esboço do infográfico que o parceiro deseja receber.

A partir daqui, devem ser testadas novas colunas, novas estratégias de cruzamento de informações e diferentes formas de apresentação das mesmas. Os gráficos construídos fornecem, assim, uma base útil para prosseguir com estas tarefas.
