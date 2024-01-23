# Entendimento de Negócios

Este documento se refere ao artefato de Entendimento de Negócios desenvolvido pelo time M&C Solutions. Este artefato contém os três itens entregáveis para fins acadêmicos, sendo eles o: Canvas Proposta de Valor, a Matriz de Risco e Análise de Tamanho de Mercado (TAM, SAM, SOM).

## 1. **Proposta de Valor**

A proposta de valor no marketing destaca um negócio, posicionando-o com uma visão estratégica, e mais direcionada para seu público. Esse tipo de análise reforça a habilidade da empresa em entender as necessidades dos clientes, com uma visão mais focada nos mesmos. Sendo assim, para sua melhor visualização, podemos utilizar algumas ferramentas.

O Canvas Proposta de Valor é uma dessas ferramentas que é muito utilizada no mercado e alinha os produtos ou serviços de uma empresa com as necessidades dos clientes. Ele destaca o segmento de clientes, a proposta de valor exclusiva, os produtos oferecidos, as preocupações e benefícios dos clientes, e como a solução resolve esses problemas e proporciona ganhos. Com esta visão, e pensando no objetivo, nas necessidade do cliente e possíveis ganhos com o projeto, determinamos o Canvas para o projeto:

![image](https://github.com/2023M8T4Inteli/grupo5/assets/99270135/2e094164-7c64-42b9-9311-e871a3063486)

**Informações do Canvas Value Proposition:**

- **Value Proposition**
    - *Products & Services:*
        - Plataforma de análise de dados
        - Ferramenta de Business Intelligence para Go-to-Market
    - *Gain creators:*
        - Otimização de consultas
        - Arquitetura e pipeline de dados consolidados
        - Representação visual intuitiva
    - *Pain relievers:*
        - Análise precisa de detalhada
        - Visualização intuitiva com insights que auxiliem na tomada de decisão
- **Customer Segments**
    - *Customer jobs:*
        - Análise de mercado precisa
        - Tomada de decisões informadas
    - *Gains:*
        - Rapidez do processo de lançamento a mercado
        - Eficácia na análise
        - Insights e métricas para tomada de decisão
    - *Pains:*
        - Dificuldade em obter dados precisos e detalhados
        - Falta de insights e métricas em tempo real

## **2.Matriz de Risco**

A matriz de risco pode ser definida como uma ferramenta essencial utilizada para identificar e avaliar os possíveis riscos que podem impactar um projeto. Ela classifica os riscos em categorias com base na probabilidade de ocorrência e no impacto potencial, permitindo às equipes priorizá-los e criar estratégias de mitigação eficazes. Ao representar graficamente os riscos em uma matriz, a equipe pode tomar decisões mais bem fundamentadas sobre onde direcionar recursos e esforços, encontrando um equilíbrio entre os riscos e as oportunidades. Isso promove uma abordagem proativa para gerenciar incertezas e superar possíveis obstáculos. Segue abaixo matriz de risco desenvolvida pela equipe em visão dos possíveis riscos (juntamente com plano de ação) e oportunidades em relação ao projeto:

(![image](https://github.com/2023M8T4Inteli/grupo5/assets/99208930/2a630be8-16f6-4526-9fd2-6ffcfd8a6441)


### **2.1 Ameaças e Plano de Ação**

Segue descrição de todas as ameaças denotadas na Matriz de Risco e seus respectivos planos de ação:

**Ameaça 01:** Mau tratamento dos dados, causando ingestão de dados com baixa volumetria.

- **Plano de Ação:** Realizar uma avaliação da infraestrutura atual identificando pontos fracos e gargalos, definindo o que pode ser feito.
- **Responsável:** Eric
- **Justificativa:** O risco de mau tratamento dos dados, resultando em baixa volumetria, é crítico devido ao potencial comprometimento da qualidade das informações.
- **Risco:** 50%

**Ameaça 02:** Limitação em integrações multiclouds, e serviços pouco escaláveis em alguns lugares.

- **Plano de Ação:** Realizar uma avaliação da infraestrutura atual identificando pontos fracos e gargalos, definindo o que pode ser feito.
- **Responsável:** Eric
- **Justificativa:** Limitações em integrações multiclouds e serviços pouco escaláveis podem impactar a eficiência operacional e a capacidade de expansão do sistema.
- **Risco:** 90%

**Ameaça 03:** Alta expectativa do cliente e abstração do escopo do projeto.

- **Plano de Ação:** Assegurar a presença do cliente desde o início do projeto para alinhar as expectativas com a realidade
- **Responsável:** Michel
- **Justificativa:** À medida que o escopo do projeto se expande devido a expectativas não gerenciadas, os prazos estabelecidos inicialmente podem não ser cumpridos.
- **Risco:** 30%

**Ameaça 04:** Criação de infográficos que não auxiliam na tomada de decisão ao cliente

- **Plano de Ação:** Validação recorrente com o cliente, para o desenvolvimento de visualizações com métricas que realmente auxiliam na tomada de decisão.
- **Responsável:** Vinícius
- **Justificativa:** A criação de infográficos ineficazes não contribuem efetivamente para a tomada de decisões dos clientes, trazendo várias consequências negativas, como decisões tomadas de forma errada, e perda de confiança na utilização da ferramenta.
- **Risco:** 30%

**Ameaça 05:** Baixa granularidade e insights enviesados (sem embasamento do cliente) na análise estatística

- **Plano de Ação:** Pesquisa assertiva e testes constante para que não haja erro nos resultados da análise estatística
- **Responsável:** Michel
- **Justificativa:** Desacredita e invalida qualquer inferência feita a partir da análise, assim como a perda de personalização dos dados, e visualizações estatísticas
- **Risco:** 30%

**Ameaça 06:** Dados imprecisos, incompletos ou de baixa qualidade podem prejudicar a análise estatística.

- **Plano de Ação:** Realizar uma avaliação da infraestrutura atual identificando pontos fracos e gargalos, definindo o que pode ser feito.
- **Responsável:** Rodrigo Martins
- **Justificativa:** Dados de baixa qualidade podem levar a resultados estatísticos incorretos, prejudicando a tomada de decisões com base nas análises.
- **Risco:** 50%

**Ameaça 07:** O cliente pode não adotar ou usar efetivamente o infográfico gerado.

- **Plano de Ação:** Colaborar estreitamente com o cliente ao longo do projeto para entender suas necessidades e preferências.
- **Responsável:** Rodrigo Campos
- **Justificativa:** Os recursos investidos na criação do infográfico podem ser desperdiçados se ele não
- **Risco:** 50%

**Ameaça 08:** Vazamento de dados ou chave de acesso por parte dos grupos.

- **Plano de Ação:** Validar os "commits" (principalmente na main) e validar com o cliente se há necessidade de mascarar dados ou realizar anonimização.
- **Responsável:** Rodrigo Martins
- **Justificativa:** Quando dados ou chave de acesso são vazados, dá a oportunidade pros concorrentes ou Hackers invadirem o sistema e roubar todos os dados.
- **Risco:** 70%

**Ameaça 09:** Dependência de serviços terceiros, como fornecedores da nuvem

- **Plano de Ação:** Validar os "commits" (principalmente na main) e validar com o cliente se há necessidade de mascarar dados ou realizar anonimização.
- **Responsável:** Lucas
- **Justificativa:** A dependência de terceiros faz com que o sistema seja vulnerável, tenha falta de controle e inclua riscos financeiros.
- **Risco:** 70%

## **3. Análise de Tamanho de Mercado**

Com a intenção de entendimento do público alvo e impacto da solução aos clientes no longo prazo, podemos usar algumas estratégias para mensurar o tamanho do seu mercado, entre elas o TAM, SAM, SOM. Esse tipo de análise de mercado, representa diferentes subconjuntos de um mercado, na qual há uma previsão em relação a demanda sobre os produtos ou serviços, projetando sua performance, baseando-se em premissas de pesquisas segmentadas e com recortes pré-estabelecidos de forma estratégica.

Direcionando essa análise para a realidade do cliente, partimos do entendimento de que a solução proposta atende a um mercado específico (no caso, o de Business Inteligence), com projeção de curto, médio e longo prazo. Segue análise e tamanho de mercado em conforme pesquisa aprofundada:

![image-tam-sam-som](https://github.com/2023M8T4Inteli/grupo5/assets/99264567/bc341dca-734f-405c-b2a5-3e8594ba5580)

### **3.1 Definição TAM, SAM, SOM:**

### **3.1.1 TAM - Total Available Market ou “Mercado Total”**

Refere-se à procura integral do mercado por um produto ou serviço, sendo feito um recorte por segmento mais amplo, com uma visão estratégica ao cliente. Normalmente, calcula-se somando as receitas do mercado em análise. Com a visão analítica de com base na pesquisa de mercado direcionada ao segmento de Business Intelligence, obtivemos a receita aproximada de R$1,7 bilhão de reais.

### **3.1.2 SAM - Serviceable Available Market ou “Mercado Endereçável”**

Determina a projeção na qual uma organização pode alcançar algum segmento específico em um futuro próximo (em média, 5 anos), de acordo com seus recursos, com base em pesquisas de mercado no segmento de varejo alimentar e de serviço alimentar no Brasil (recorte geográfico). A receita aproximada neste quesito é de R$150 milhões de reais (recorte de 40% do mercado atual de Business Intelligence no Brasil).

### **3.1.3 SOM - Serviceable Obtainable Market ou “Mercado Acessível”**

Pode ser definida como a parte mais “nichada” da análise. Essa análise traz uma perspectiva mais realista sobre qual parcela do mercado na qual há possibilidade de conquistar, com base no momento atual do negócio. Esse indicador é utilizado para perspectivas de curto prazo (de 1 a 2 anos), por isso possui um recorte mais segmentado dentro da proposta da empresa. De acordo com o projeto, e a demanda apresentada, realizamos o recorte no segmento de distribuição alimentar, com base no estado de São Paulo, retirando a porcentagem de empresas que já utilizam Business Intelligence.

## Referências utilizadas:

*Transformações digitais no Brasil: insights sobre o nível de maturidade digital das empresas no país*. (1 C.E., January 1). McKinsey & Company. [https://www.mckinsey.com/br/our-insights/transformacoes-digitais-no-brasil](https://www.mckinsey.com/br/our-insights/transformacoes-digitais-no-brasil) 

Negócio, R. V. M. (2023, February 23). As perspectivas e tendências para o varejo alimentar em 2023. *Vivo Meu Negócio*. [https://vivomeunegocio.com.br/bares-e-restaurantes/gerenciar/varejo-alimentar/](https://vivomeunegocio.com.br/bares-e-restaurantes/gerenciar/varejo-alimentar/) 

Statista. (n.d.). *Business Intelligence Software - Brazil | Market forecast*. [https://www.statista.com/outlook/tmo/software/enterprise-software/business-intelligence-software/brazil](https://www.statista.com/outlook/tmo/software/enterprise-software/business-intelligence-software/brazil) 

*Alimentos* (n.d.). Investe SP. [https://www.investe.sp.gov.br/setores-de-negocios/alimentos/#:~:text=Cerca%20de%2028%2C6%25%20da,e%20Estat%C3%ADstica%20(IBGE)%20%E2%80%93%20](https://www.investe.sp.gov.br/setores-de-negocios/alimentos/#:~:text=Cerca%20de%2028%2C6%25%20da,e%20Estat%C3%ADstica%20(IBGE)%20%E2%80%93%20) 

*Value Proposition Canvas: o que é e como funciona essa metodologia? - G4 Educacão*. (n.d.). [https://g4educacao.com/portal/value-proposition-canvas](https://g4educacao.com/portal/value-proposition-canvas)
