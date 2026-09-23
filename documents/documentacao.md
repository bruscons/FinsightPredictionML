# Documentação Modelo Preditivo - Inteli

```
INSTRUÇÕES GERAIS (remova este trecho ao final)

Você deve editar este documento utilizando notação markdown - siga as convenções neste link 
https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax
```

## FinSight
### Bill Hunters 
#### Bruno Martins, Bruno Paiva, Carlos Icaro, Danilo de Castro, Enzo Araujo, Matheus Henrique, Victor Garcia 

## Sumário
[1. Introdução](#c1)

[2. Objetivos e Justificativa](#c2)

[3. Metodologia](#c3)

[4. Desenvolvimento e Resultados](#c4)

[5. Conclusões e Recomendações](#c5)

[6. Referências](#c6)

[Anexos](#attachments)


## <a name="c1"></a>1. Introdução

&nbsp;&nbsp;&nbsp;&nbsp;Este documento constitui a análise formal de negócios e a especificação técnica do projeto desenvolvido pelos estudantes pertencentes ao grupo Bill Hunters do Instituto de Liderança e Tecnologia (INTELI), no âmbito do Módulo 3, intitulado "Lógica para Predição com Inteligência Artificial". O propósito fundamental desta documentação é detalhar o contexto, o problema de negócio, a solução proposta e o plano de implementação de um modelo preditivo concebido para otimizar a gestão de recebíveis e mitigar os riscos de inadimplência para a empresa parceira, Finnet.

&nbsp;&nbsp;&nbsp;&nbsp;A estrutura foi concebida para atender a uma audiência diversa, englobando tanto os avaliadores acadêmicos, que analisarão o rigor metodológico e a profundidade analítica, quanto os stakeholders corporativos da Finnet, que avaliarão a relevância e a viabilidade comercial da solução. Esta primeira seção dedica-se a estabelecer o alicerce conceitual do projeto, explorando o cenário de mercado, o posicionamento do parceiro de negócio e a magnitude do problema a ser resolvido. Desta forma, estabelece-se o "porquê" fundamental que justifica a iniciativa, antes que as seções subsequentes se aprofundem no "como", detalhando a análise de dados, o desenvolvimento do modelo de aprendizado de máquina e a arquitetura da solução final.

### 1.1. O Parceiro: Finnet

&nbsp;&nbsp;&nbsp;&nbsp;Fundada em 2003, a Finnet é uma infraestrutura consolidada no ecossistema de pagamentos B2B do Brasil. A empresa se destaca pelo volume massivo de operações, processando anualmente mais de R$ 2,1 trilhões em transações e conectando mais de 3,2 milhões de CNPJs. Seu posicionamento é fortalecido pela participação pioneira no Open Finance Brasil, sendo a única empresa de conectividade a integrar a iniciativa junto ao Banco Central (BACEN), informações presentes no próprio site da empresa. Em um mercado competitivo, onde o Brasil lidera o setor de fintechs na América Latina com 1.706 empresas ativas em 2025, essa vanguarda é um diferencial de acordo com a pesquisa acadêmica (Porto et al., 2024). A capacidade de extrair inteligência de dados por meio de Inteligência Artificial é a nova fronteira competitiva do setor. Portanto, o desenvolvimento de um modelo preditivo não é apenas um incremento ao portfólio da Finnet, mas uma necessidade para sustentar sua liderança.

### 1.2. Portfólio de Soluções

&nbsp;&nbsp;&nbsp;&nbsp;Com sede em São Paulo, a Finnet oferece uma suíte integrada de soluções financeiras. Seu portfólio se baseia em quatro pilares principais:

**•	Gestão Financeira:** Através do Bank Manager, automatiza contas a pagar e a receber em um ambiente multibanco.

**•	Soluções de Cobrança:** Foca na redução da inadimplência com uma plataforma online para gestão de boletos.

**•	Conectividade Financeira:** Centraliza os processos financeiros, unificando a comunicação entre a empresa e seus bancos.

**•	Crédito:** Oferece gestão da cadeia de suprimentos e antecipação de recebíveis por meio do Painel Fornecedor.

&nbsp;&nbsp;&nbsp;&nbsp;Este projeto se insere diretamente no pilar de "Soluções de Cobrança" com foco no trabalho com a plataforma “Luna”, agregando uma camada de inteligência preditiva para antecipar, e não apenas remediar, a inadimplência.

### 1.3. O Problema de Negócio: O Custo da Inadimplência B2B

&nbsp;&nbsp;&nbsp;&nbsp; Antes de iniciar a criação da solução, é fundamental compreender de forma plena o contexto e as motivações que sustentam o projeto, garantindo que seu desenvolvimento esteja totalmente alinhado às necessidades do parceiro, Finnet. Para isso, tornou-se necessário um entendimento objetivo e aprofundado do cenário da inadimplência corporativa no mercado brasileiro.

&nbsp;&nbsp;&nbsp;&nbsp;A inadimplência corporativa no Brasil é um fenômeno macroeconômico crônico. Em 2024, o país encerrou o ano com 6,9 milhões de empresas inadimplentes (31,6% do total), somando R$ 150,6 bilhões em dívidas. Os setores de Serviços (55,3%) e Comércio (35,4%) são os mais afetados. Esse cenário impacta diretamente o custo do crédito, sendo o risco de inadimplência responsável por cerca de 32% da composição do spread bancário nacional.

&nbsp;&nbsp;&nbsp;&nbsp;A inadimplência corporativa no Brasil é um fenômeno macroeconômico crônico. Dados da Serasa Experian apontam que, em 2024, o país encerrou o ano com 6,9 milhões de empresas inadimplentes (31,6% do total), somando R$ 150,6 bilhões em dívidas. Os setores de Serviços (55,3%) e Comércio (35,4%) são os mais afetados. Esse cenário impacta diretamente o custo do crédito, sendo o risco de inadimplência responsável por cerca de 32% da composição do spread bancário nacional, segundo a Federação Brasileira de Bancos (FEBRABAN, 2021).

#### 1.3.1 O Paradoxo do Boleto Bancário

&nbsp;&nbsp;&nbsp;&nbsp;Apesar da ascensão do Pix, o boleto bancário mantém sua hegemonia em operações B2B de alto valor. De acordo com a Agência Brasil, em 2023, boletos movimentaram R$ 5,7 trilhões. Já no primeiro semestre de 2024, o valor alcançou R$ 6,67 trilhões de acordo com o portal de notícias do mundo dos negócios Infomoney. Essa relevância financeira torna a inadimplência associada a boletos um problema de alto impacto, pois o não pagamento de um único título pode gerar um disruptivo efeito cascata.

#### 1.3.2 A Necessidade de uma Abordagem Proativa

&nbsp;&nbsp;&nbsp;&nbsp;A gestão de recebíveis tradicional é reativa, iniciando a cobrança somente após o vencimento do título. Essa abordagem é frequentemente ineficiente e não consegue acompanhar a complexidade do endividamento atual. A introdução de um modelo preditivo permite uma mudança de paradigma: da gestão reativa para a gestão de risco proativa. A pergunta do gestor deixa de ser "Como cobrar este cliente em atraso?" e passa a ser "Qual a probabilidade de este cliente atrasar e que ações posso tomar agora para mitigar o risco?". Essa capacidade de antecipação permite estratégias personalizadas, como a oferta de descontos para pagamento antecipado ou a renegociação de prazos antes do vencimento, preservando o relacionamento comercial.

#### 1.3.3 Governança e Conformidade Regulatória

&nbsp;&nbsp;&nbsp;&nbsp;A solução será desenvolvida sobre um pilar inegociável de governança de dados e conformidade com a legislação. O projeto lidará com dados sensíveis de pagadores, o que o coloca sob a jurisdição da Lei Geral de Proteção de Dados (LGPD - Lei nº 13.709/2018) e da Lei de Sigilo Bancário (Lei Complementar nº 105/2001). O desafio, portanto, não é apenas técnico, mas sim integrar a predição de inadimplência a um framework ético e seguro, que garanta a confiança do parceiro e a integridade da solução.

### 1.4. Conclusão

&nbsp;&nbsp;&nbsp;&nbsp;Portanto, a presente introdução estabelece o alicerce fundamental do projeto ao articular a confluência entre a posição de liderança da Finnet no ecossistema de pagamentos e a magnitude da inadimplência B2B no cenário macroeconômico brasileiro. Foi demonstrado que a persistente relevância do boleto bancário em operações de alto valor torna o impacto de cada evento de não pagamento particularmente severo, evidenciando que o paradigma reativo de cobrança, adotado tradicionalmente, se mostra insuficiente e oneroso.

&nbsp;&nbsp;&nbsp;&nbsp;Neste contexto, a concepção de um modelo preditivo de inadimplência é apresentada não como somente um incremento tecnológico, mas como um imperativo. A transição para uma gestão de risco proativa é justificada como o mecanismo essencial para mitigar perdas financeiras, otimizar a alocação de recursos de cobrança e preservar o capital de relacionamento com os clientes por meio de intervenções antecipadas. Foi sublinhado, ainda, que a inovação proposta será desenvolvida sobre o pilar inegociável da governança de dados, em estrita conformidade com a Lei Geral de Proteção de Dados (LGPD) e a Lei de Sigilo Bancário.

&nbsp;&nbsp;&nbsp;&nbsp;Desta forma, a relevância do problema e a viabilidade da solução foram solidamente fundamentadas, justificando a iniciativa e estabelecendo a base para as seções subsequentes, que se aprofundarão na análise técnica, no desenvolvimento do modelo e na arquitetura da solução a ser implementada.

## <a name="c2"></a>2. Objetivos e Justificativa

&nbsp;&nbsp;&nbsp;&nbsp;A seção de Objetivos e Justificativa tem como propósito apresentar de forma estruturada as principais problemáticas levantadas pelo parceiro de negócios e demonstrar como o grupo direcionou seus esforços para solucioná-las.


### 2.1 Objetivos

&nbsp;&nbsp;&nbsp;&nbsp;O objetivo geral deste projeto é aprimorar a eficiência da plataforma de Soluções de Cobrança da Finnet, reduzindo a inadimplência e otimizando a gestão de recebíveis de seus clientes corporativos. Especificamente, busca-se desenvolver mecanismos que permitam disponibilizar métricas individualizadas — como o score de risco de inadimplência por CNPJ ou CPF —, projetar fluxos de recebimento que contribuam para o planejamento de caixa e antecipar a identificação de boletos com maior probabilidade de atraso ou inadimplência. 

&nbsp;&nbsp;&nbsp;&nbsp;Além disso, o modelo visa recomendar prazos de vencimento mais adequados, de modo a aumentar a taxa de pagamentos em dia e apoiar a tomada de decisão em estratégias de cobrança preventiva e personalizada. Dessa forma, a Finnet busca consolidar uma abordagem preditiva e orientada por dados, promovendo a eficiência operacional e o fortalecimento das relações comerciais entre empresas.


### 2.2 Proposta de Solução

&nbsp;&nbsp;&nbsp;&nbsp;A proposta apresentada consiste no desenvolvimento de um modelo preditivo de inadimplência capaz de analisar, de forma integrada, o histórico de pagamentos, as características financeiras e os dados cadastrais dos clientes corporativos. A partir dessa análise, o sistema será capaz de estimar a probabilidade de atraso, classificar o comportamento de pagamento em categorias como “em dia”, “em atraso” ou “em inadimplência”, além de projetar os valores previstos de recebimento dentro de determinado período e calcular um score individual de risco por CNPJ ou CPF.

&nbsp;&nbsp;&nbsp;&nbsp;Com essa abordagem, a Finnet busca evoluir de um modelo reativo — em que a ação ocorre apenas após o não pagamento — para uma gestão proativa de risco, baseada em dados e inteligência analítica. Essa mudança permitirá que a empresa identifique antecipadamente possíveis inadimplentes e adote medidas preventivas, como a renegociação de prazos, o incentivo ao pagamento antecipado e a segmentação de estratégias de cobrança conforme o perfil de risco identificado. Assim, o modelo proposto não apenas melhora o desempenho operacional das soluções de cobrança, mas também agrega valor estratégico ao posicionamento da Finnet no mercado.

### 2.3 Justificativa

&nbsp;&nbsp;&nbsp;&nbsp;A implementação de um modelo preditivo de inadimplência se justifica pela crescente relevância desse fenômeno no cenário macroeconômico brasileiro, especialmente no contexto B2B, onde a inadimplência impacta diretamente o custo de crédito, o fluxo de caixa e a sustentabilidade financeira das empresas. As abordagens tradicionais de gestão de recebíveis, baseadas em ações corretivas após o atraso, têm se mostrado limitadas diante da complexidade e do volume de transações corporativas. Nesse sentido, a proposta introduz uma camada de inteligência analítica que permite a antecipação de riscos e a definição de estratégias mais assertivas de cobrança e relacionamento.

&nbsp;&nbsp;&nbsp;&nbsp;Entre os principais benefícios esperados estão a redução de perdas financeiras, ao permitir a identificação precoce de possíveis inadimplências; a otimização da alocação de recursos de cobrança, priorizando clientes de maior risco; e o fortalecimento do relacionamento comercial, que passa a ser conduzido de forma preventiva e colaborativa, e não apenas punitiva. Além disso, a solução representa um avanço significativo em inovação competitiva, consolidando a Finnet como referência em soluções de cobrança preditiva no mercado B2B. Dessa forma, o projeto não se limita a aprimorar a eficiência operacional, mas reposiciona estrategicamente a empresa na vanguarda tecnológica, integrando inteligência artificial, governança de dados e compliance regulatório em um framework robusto, escalável e sustentável.


## <a name="c3"></a>3. Metodologia

A execução de projetos de ciência de dados, especialmente no setor financeiro, demanda a aplicação de uma metodologia que não seja somente focada na execução técnica, mas que sirva também como um pilar fundamental para garantir que os resultados analíticos se traduzam em valor de negócio tangível e mensurável. A ausência de um processo formal e padronizado pode transformar iniciativas de alto potencial em empreendimentos de risco elevado, cujos resultados se tornam excessivamente dependentes da experiência própria dos executores, dificultando a replicabilidade, a escalabilidade e a gestão do conhecimento organizacional, assim, como presente na bibliografia (Wirth e Hipp, 2000). Para o desenvolvimento de uma solução preditiva de inadimplência para a Finnet, um projeto que visa apoiar decisões financeiras, a escolha de um framework muito bem estruturado é imperativo. Nesse contexto, foi adotado o Cross-Industry Standard Process for Data Mining (CRISP-DM) como a metodologia deste projeto.

A seleção do CRISP-DM é fundamentada em sua comprovada eficácia e ampla aceitação como um padrão utilizado na indústria para projetos de mineração de dados e ciência de dados (Shearer, 2000). Sua natureza agnóstica em relação a ferramentas e domínios de aplicação, aliada a uma estrutura cíclica e iterativa, oferece a flexibilidade necessária para a construção de um projeto ligado a complexidade inerente à predição de comportamento de pagamento. A metodologia fornece uma linha de desenvolvimento, segmentando o ciclo de vida do projeto em seis fases distintas e interconectadas, que guiam a equipe desde a formulação do problema de negócio até a implantação e o monitoramento contínuo da solução. A seguir, será apresentado o referencial teórico que fundamenta cada uma dessas fases, enunciando suas tarefas e objetivos no contexto do desafio proposto pela Finnet.

### 3.1 Fundamentos e Estrutura da Metodologia CRISP-DM

Concebido no final da década de 1990 por um consórcio de pioneiros da indústria, incluindo DaimlerChrysler, SPSS Inc. e NCR Corporation, o CRISP-DM surgiu da necessidade premente de padronizar a execução de projetos de mineração de dados, que até então eram conduzidos de forma amplamente desestruturada (Chapman et al., 2000). A falta de um processo padrão tornava os projetos mais arriscados, de difícil gerenciamento e com resultados imprevisíveis, um cenário insustentável para aplicações de missão crítica, como as do setor financeiro. O objetivo do consórcio era criar um modelo de processo que fosse neutro em relação à indústria e à tecnologia, permitindo sua aplicação universal e fomentando uma linguagem comum entre profissionais da área como escrito por Wirth e Hipp. Essa filosofia de ser um padrão aberto e não proprietário foi um dos principais catalisadores para sua ampla adoção.

A estrutura do CRISP-DM é caracterizada por sua organização hierárquica e sua natureza cíclica, aspectos que a tornam particularmente adequada para o projeto da Finnet. Hierarquicamente, a metodologia se desdobra em quatro níveis de abstração: Fases, que representam as seis etapas principais do ciclo de vida; Tarefas Genéricas, que descrevem os objetivos a serem alcançados em cada fase; Tarefas Especializadas, que detalham como as tarefas genéricas podem ser executadas em contextos específicos (como o de análise de crédito); e a Instância de Processo, que é o registro concreto das ações e decisões de um projeto particular. Essa estrutura permite que o CRISP-DM sirva tanto como um guia de alto nível quanto como um manual de execução. A natureza cíclica, simbolizada pelo círculo externo em seu diagrama de processo, reflete a realidade da ciência de dados: o conhecimento adquirido ao final de um projeto frequentemente revela novas questões de negócio, iniciando um novo ciclo de descoberta e aprimoramento. Essa capacidade de iteração e aprendizado contínuo é vital para o problema de predição de inadimplência, que é dinâmico e influenciado por fatores macroeconômicos e comportamentais em constante mudança.

### 3.2 A Fase de Compreensão do Negócio (Business Understanding)

A fase de Compreensão do Negócio é o ponto de partida e a etapa mais importante do ciclo de vida do CRISP-DM. Seu objetivo primordial é focar nos objetivos e requisitos do projeto sob uma perspectiva estritamente de negócio, para então converter esse conhecimento em uma definição formal do problema de mineração de dados e em um plano preliminar para alcançá-lo (Chapman et al., 2000). Nesse cenário, negligenciar esta fase é um erro comum que pode levar ao desenvolvimento de modelos tecnicamente precisos, mas que falham em gerar valor de negócio real. Por isso, é importante discorrer sobre quatro tarefas principais dessa fase, para que elas sejam conhecidas e bem aplicadas pela equipe de desenvolvimento.

A primeira tarefa é Determinar os Objetivos de Negócio. Nela, é fundamental compreender em profundidade o que o cliente ou a organização deseja realizar. Isso envolve identificar o problema de negócio central, como a necessidade de reduzir a inadimplência ou otimizar a gestão de cobranças, e detalhar os fatores que o influenciam. Além disso, é nesta tarefa que se definem os critérios de sucesso do projeto do ponto de vista do negócio, ou seja, quais resultados quantitativos ou qualitativos indicarão que o projeto foi bem-sucedido.

A segunda tarefa é Avaliar a Situação, o que consiste em realizar um inventário completo dos recursos disponíveis, incluindo pessoal (com suas respectivas habilidades), dados, infraestrutura computacional e conhecimento de domínio. Ademais, são identificados os requisitos do projeto, as premissas e as restrições. Posteriormente, uma análise de riscos e contingências é realizada para antecipar possíveis obstáculos. Finalmente, uma análise de custo-benefício é conduzida para avaliar a viabilidade do projeto, comparando os custos de sua execução com os benefícios esperados para o negócio.

Com base nas informações coletadas nas tarefas anteriores, a terceira tarefa é Determinar as Metas de Mineração de Dados. Este é o ponto de transição entre o problema de negócio e a solução técnica. Assim, os objetivos de negócio são traduzidos em metas técnicas específicas e mensuráveis. Por exemplo, o objetivo de negócio de "melhorar a eficiência da cobrança" pode ser traduzido na meta de "desenvolver um modelo preditivo que classifique os pagadores em categorias de risco de inadimplência com uma precisão mínima de 95%". Aqui, também são definidos os critérios de sucesso técnico, que servirão para avaliar a qualidade dos modelos que serão gerados.

Por fim, a fase se encerra com a tarefa de Produzir o Plano do Projeto. Este documento detalha o plano de ação para atingir tanto as metas de mineração de dados quanto os objetivos de negócio. O plano descreve as etapas a serem executadas ao longo de todo o projeto, os recursos necessários para cada fase, os cronogramas, as entregas e uma avaliação inicial das ferramentas e técnicas que serão empregadas nas fases subsequentes como presente no referencial teórico (Chapman et al., 2000).

### 3.3 A Fase de Compreensão dos Dados (Data Understanding):

Após a definição clara dos objetivos de negócio e do plano do projeto, a fase de Compreensão dos Dados inicia as atividades de análise exploratória. O objetivo principal desta fase é obter uma familiaridade inicial com os dados, identificar potenciais problemas de qualidade, descobrir primeiros insights e identificar subconjuntos de dados que pareçam promissores para a modelagem como escrito por Chapman. Esta fase é fundamental para evitar surpresas em etapas posteriores e para garantir que a base de dados disponível seja adequada para responder às questões de negócio formuladas. Assim, esta fase é composta por quatro tarefas.

A primeira tarefa é Coletar os Dados Iniciais, que consiste em adquirir os dados brutos listados como recursos no plano de projeto. Esta coleta pode envolver a extração de dados de um ou mais bancos de dados, arquivos planos ou outras fontes. Nesse sentido, se necessário, os dados são carregados em uma ferramenta de análise para as próximas etapas. Assim, o resultado desta tarefa é um relatório de coleta inicial de dados, que documenta as fontes e os métodos de aquisição.
A segunda tarefa é Descrever os Dados. Nela, as propriedades superficiais do conjunto de dados são examinadas e documentadas. Isso inclui a verificação do formato dos dados, o número de registros (linhas) e atributos (colunas), as identidades e os tipos de cada campo. O objetivo é obter uma visão geral quantitativa dos dados disponíveis, o que é formalizado em um relatório de descrição de dados.

A terceira tarefa, Explorar os Dados, aprofunda a análise iniciada na tarefa anterior. Utilizando técnicas de estatística descritiva e visualização de dados, a equipe investiga os dados de forma mais detalhada para responder às questões de mineração de dados formuladas na fase anterior. São realizadas análises de correlação, distribuição de variáveis e identificação de padrões iniciais. Esta exploração ajuda a formar e a refinar hipóteses sobre os dados, e seus resultados são consolidados em um relatório de exploração de dados.

A fase conclui com a tarefa de Verificar a Qualidade dos Dados. Aqui, os dados são examinados minuciosamente em busca de problemas que possam comprometer a qualidade da modelagem, como valores ausentes (missing values), dados incorretos ou inconsistentes, ruídos e valores atípicos (outliers). Cada problema identificado é documentado em um relatório de qualidade de dados, que servirá como insumo essencial para a próxima fase do processo.

### 3.4 A Fase de Preparação dos Dados (Data Preparation)

A fase de Preparação dos Dados é frequentemente a mais longa e trabalhosa de um projeto de mineração de dados, consumindo uma parcela significativa do tempo total do ciclo do projeto. Nesse cenário, seu objetivo é realizar todas as atividades necessárias para construir o conjunto de dados final que será utilizado como entrada para as ferramentas de modelagem (Shearer, 2000). As tarefas desta fase são executadas de forma iterativa e não seguem uma ordem específica. A qualidade do modelo final é diretamente dependente da qualidade do trabalho realizado nesta etapa. As cinco tarefas principais desta fase são descritas a seguir.

A primeira tarefa é Selecionar os Dados, na qual se decide quais dados serão efetivamente utilizados na análise. Com base nos objetivos de mineração, na qualidade dos dados e em restrições técnicas (como volume de dados ou tempo de processamento), são selecionados os registros e atributos mais relevantes. A justificativa para a inclusão ou exclusão de cada parte dos dados é documentada para garantir a rastreabilidade das decisões.

A segunda tarefa é Limpar os Dados. Com base no relatório de qualidade de dados da fase anterior, são aplicadas técnicas para tratar os problemas identificados. Isso pode incluir a imputação de valores ausentes utilizando métodos estatísticos (como média ou mediana), a correção de dados inconsistentes ou a remoção de registros ou atributos com baixa qualidade. O objetivo é elevar a qualidade dos dados ao nível exigido pelas técnicas de modelagem que serão aplicadas.

A terceira tarefa que é Construir Dados, envolve a criação de novos atributos a partir dos já existentes, um processo também conhecido como engenharia de características (feature engineering). Atributos derivados podem capturar informações mais relevantes para o problema de negócio e melhorar significativamente o desempenho dos modelos. Por exemplo, a partir de datas de vencimento e pagamento, pode-se construir um atributo que represente o número de dias em atraso.

A quarta tarefa é Integrar os Dados. Em muitos projetos, os dados necessários estão distribuídos em múltiplas fontes, como tabelas, arquivos ou sistemas diferentes. Esta tarefa consiste em combinar essas fontes para criar um conjunto de dados unificado e coeso. A integração pode envolver a fusão de tabelas com base em chaves comuns ou a agregação de dados em diferentes níveis de granularidade.

Finalmente, a tarefa de Formatar os Dados realiza as transformações sintáticas necessárias para que os dados se adequem aos requisitos específicos da ferramenta de modelagem a ser utilizada. Isso pode incluir a conversão de tipos de dados, a reordenação de colunas ou a aplicação de transformações para normalizar ou padronizar valores numéricos. O resultado desta fase é um conjunto de dados limpo, integrado e formatado, pronto para a modelagem.

### 3.5 A Fase de Modelagem (Modeling)

Na fase de Modelagem, diversas técnicas de aprendizado de máquina são selecionadas e aplicadas, e seus parâmetros são calibrados para valores ótimos. O objetivo é construir modelos preditivos ou descritivos que capturem os padrões identificados nos dados e que atendam às metas de mineração de dados definidas anteriormente. Geralmente, algumas técnicas são aplicadas ao mesmo problema, e seus resultados são comparados na fase seguinte.

A primeira tarefa é Selecionar a Técnica de Modelagem. Nesta etapa, a equipe de projeto escolhe os algoritmos de modelagem que serão utilizados. A escolha depende do tipo de problema de mineração de dados (classificação, regressão, clusterização, etc.) e das características do conjunto de dados. É importante também documentar as premissas de cada técnica, como, por exemplo, a suposição de linearidade em um modelo de regressão linear.

A segunda tarefa é Gerar o Desenho de Teste. Antes de construir o modelo, é crucial definir um procedimento muito bem estruturado para testar sua qualidade e validade. Uma prática comum é dividir o conjunto de dados em subconjuntos de treino e teste. O modelo é construído utilizando apenas o conjunto de treino, e sua performance é avaliada no conjunto de teste, que contém dados que o modelo nunca viu antes. Essa abordagem garante uma estimativa imparcial da capacidade de generalização do modelo para novos dados.

A terceira tarefa é a Construção do Modelo. Nela, a ferramenta de modelagem é executada sobre o conjunto de dados de treino para gerar um ou mais modelos. Esta tarefa pode ser altamente iterativa, envolvendo a calibração de múltiplos hiperparâmetros do algoritmo para encontrar a combinação que produz o melhor desempenho. As configurações de parâmetros utilizadas para cada modelo gerado são cuidadosamente documentadas.

A última tarefa desta fase é a Avaliação do Modelo (Assess Model). É importante notar que esta avaliação é de natureza predominantemente técnica e difere da avaliação de negócio que ocorrerá na fase seguinte. Aqui, os modelos são avaliados com base nos critérios de sucesso técnico definidos anteriormente. O desenvolvedor interpreta os modelos, verifica sua consistência com o conhecimento de domínio e julga seu desempenho com base em métricas técnicas, como acurácia, precisão, recall ou erro quadrático médio. Esta avaliação técnica permite classificar os modelos gerados e selecionar os mais promissores para a próxima fase.

### 3.6 A Fase de Avaliação (Evaluation)

Antes de proceder para a implantação final de um modelo, é fundamental avaliá-lo de maneira aprofundada e revisar rigorosamente os passos executados para sua construção. A fase de Avaliação é o momento em que os resultados do projeto são analisados sob a ótica dos critérios de sucesso de negócio definidos na primeira fase. O objetivo principal é determinar se os modelos desenvolvidos atendem a esses critérios e se o projeto como um todo resolve o problema de negócio que o originou como presente na blibiografia (Chapman et al., 2000). Esta fase representa uma ponte muito importante entre a validação técnica e a validação estratégica, garantindo que o resultado final seja não apenas um artefato estatisticamente ótimo, mas um ativo de valor para a organização.

A primeira tarefa é Avaliar os Resultados. Nela, os modelos mais promissores da fase anterior são submetidos a uma avaliação que supera as métricas técnicas. A equipe de projeto, em conjunto com os stakeholders do negócio, analisa se os resultados do modelo são compreensíveis, úteis e se podem ser implementados de forma prática na operação da empresa. É verificado se os modelos atingem os critérios de sucesso de negócio e se o retorno sobre o investimento justifica a implantação (em casos reais de mercado e não para fins educacionais.

A segunda tarefa é Revisar o Processo. Esta é uma revisão abrangente de todo o projeto de mineração de dados, desde a compreensão do negócio até a modelagem. O objetivo é garantir que todas as etapas foram executadas corretamente e que nenhum fator importante foi negligenciado. Esta revisão ajuda a identificar possíveis falhas no processo e a consolidar o aprendizado que pode ser aplicado em projetos futuros.

Com base nas duas tarefas anteriores, a terceira e última tarefa é Determinar os Próximos Passos. A equipe decide sobre o que irá ser tomado como decisão para o desfecho do projeto. As opções incluem: proceder para a implantação do(s) modelo(s) aprovado(s); realizar mais iterações, retornando a fases anteriores (como preparação de dados ou modelagem) para refinar os modelos; ou iniciar novos projetos, caso os resultados tenham revelado novas oportunidades ou questões de negócio. A decisão final é documentada, justificando a escolha e delineando as próximas ações.

### 3.7 A Fase de Implantação (Deployment)

A criação de um modelo, por si só, não gera valor; o valor é criado quando o conhecimento adquirido é utilizado para aprimorar a tomada de decisão. A fase de Implantação, ou Deployment, abrange todas as atividades necessárias para colocar o modelo em produção e garantir que seus resultados sejam integrados aos processos de negócio da organização. A complexidade desta fase pode variar bastante, desde a geração de um relatório final até a implementação de um processo de mineração de dados automatizado e contínuo.

A primeira tarefa é Planejar a Implantação. Nela, é desenvolvido um plano detalhado que descreve como o modelo será integrado aos sistemas e processos operacionais existentes. O plano define os passos necessários, os recursos envolvidos e o cronograma para a implantação.

A segunda tarefa é Planejar o Monitoramento e a Manutenção. Um modelo de aprendizado de máquina não é um artefato estático; seu desempenho pode degradar ao longo do tempo à medida que as características dos dados de entrada mudam (um fenômeno conhecido como model drift). Portanto, é essencial criar um plano para monitorar continuamente a performance do modelo em produção e para realizar sua manutenção, o que pode incluir o retreinamento periódico com novos dados.

A terceira tarefa é a Produção do Relatório Final. Dependendo do público, este pode ser um relatório executivo resumido, destacando os principais resultados e o impacto no negócio, ou um relatório técnico detalhado, documentando todo o processo, desde a coleta de dados até a avaliação do modelo. Este documento é um entregável fulcral do projeto.

Finalmente, a última tarefa do ciclo CRISP-DM é Revisar o Projeto. Trata-se de uma retrospectiva final do projeto, documentando as lições aprendidas, o que funcionou bem e o que poderia ser melhorado. Esta tarefa é fundamental para a gestão do conhecimento, permitindo que a organização e a equipe capitalizem a experiência adquirida e aprimore a execução de futuros projetos de ciência de dados e modelagem preditiva.

### Conclusão

A adoção do CRISP-DM como metodologia para o desenvolvimento do projeto de predição de inadimplência da Finnet mostra-se não apenas uma escolha técnica, mas uma decisão que alinha ciência de dados e geração de valor de negócio. Ao longo de suas fases — desde a compreensão do problema e dos objetivos de negócio, passando pela análise e preparação dos dados, até a modelagem, avaliação e implantação — o framework garante que o processo seja conduzido de maneira muito bem estruturada, iterativa e orientada a resultados que geram valor para o cliente. Essa abordagem minimiza riscos, aumenta a confiabilidade das soluções geradas e fortalece a capacidade da organização em transformar dados em valor.

Além disso, a natureza cíclica do CRISP-DM assegura que o aprendizado obtido em cada etapa seja continuamente incorporado ao processo, permitindo ajustes e refinamentos constantes diante da complexidade e da dinamicidade do setor financeiro. No caso da Finnet, cujo desafio está diretamente relacionado à antecipação do comportamento de pagamento, essa característica é essencial para manter a relevância e a eficácia do modelo frente às mudanças econômicas e comportamentais do mercado.

Assim, a metodologia não apenas guia o projeto do ponto de vista técnico, mas também estabelece uma ponte entre ciência de dados e tomada de decisão, possibilitando que os resultados obtidos sejam traduzidos em insights de negócio tangíveis e mensuráveis. Dessa forma, o CRISP-DM consolida-se como um pilar para a construção de soluções preditivas, escaláveis e sustentáveis, alinhadas aos objetivos organizacionais da Finnet.  

## <a name="c4"></a>4. Desenvolvimento e Resultados
### 4.1. Compreensão do Problema

#### 4.1.1. Contexto da indústria 

##### **Modelo de Negócios da Empresa Parceira Finnet:**

&nbsp;&nbsp;&nbsp;&nbsp;Abordar a compreensão do problema é essencial para que a solução proposta esteja alinhada à realidade de mercado, aos desafios do setor e às particularidades da empresa parceira. No caso da Finnet, isso significa entender como o seu modelo de negócios, o cenário competitivo e as tendências tecnológicas moldam suas oportunidades e ameaças. Esse diagnóstico inicial não apenas orienta o direcionamento estratégico do projeto, mas também evita desvios durante o desenvolvimento, permitindo que as funcionalidades, integrações e recursos da solução atendam de forma efetiva às demandas identificadas. Ao analisar o contexto da indústria e as forças competitivas, é possível antecipar obstáculos, identificar vantagens competitivas e garantir que o produto final seja relevante, escalável e capaz de gerar valor sustentável.

&nbsp;&nbsp;&nbsp;&nbsp;A Finnet opera majoritariamente com um modelo de negócios B2B (Business-to-Business). A empresa oferece uma plataforma de tecnologia como serviço (SaaS) com o intuito de automatizar e otimizar a gestão de processos financeiros de empresas grandes e médias. Ela funciona como um hub de conectividade, integrando um sistema de gestão de seus clientes a muitos bancos e instituições financeiras. A monetização flui através de assinaturas e de taxas sobre transações concluídas e seus volumes. A Finnet transmuta seu valor através da centralização de informações, automação de tarefas manuais e eficiência operacional da sua operação financeira.

&nbsp;&nbsp;&nbsp;&nbsp;A concorrência da Finnet é considerada multifacetada dentro do mercado de tecnologia financeira B2B. Cada player foca em um nicho específico, porém todos acabam sendo concorrentes. A Star Bank, por exemplo, oferece serviços através de APIs muito bem desenvolvidas que acabam sendo mais atrativas para clientes procurando a automação profunda de rotinas financeiras. Do outro lado, a iugu se especializa no mercado por conta da sua solução de automação para o mercado de recorrência e marketplace, onde compete com ferramentas poderosas de cobranças online. A Accesstage é considerada um concorrente direto da Finnet, se consolidando como um dos maiores hubs de integração de dados do Brasil. A empresa tenta buscar o mesmo perfil de clientes da Finnet, entregando soluções para a automação de contas a pagar e receber.

&nbsp;&nbsp;&nbsp;&nbsp;O setor de tecnologia financeira está passando por uma evolução extremamente rápida. Dentro desse avanço, passamos por três pilares muito importantes. Primeiramente, algo que está sendo enfatizado ao longo dessa evolução é a Hiper-Automação de processos. Isso ocorre porque o setor de finanças tenta otimizar o fluxo de tarefas de ponta a ponta, sem intervenções e falhas humanas. Após isso, o uso de Inteligência Artificial e análise preditiva vem se intensificando com o intuito de prevenir o gasto excessivo de tempo e dinheiro, buscando eliminar o risco de inadimplência, otimizar o fluxo de caixa e personalizar estratégias específicas de cobrança, principalmente antes do dia de pagamento (predição necessária). Em conclusão, plataformas como a da Finnet tendem a ser mais abertas por conta da popularização e consolidação do Open Finance e do Pix. Essa consolidação aumenta a demanda por dados mais ricos e análises mais inteligentes, algo que solidifica seu lugar no mercado.

##### **Análise das 5 Forças de Porter:**

&nbsp;&nbsp;&nbsp;&nbsp;A análise das Cinco Forças de Porter é uma ferramenta estratégica desenvolvida por Michael E. Porter em 1979, que permite avaliar a estrutura competitiva de uma indústria. Ao examinar cinco forças determinantes — ameaça de novos entrantes, ameaça de produtos ou serviços substitutos, poder de barganha dos fornecedores, poder de barganha dos clientes e rivalidade entre os concorrentes existentes —, as empresas podem identificar oportunidades e ameaças em seu ambiente de negócios, auxiliando na formulação de estratégias que sejam competitivas para o setor em que estão inseridas. 

&nbsp;&nbsp;&nbsp;&nbsp;No caso da Finnet, atuar no setor de Techfin B2B significa lidar com barreiras regulatórias elevadas, clientes corporativos sofisticados, fornecedores com poder significativo e uma concorrência que envolve desde players tradicionais até gigantes de ERP e bancos digitais. Utilizar as Cinco Forças de Porter nesse contexto é essencial para compreender como cada uma dessas pressões afeta a atratividade do setor, identificar riscos como a entrada de competidores bem capitalizados ou a verticalização de fornecedores, e direcionar decisões para fortalecer sua posição como orquestradora de serviços financeiros na era do Open Finance. A análise a seguir, baseada no modelo das Cinco Forças de Michael Porter, disseca a estrutura competitiva do setor de Techfin B2B para determinar sua atratividade e identificar as principais pressões que a Finnet enfrenta.

##### **Ameaça de Novos Entrantes (Nível: Baixa a Moderada):**

&nbsp;&nbsp;&nbsp;&nbsp;A ameaça de novos entrantes no setor de Techfin B2B é avaliada como baixa a moderada, sendo mitigada por um conjunto de barreiras estruturais e regulatórias muito bem estruturadas que protegem os agentes estabelecidos. A barreira mais proeminente é a regulatória, imposta pelo Banco Central do Brasil (BACEN). A obtenção de uma licença para operar como Iniciador de Transação de Pagamento (ITP), funcionalidade essencial no ecossistema do Open Finance, é um processo deliberadamente complexo e oneroso, projetado para garantir a solidez e a segurança do sistema financeiro nacional (SFN). Conforme estipulado nas Resoluções BCB nº 80 e 81 de 2021, os postulantes devem comprovar um capital social mínimo de R$ 1 milhão, implementar políticas de governança corporativa auditáveis e submeter-se a um rigoroso e prolongado processo de testes de homologação. Tais exigências criam uma barreira de capital e conformidade que desencoraja a entrada de startups com recursos limitados. 

&nbsp;&nbsp;&nbsp;&nbsp;Adicionalmente, o setor é caracterizado por fortes economias de escala e um poderoso efeito de rede. A proposta de valor de plataformas como a da Finnet é intrinsecamente ligada à amplitude de seu ecossistema, que já interliga mais de 3,2 milhões de CNPJs a mais de 120 instituições financeiras, informações presentes no próprio site da Finnet. Cada novo participante corporativo ou bancário aumenta o valor da rede para todos os existentes, criando um ciclo virtuoso que é extremamente difícil e custoso para um novo concorrente replicar do zero.

&nbsp;&nbsp;&nbsp;&nbsp;Por fim, os custos de troca (switching costs) para os clientes corporativos são altos. A integração de uma solução de automação financeira aos sistemas de gestão empresarial (ERPs) é um processo complexo e que consome tempo e recursos significativos para que seja montado todo o sistema. Uma vez implementada, a solução se torna parte integrante do fluxo de trabalho financeiro, e a migração para um novo provedor implicaria não apenas custos financeiros diretos, mas também riscos operacionais de uma nova experiência de serviços. A confiança depositada em um player estabelecido como a Finnet, que processa mais de R$ 2,1 trilhões anualmente, constitui um ativo intangível de grande valor. Contudo, a ameaça não é inexistente. A ascensão de concorrentes nativos digitais e bem capitalizados, como o Stark Bank — que atraiu um aporte de US$ 45 milhões em uma rodada que incluiu a Bezos Expeditions, fundo de Jeff Bezos — representa um fator de moderação. Tais empresas possuem o capital para superar as barreiras regulatórias e competir agressivamente com base em tecnologia superior e experiência de usuário, visando um nicho de empresas de alto crescimento que podem ter menor inércia para adotar novas soluções.

##### **Poder de Barganha dos Fornecedores (Nível: Moderado a Alto):**

&nbsp;&nbsp;&nbsp;&nbsp;O poder de barganha dos fornecedores é considerado de moderado a alto, exercendo uma pressão constante sobre a rentabilidade e a autonomia da Finnet. Este poder emana de duas fontes principais e interdependentes.

&nbsp;&nbsp;&nbsp;&nbsp;A primeira, e mais crítica, são os grandes provedores de sistemas de gestão empresarial (ERPs), como TOTVS, SAP e Oracle. O modelo de negócio da Finnet é explicitamente posicionado como um "complemento ao seu ERP", o que cria uma dependência grande. Esses fornecedores controlam a plataforma tecnológica central do cliente e, portanto, detêm uma alavancagem negocial muito grande. Eles podem impor custos e condições para o acesso a APIs e, possuem a capacidade de internalizar as funcionalidades oferecidas por parceiros, transformando-se de fornecedores em concorrentes diretos. A TOTVS, líder de mercado no Brasil, já materializou essa ameaça ao lançar sua própria divisão, a TOTVS Techfin, com o objetivo de oferecer um "ERP Banking" que integra serviços financeiros diretamente em suas soluções de gestão.

&nbsp;&nbsp;&nbsp;&nbsp;A segunda fonte de poder são as instituições financeiras (bancos), que fornecem a infraestrutura subjacente para liquidação de pagamentos, custódia de contas e oferta de crédito. Embora a abordagem multibanco da Finnet dilua a dependência de uma única instituição, o sistema bancário como um todo detém um poder considerável, controlando o acesso ao sistema financeiro. A relação da Finnet com os provedores de ERP é, portanto, um delicado equilíbrio. A sustentabilidade de longo prazo da Finnet depende de sua capacidade de inovar a uma velocidade superior à da internalização de funcionalidades pelos ERPs, mantendo uma proposta de valor tão especializada que os clientes a considerem indispensável, mesmo diante de alternativas nativas já existentes.

##### **Poder de Barganha dos Clientes (Nível: Moderado a Alto):**

&nbsp;&nbsp;&nbsp;&nbsp;O poder de barganha dos clientes é classificado como moderado a alto, uma consequência direta do perfil do público-alvo da Finnet: médias e grandes corporações, incluindo algumas das maiores empresas do Brasil, como JBS, Renner, Magazine Luiza e Petrobras. Estes clientes são compradores sofisticados, com departamentos financeiros e de tecnologia muito bem estabelecidos, que gerenciam um volume muito grande de transações. Durante o processo de negociação inicial, esse perfil de cliente exerce um poder de barganha fundamental, podendo demandar personalizações, níveis de serviço (SLAs) rigorosos, certificações de segurança e, naturalmente, preços competitivos. Contudo, a dinâmica de poder se altera após a contratação e implementação da solução.

&nbsp;&nbsp;&nbsp;&nbsp;Uma vez que as plataformas da Finnet estão integradas aos fluxos de trabalho e ao ERP do cliente, os custos de troca tornam-se um fator mitigador de uma possível taxa de evasão. A migração para um concorrente envolveria não apenas o custo de uma nova licença e implementação, mas também a disrupção operacional, o retrabalho de processos internos e o risco inerente a qualquer projeto de TI de grande escala. Essa "pegajosidade" (stickiness) da solução cria uma barreira de saída que reduz o poder do cliente ao longo do ciclo de vida do contrato, permitindo que a Finnet construa relacionamentos de longo prazo e expanda sua oferta de serviços dentro da base instalada.

##### **Ameaça de Produtos ou Serviços Substitutos (Nível: Moderada):**

&nbsp;&nbsp;&nbsp;&nbsp;A ameaça de produtos ou serviços substitutos é moderada, originando-se não de tecnologias disruptivas, mas de abordagens alternativas que os clientes podem adotar para resolver o mesmo problema de automação e integração financeira. A primeira alternativa é o desenvolvimento interno (in-house) de uma plataforma customizada.

&nbsp;&nbsp;&nbsp;&nbsp;Grandes corporações com a presença de equipes de TI podem considerar essa opção para ter controle total sobre a solução. No entanto, essa abordagem acarreta custos proibitivos, não apenas no desenvolvimento inicial, que pode facilmente ultrapassar centenas de milhares de dólares, mas também na manutenção contínua, que exige uma equipe especializada para lidar com as constantes atualizações de APIs bancárias e mudanças regulatórias. 

&nbsp;&nbsp;&nbsp;&nbsp;A segunda, e mais significativa, ameaça de substituição vem dos módulos financeiros nativos oferecidos pelos próprios sistemas ERP. Embora possam ser menos especializados ou ter uma conectividade multibanco inferior à das soluções da Finnet, sua integração nativa representa uma alternativa de baixa conveniência para os clientes. 

&nbsp;&nbsp;&nbsp;&nbsp;A terceira alternativa é a manutenção do status quo, ou seja, a continuidade dos processos manuais. Para muitas empresas, a alternativa à automação é continuar utilizando múltiplos portais de internet banking e planilhas para a conciliação, um processo ineficiente e propenso a erros. Neste caso, o maior concorrente da Finnet não é outra empresa, mas a inércia organizacional. A estratégia comercial deve, portanto, focar em quantificar o custo oculto dessa ineficiência para justificar o investimento na automação.

##### **Rivalidade entre Concorrentes Existentes (Nível: Alta):**

&nbsp;&nbsp;&nbsp;&nbsp;A rivalidade entre concorrentes existentes é classificada como alta, em um cenário competitivo multifacetado onde a Finnet enfrenta adversários de diferentes perfis. 

&nbsp;&nbsp;&nbsp;&nbsp;O rival mais direto é a Accesstage, um incumbente com uma trajetória e modelo de negócio muito similares. Ambas as empresas possuem mais de duas décadas de mercado, foco em pagamentos B2B e gestão financeira, e uma estratégia atual que converge para a liderança no Open Finance B2B, incluindo a obtenção da licença de ITP, o que as coloca em uma disputa acirrada pelo mesmo perfil de cliente corporativo.

&nbsp;&nbsp;&nbsp;&nbsp;Uma segunda frente de competição vem dos disruptores bancários com uma abordagem API-first, cujo principal expoente é o Stark Bank. Nascido como um banco digital para empresas, ele oferece uma suíte completa de serviços (conta, cartões, pagamentos, crédito) em uma única plataforma moderna, ameaçando tornar a camada de integração intermediária da Finnet obsoleta para empresas de tecnologia e startups que buscam uma solução "tudo-em-um".

&nbsp;&nbsp;&nbsp;&nbsp;A terceira camada de rivalidade, mais indireta, é composta por provedores de infraestrutura como serviço (Banking as a Service - BaaS), como a Celcoin. Essas empresas oferecem a infraestrutura modular (APIs de Pix, BaaS, crédito) que permite que outros players, incluindo concorrentes diretos da Finnet, construam e lancem seus próprios serviços financeiros com maior agilidade e menor custo, efetivamente diminuindo as barreiras de entrada para novos competidores de nicho.

&nbsp;&nbsp;&nbsp;&nbsp;Por fim, a ameaça mais significativa a longo prazo vem dos gigantes de ERP, como a TOTVS. Ao alavancar sua posição dominante no sistema de gestão do cliente, a TOTVS, com sua divisão Techfin, pode empurrar suas próprias soluções financeiras integradas, transformando-se de um parceiro em um forte concorrente e com um canal de distribuição já estabelecido.

##### **Conclusão:**

&nbsp;&nbsp;&nbsp;&nbsp;A análise das cinco forças revela que o setor de Techfin B2B no Brasil é moderadamente atrativo. Ele é protegido por altas barreiras de entrada e se beneficia de relações de longo prazo com os clientes, mas, ao mesmo tempo, é caracterizado por uma rivalidade intensa e por pressões de fornecedores e clientes poderosos.

&nbsp;&nbsp;&nbsp;&nbsp;A vantagem competitiva da Finnet está fundamentada em seu ecossistema estabelecido, baseado em confiança, uma vasta rede de conexões e profundas capacidades de integração. Para prosperar no cenário atual, a empresa deve alavancar esses ativos para se consolidar como a ponte indispensável de serviços financeiros B2B na nova era do Open Finance. As implicações são claras: é imperativo acelerar a adoção de novas tecnologias, como as funcionalidades de ITP e Open Finance, para se manter à frente tanto dos rivais tradicionais quanto dos ERPs.

&nbsp;&nbsp;&nbsp;&nbsp;Além disso, aprofundar a integração de produtos é crucial para aumentar os custos de troca para os clientes, defendendo-se contra disruptores "tudo-em-um" como o Stark Bank. É justamente nesses pontos anteriores que surge a oportunidade da ação de um sistema preditivo que possa auxiliar na diferenciação da Finnet frente aos seus principais concorrentes diretos.

&nbsp;&nbsp;&nbsp;&nbsp;Por fim, a Finnet deve explorar ativamente sua posição neutra e multibanco como um diferencial chave contra soluções financeiras que são cativas de um único banco ou de uma única plataforma de ERP.

#### 4.1.2. Análise SWOT 
&nbsp;&nbsp;&nbsp;&nbsp;A compreensão detalhada do contexto competitivo e das forças que moldam o setor de Techfin B2B permite agora avançar para uma avaliação mais integrada da posição estratégica da Finnet. Enquanto a análise das Cinco Forças de Porter destacou as pressões externas e os vetores que influenciam a atratividade do mercado, a Análise SWOT amplia essa visão ao considerar também os fatores internos que sustentam ou limitam a competitividade da empresa. Assim, será possível identificar, de forma estruturada, as principais forças e fraquezas da Finnet, bem como as oportunidades e ameaças presentes no ambiente, oferecendo uma base sólida para orientar decisões e priorizar iniciativas no desenvolvimento da solução proposta.

&nbsp;&nbsp;&nbsp;&nbsp; No contexto do projeto de inadimplência preditiva da Finnet, ela ajuda a mapear vantagens competitivas,assim como pontos de melhoria, oportunidades de mercado e riscos, orientando decisões estratégicas e o alinhamento das soluções às necessidades do cliente.

&nbsp;&nbsp;&nbsp;&nbsp;A análise a seguir apresenta os principais pontos estratégicos identificados para a Finnet, considerando seu posicionamento no setor de automação financeira e integração bancária.

<div align="center">
<sub>Imagem XX: Analise SWOT.</sub>
<img src="https://plum-atomic-lemur-391.mypinata.cloud/ipfs/bafybeiaknofbkipkeskxw4ilfpjmdrjuoen55lzp27me6bpx52jrr6tup4" alt="Analise SWOT">
<sup>Fonte: Material produzido pela equipe, 2025.</sup>
</div>

&nbsp;&nbsp;&nbsp;&nbsp;Forças – A força da Finnet está na especialização em automação financeira e na capacidade de integração com múltiplas instituições bancárias, o que garante eficiência operacional e redução de erros. Além disso, possui um portfólio amplo voltado para médias e grandes empresas.

&nbsp;&nbsp;&nbsp;&nbsp;Oportunidades – O crescimento acelerado do mercado de techfins e a consolidação do Open Finance no Brasil abrem espaço para inovação e expansão da base de clientes. Há também potencial para aumentar a participação de mercado em nível regional e internacional, além de explorar estratégias de marketing mais amplas para fortalecer a marca.

&nbsp;&nbsp;&nbsp;&nbsp;Fraquezas – Uma das principais fraquezas da Finnet é a dependência do mercado nacional, o que a torna mais suscetível a oscilações econômicas e limita a diversificação. Outro desafio recorrente é a necessidade de adaptação constante a requisitos técnicos e regulatórios, o que demanda investimentos contínuos em atualização tecnológica e compliance.

&nbsp;&nbsp;&nbsp;&nbsp;Ameaças – O segmento de tecnologia financeira é altamente regulado, o que impõe riscos legais significativos. A manipulação de dados sensíveis aumenta a exposição a ameaças de segurança da informação. Além disso, há forte concorrência de fintechs, enquanto a instabilidade econômica e política pode afetar diretamente o desempenho da carteira de clientes.

#### 4.1.3. Planejamento Geral da Solução: Previsão de Inadimplência na Plataforma da Finnet

&nbsp;&nbsp;&nbsp;&nbsp;Após a análise detalhada do cenário da Finnet e do setor em que atua, foi possível estruturar o planejamento geral da solução, etapa fundamental para transformar o diagnóstico estratégico em ações concretas. Essa fase é essencial porque define de forma clara como a proposta irá atender às necessidades identificadas, explorando oportunidades e mitigando riscos apontados anteriormente. No caso deste projeto, o foco está no desenvolvimento de um sistema de previsão de inadimplência integrado à plataforma Luna, que trará inteligência preditiva para apoiar a tomada de decisão financeira. Nos tópicos a seguir, serão apresentados o funcionamento da solução, os dados utilizados, as técnicas de modelagem aplicadas, seu uso prático e os critérios de sucesso que orientarão a avaliação de desempenho.

&nbsp;&nbsp;&nbsp;&nbsp;A gestão de boletos e contas a receber é algo muito desafiador e complicado, porém uma etapa crítica para empresas pequenas, médias e grandes. A inadimplência, nesse caso, representa um risco direto ao fluxo de caixa e à saúde financeira do negócio. Este projeto foi projetado e planejado com a função de transformar esse processo de cobrança recorrente em algo planejado e proativo. Isto só se torna possível exclusivamente por conta da nossa solução orientada por dados, agregando diretamente uma inteligência preditiva dentro da plataforma Luna.

&nbsp;&nbsp;&nbsp;&nbsp;O ponto inicial do projeto se baseia na análise e no conjunto de dados transacionais, contendo o histórico de cobranças emitidas. O 'core' do nosso modelo consiste nas seguintes informações:

* **Dados de Cobrança:** informações obrigatórias como `valor_original`, `data_emissão` e `data_vencimento`.
* **Dados do Pagamento:** Histórico de liquidação ou registro, inclui `data_pagamento` e `valor_pago`. Quando esses valores são ausentes, o pagador tem uma inclinação forte à inadimplência.
* **Dados do Pagador:** Identificadores do pagador como `CNPJ` e `CPF`, onde é possível coletar dados particulares e entender o comportamento de cada cliente individual.
* **Dados Comportamentais:** Colunas como `teve_acesso_pagador` e `qtde_acessado_pagador` funcionam como um indicador de intenção do pagador em quitar sua dívida.

&nbsp;&nbsp;&nbsp;&nbsp;O conjunto de dados apresentado contém padrões implícitos que podem ser calculados a partir do que existe e transformá-los em conhecimento adicional. Esse conhecimento será extremamente necessário para o treinamento do modelo e o aprimoramento da acurácia.

&nbsp;&nbsp;&nbsp;&nbsp;A solução será feita através do desenvolvimento de um modelo de Machine Learning de classificação, onde utilizaremos Python e as bibliotecas Pandas, NumPy e Scikit-learn. O Pandas será utilizado para a manipulação de dados e o Scikit-learn para a modelagem. Um dos algoritmos que serão utilizados dentre todos será o `RandomForestClassifier`, um modelo de alta performance para complexidade tabular. Fizemos a escolha de utilizar o Jupyter Notebook para a visualização e exploração dos dados de forma interativa durante o desenvolvimento do modelo preditivo. Isso nos ajudou a criar um modelo fundamentado em um processo iterativo onde cada feature pode ser aprimorada rapidamente, além de possibilitar uma documentação mais acessível e intuitiva.

&nbsp;&nbsp;&nbsp;&nbsp;A Engenharia de Atributos é uma técnica que consiste em transformar os dados brutos em *features* preditivas e inteligentes. O modelo será treinado para prever as tendências de pagamentos de novas cobranças em três categorias: Em Dia, Atraso ou Inadimplente, além de prover um score de risco probabilístico e uma matriz de confusão.

### Utilização e Aplicação

&nbsp;&nbsp;&nbsp;&nbsp;Nosso usuário final será o gestor financeiro ou analista de contas a receber do cliente da Finnet. Essa ferramenta será aplicada diretamente no dashboard da Luna, plataforma da Finnet, gerando eficiência, visualizações inteligentes e preditivas. Com a integração, essa abordagem move a área financeira de uma posição reativa para proativa, diminuindo custos.

&nbsp;&nbsp;&nbsp;&nbsp;Os benefícios esperados dessa implementação seriam a redução da taxa de inadimplência, otimização do fluxo de caixa, permitindo um planejamento financeiro mais confiável, aumento de eficiência operacional e agregação de valor no produto final da Finnet.

### Critérios de Sucesso

Os critérios técnicos que vão medir o sucesso do nosso projeto são:
- Acurácia geral do modelo entre 80 e 94 por cento de precisão.
- Recall para aumentar a acurácia da predição de inadimplência do modelo.
- Validação de acurácia através de banco de dados fictícios, porém parecidos com os originais.
- Não causar overfitting no modelo.
- Feedback positivo da Finnet em relação a eficiência e design da nossa plataforma. 
- Melhora impactante na tomada de decisões e planejamentos financeiros dos usuários da plataforma.

&nbsp;&nbsp;&nbsp;&nbsp;Essas métricas serão utilizadas ao final do projeto para assegurar a Finnet de que o sistema foi desenvolvido de forma robusta e eficiente, sempre visando a qualidade e entrega de resultados. O critério de sucesso proporciona os requisitos mínimos para o sucesso do projeto.  

#### 4.1.4. Canva Proposta de Valor 


&nbsp;&nbsp;&nbsp;&nbsp;O Canva Proposta de Valor é uma ferramenta estratégica que tem como objetivo alinhar o que uma empresa oferece com o que seus clientes realmente valorizam, permitindo uma análise detalhada das necessidades, dores e expectativas do público-alvo em relação às soluções oferecidas. 
&nbsp;&nbsp;&nbsp;&nbsp;Ele é dividido entre o perfil do cliente — que contempla suas tarefas, dores e ganhos — e a proposta de valor — que descreve os produtos e serviços, os criadores de ganho e os analgésicos que aliviam as dores identificadas. No modelo elaborado para a Finnet, observam-se dores relevantes como a elevada taxa de churn e a falta de competitividade com plataformas concorrentes, contrastando com ganhos esperados como o aumento da satisfação dos clientes e da competitividade no mercado. A proposta de valor apresentada responde diretamente a esses pontos ao oferecer uma série de modelos preditivos voltados à análise de risco de inadimplência, previsão de atrasos e identificação da melhor janela de pagamento, o que fortalece a tomada de decisão dos usuários da plataforma Luna, da Finnet. Ao fornecer análises precisas e conectadas às reais necessidades do mercado, o modelo atua como solução prática para os principais desafios enfrentados pela Finnet.
&nbsp;&nbsp;&nbsp;&nbsp;Abaixo encontra-se o canvas da proposta de valor do projeto para FINNET:

<div align="center">
<sub>Figura 01: Canva proposta de valor.</sub>
</div>
<div align="center">
<img src="https://plum-atomic-lemur-391.mypinata.cloud/ipfs/bafkreih5u5yxyy3w4yrhbefp3jcxpiimiiwypb7xu2k53r6o6ysy5ldq2a">
<sub>Fonte: Material produzido pela equipe, 2025.</sub>
</div>

#### 4.1.5. Matriz de Riscos

&nbsp;&nbsp;&nbsp;&nbsp;A matriz de risco é um framework de gestão utilizado para priorização de processos no ambiente de desenvolvimento. Também conhecida como matriz de probabilidade e impacto, ela auxilia no entendimento na gravidade potencial de um risco e sua probabilidade de ocorrência, permitindo que a equipe faça um planejamento estratétigo de mitigação e gerenciamento desses riscos.

&nbsp;&nbsp;&nbsp;&nbsp;O modelo utilizado em questão também inclui uma matriz de oportunidades que, assim como a matriz de risco, permite avaliar possiveis oportunidades e planejar melhores formas de alcançá-las. 

&nbsp;&nbsp;&nbsp;&nbsp;Abaixo encontra-se a matriz de risco do projeto atualizada:


<div align="center">
<sub>Imagem XX: Matriz de Risco.</sub>
<img src="https://plum-atomic-lemur-391.mypinata.cloud/ipfs/bafkreicilpmeffki37op2yab3g4h3uvvtirxbwql3sneteannu6b33spfq" alt="Imagem Matriz de Risco">
<sup>Fonte: Material produzido pela equipe, 2025.</sup>
</div>


#### 4.5.1.1 Especificação de Riscos

A1: O modelo não é transparente ou possível de compreender

&nbsp;&nbsp;&nbsp;&nbsp;A ausência de transparência em modelos preditivos, especialmente em algoritmos complexos como redes neurais, pode dificultar a interpretação dos resultados e a tomada de decisão baseada nos mesmos. Isso compromete a confiança e a adoção por parte dos stakeholders. Este risco foi classificado com alto impacto e média probabilidade.

> #### Plano de mitigação:
>
> Utilização de métodos de interpretabilidade como SHAP (SHapley Additive exPlanations) ou LIME (Local Interpretable Model-agnostic Explanations), além da escolha de algoritmos mais explicáveis quando possível, como árvores de decisão.

---

A2: Dados não qualificados comprometem a predição

&nbsp;&nbsp;&nbsp;&nbsp;Dados inconsistentes, desatualizados ou mal estruturados impactam diretamente a qualidade das predições. Esse risco foi alocado como impacto alto e probabilidade baixa, pois, embora o impacto seja relevante, há processos definidos de ETL (Extração, Transformação e Carga) que podem ser utilizados.

> #### Plano de mitigação:
>
> Implementar pipeline robusto de tratamento e qualificação de dados, com etapas de limpeza, normalização e validação antes da entrada no modelo. Utilizar ferramentas como Pandas e Great Expectations.

---

A3: As predições não são aferíveis

&nbsp;&nbsp;&nbsp;&nbsp;Caso não haja meios de validar ou comparar as predições com dados reais ou referências confiáveis, o modelo pode perder credibilidade e ser descartado. Esse risco foi classificado como impacto muito alto e probabilidade baixa.

> #### Plano de mitigação:
>
> Construção de um conjunto de dados de validação robusto e uso de métricas de avaliação contínuas como precisão, recall, F1-score e AUC-ROC. Monitoramento pós-implantação também é necessário.

---

A4: Underfitting e Overfitting

&nbsp;&nbsp;&nbsp;&nbsp;Em tradução, underfitting e overfitting significam, respectivamente, subajuste e sobreajuste. De acordo com o portal Medium, isso ocorre quando o modelo não aprende ou se adequa demais com os dados de teste. Esse risco foi alocado comode alto impacto e de média-baixa probabilidade, pois, em caso de ocorrência, o modelo todo é comprometido, mas temos ferramentas suficientes para mitiga-lo.

<div align="center">
<sub>Imagem XX: Graficos de adequação de modelos.</sub>
<img src="https://plum-atomic-lemur-391.mypinata.cloud/ipfs/bafkreibnhhw6b3ut7z7z6wksfcuws5lecorturcr752kx3i3dytgfq3tcu" alt="Imagem Matriz de Risco">
<sup>Fonte: Medium, 2025.</sup>
</div>

>  #### Plano de mitigação: 
>
>Feature Selector do scikit-learn para conhecer quais são as features (variáveis) que mais influênciam do modelo preditivo e Learning Curve do scikit-learn, pode ser uma boa visualização para analisar a performance do modelo.

---

A5: O modelo tem baixa confiabilidade

&nbsp;&nbsp;&nbsp;&nbsp;A baixa confiabilidade do modelo significa que os resultados entregues não são consistentes, reprodutíveis ou corretos. Isso pode ocorrer devido à má qualidade dos dados, algoritmos inadequados ou configurações erradas. Classificado como de impacto muito alto e probabilidade alta, é um dos riscos mais críticos identificados.

> #### Plano de mitigação:
>
> Realizar testes de robustez do modelo, validação cruzada k-fold, além da revisão contínua de dados e hiperparâmetros. Implementar também logging e auditoria de previsões para rastrear falhas.

---

#### 4.1.5.2 Especificação de Oportunidades

O1: O modelo aumenta a confiabilidade dos usuários na empresa

&nbsp;&nbsp;&nbsp;&nbsp;A adoção do modelo pode auxiliar a Finnet na antecipação de comportamentos de inadimplência, permitindo ações proativas e redução de prejuízos para os clientes, aumentando sua confiança com a empresa. Classificado como impacto muito alto e probabilidade baixa.

---

O2: As predições do modelo são confiáveis

&nbsp;&nbsp;&nbsp;&nbsp;Ter um modelo cujas predições demonstram precisão e coerência em diferentes cenários favorece sua adoção e confiança por parte dos usuários. Essa oportunidade foi classificada com impacto muito alto e probabilidade média.

---

O3: A Finnet tem interesse em aplicar o modelo

&nbsp;&nbsp;&nbsp;&nbsp;O interesse da empresa em adotar a solução impulsiona a continuidade do projeto e aumenta as chances de implantação real. Classificado como impacto alto e probabilidade baixa.

---

O4: A solução é escalável para ambiente de execução

&nbsp;&nbsp;&nbsp;&nbsp;Se o modelo puder ser escalado para diferentes volumes de dados e usuários sem perda de desempenho, ele se torna viável para produção. Classificado como impacto moderado e probabilidade média.

---

O5: O modelo possui compatibilidade com a platafroma Luna

&nbsp;&nbsp;&nbsp;&nbsp;A compatibilidade do modelo com a plataforma Luna permite integração direta, reduzindo custos e tempo de implementação. Classificado como impacto moderado e probabilidade alta.


#### 4.1.6. Personas

&nbsp;&nbsp;&nbsp;&nbsp;As personas são representações fictícias de perfis reais que ajudam a compreender necessidades e objetivos dos diferentes públicos de um projeto, com o objetivo de aproximar a solução com as dores reais de seus usuários, orientando decisões de design, desenvolvimento e comunicação. 

&nbsp;&nbsp;&nbsp;&nbsp;Para o projeto, definimos quatro personas: duas sob a ótica de profissionais internos da Finnet (representados nos quadros azuis) - um Analista de Dados e um Gerente de TI, responsáveis por alimentar, gerenciar e integrar o modelo preditivo - e  duas sob a perspectiva de usuários da plataforma Luna (representados nos quadros verdes), que são os clientes da Finnet que utilizam a plataforma para gestão de cobranças e recebíveis. Essa abordagem garante que o projeto contemple tanto questões de experiência do cliente quanto as demandas técnicas e operacionais da equipe.

&nbsp;&nbsp;&nbsp;&nbsp;Abaixo encontram-se as personas desenvolvidas:


##### Persona David
<div align="center">
<sub>Figura XX: Persona Finnet David.</sub>
</div>
<div align="center">
<img src="https://plum-atomic-lemur-391.mypinata.cloud/ipfs/bafybeibjk444ju4ea33q3uftxq74ibvjfh2gj4zf7gcbjkec4pa3u2pq6e" alt="Persona David">
<sub>Fonte: Material produzido pela equipe, 2025.</sub>
</div>

<br/>&nbsp;&nbsp;&nbsp;&nbsp;**Descrição:** David é um analista de dados sênior de 30 anos que trabalha na plataforma Luna e está na empresa FINNET há 10 anos. Ele é formado em Engenharia de Software. Seus principais desafios incluem a dificuldade em manter os sistemas atualizados e o fato de lidar frequentemente com modelos complexos e difíceis de entender. Sua motivação é encontrar uma solução que seja fácil de manter, treinar e escalar. A solução que ele busca é um modelo preditivo que seja compreensível, escalável, com variáveis mapeadas e compatível com a plataforma Luna.

---

##### Persona Cecília
<div align="center">
<sub>Figura XX: Persona Finnet Cecília.</sub>
</div>
<div align="center">
<img src="https://plum-atomic-lemur-391.mypinata.cloud/ipfs/bafybeiby7lwpp4prdu6ldf55272dlcob2xotnd76ac6ugyiaqzdyzpo63a" alt="Persona Cecília">
<sub>Fonte: Material produzido pela equipe, 2025.</sub>
</div>


<br/>&nbsp;&nbsp;&nbsp;&nbsp;**Descrição:** Cecília tem 33 anos, é Head de Negócios na Finnet e trabalha lá há 12 anos. Ela é formada em Ciência de Dados e se dedica a garantir a saúde e a integridade dos negócios da empresa, mantendo a conformidade com a legislação local. Seus principais desafios são a dificuldade em fornecer métricas claras sobre inadimplência e tendência de pagamentos para os clientes, além de proteger dados sensíveis conforme as diretrizes da LGPD. Sua motivação é conquistar mais confiança com os stakeholders, obter maior poder de negociação e garantir a conformidade e estabilidade legal. A solução ideal para ela é um modelo preditivo que forneça métricas confiáveis e fáceis de entender, ao mesmo tempo que assegura a integridade legal dos dados sensíveis da empresa.

---

##### Persona Alice 
<div align="center">
<sub>Figura XX: Persona cliente Alice.</sub>
</div>
<div align="center">
<img src="https://plum-atomic-lemur-391.mypinata.cloud/ipfs/bafkreif3nljnowr3sqsfzasucoqj5ianyg7kp2jglhxkrwvfoax66nbtzi" alt="Persona Alice">
<sub>Fonte: Material produzido pela equipe, 2025.</sub>
</div>

<br/>&nbsp;&nbsp;&nbsp;&nbsp;**Descrição:** Marcelo é um gerente financeiro de 38 anos em uma empresa de médio porte, formado em Ciências Contábeis. Seu objetivo principal é aumentar a previsibilidade do fluxo de caixa e reduzir a inadimplência. Seus desafios incluem a dificuldade em prever o melhor momento para fazer cobranças, a pressão da diretoria para melhorar a taxa de recebimento e a alta taxa de inadimplência de clientes recorrentes. Sua motivação é automatizar as análises e previsões de pagamento para diminuir a dependência de planilhas manuais e análises demoradas. A solução ideal para ele é um modelo que forneça pontuações de risco e previsões de pagamento, permitindo que ele tome decisões de cobrança mais assertivas, ajustando datas e estratégias de forma eficiente.

---

##### Persona Marcelo 
<div align="center">
<sub>Figura XX: Persona clienete Marcelo.</sub>
</div>
<div align="center">
<img src="https://plum-atomic-lemur-391.mypinata.cloud/ipfs/bafkreiddn73arqvhjkawbdxzzn74vuc5okwh6zlohp7t5y6hx4fkpac3ta" alt="Persona Marcelo">
<sub>Fonte: Material produzido pela equipe, 2025.</sub>
</div>

<br/>&nbsp;&nbsp;&nbsp;&nbsp;**Descrição:** Marcelo tem 38 anos, é o diretor financeiro de uma grande empresa e é formado em Economia. Seu objetivo principal é otimizar o capital de giro e aumentar a previsibilidade financeira para auxiliar na tomada de decisões estratégicas. Seus principais desafios incluem a dificuldade em consolidar informações de diferentes unidades da empresa e o impacto da inadimplência no fluxo de caixa projetado. Sua motivação é obter indicadores claros e confiáveis para apresentar ao conselho e à diretoria, além de integrar inteligência preditiva ao sistema financeiro que a empresa já utiliza. A solução ideal para ele é um modelo que ofereça previsões de recebimento e análises de risco, permitindo ajustes estratégicos no planejamento financeiro.

<hr/>

&nbsp;&nbsp;&nbsp;&nbsp;Em conclusão, as personas desenvolvidas para o projeto oferecem uma visão clara e objetiva dos principais perfis que interagem com a solução. Essa abordagem garante que o desenvolvimento do produto considere simultaneamente as necessidades e expectativas do usuário final e os requisitos técnicos e operacionais da equipe, criando um alinhamento estratégico que favorece a entrega de valor e a eficiência da solução.

**Link das personas:** https://www.canva.com/design/DAGvyXrSyLQ/MwDC1k6Vhzp1U0Gin9fFqg/edit

#### 4.1.7. Jornadas do Usuário

&nbsp;&nbsp;&nbsp;&nbsp;A jornada de usuário é uma representação visual do caminho que uma pessoa percorre ao interagir com um produto ou serviço. Ela mostra as etapas, necessidades e sentimentos envolvidos em cada momento dessa experiência até atingir um objetivo específico.

&nbsp;&nbsp;&nbsp;&nbsp;Em relação ao projeto, a jornada de usuário descreve como os diferentes perfis de usuários interagem com o sistema preditivo desenvolvido. O objetivo é garantir que a utilização da solução, desde a coleta de dados até a interpretação dos resultados, seja intuitiva, eficiente e confiável.  

&nbsp;&nbsp;&nbsp;&nbsp;Além disso, a jornada de usuário serve como guia para alinhar as necessidades de negócio da Finnet às expectativas dos usuários finais, oferecendo valor real na redução da inadimplência e no processo de tomada de decisão.

&nbsp;&nbsp;&nbsp;&nbsp;Abaixo lista-se todas as jornadas de usuário produzidas:

#### Jornada de usuário da Persona Alice
&nbsp;&nbsp;&nbsp;&nbsp;Alice, 33 anos, é gerente financeira em uma empresa de médio porte. A seguir, descrevem-se as etapas de sua jornada com o modelo, destacando como a solução a apoia em cada fase do processo.

<div align="center">
<sub>Figura XX: Jornada de usuário da Alice.</sub>
</div>
<div align="center">
<img src="https://plum-atomic-lemur-391.mypinata.cloud/ipfs/bafybeih5oakd6aqk5ftjw2tdif3hgmwlpnxdbo2chtaqb7r6feh2orzkbm" alt="Jornada de usuário Alice - Figura">
</div>
<div align="center">
<sub>Fonte: Material produzido pela equipe, 2025.</sub>
</div>

##### Etapas da Jornada:

&nbsp;&nbsp;&nbsp;&nbsp; A jornada da persona Alice foi estruturada para representar como uma usuária interagiria com o modelo preditivo ao longo de diferentes fases de uso. Cada etapa foi mapeada considerando os desafios enfrentados por profissionais em sua posição e como a solução pode apoiá-los na tomada de decisão. Esse mapeamento permite visualizar não apenas a utilização prática do sistema, mas também os ganhos de valor gerados em cada momento da experiência, desde a descoberta inicial até a consolidação de resultados junto à diretoria.

&nbsp;&nbsp;&nbsp;&nbsp;Fase 1 – Consulta Inicial: Alice inicia sua interação acessando a plataforma Luna para verificar previsões de inadimplência. Nesse momento, sua principal dúvida é sobre a confiabilidade dos números apresentados. É a fase de descoberta, onde ela começa a compreender os dados disponíveis e a potencial utilidade do sistema.

&nbsp;&nbsp;&nbsp;&nbsp;Fase 2 – Identificação de clientes: Alice analisa relatórios de risco e previsões de inadimplência, priorizando clientes críticos para atuação imediata. Aqui, ela consegue visualizar onde deve concentrar esforços, transformando dados em ações direcionadas. É a fase de diagnóstico, em que o sistema apoia decisões iniciais de intervenção.

&nbsp;&nbsp;&nbsp;&nbsp;Fase 3 – Estratégia de cobrança: Alice seleciona clientes, ajusta prazos e modos de cobrança e gera relatórios com previsões de recebimento para a diretoria. Essa etapa é estratégica, pois permite que ela justifique decisões baseadas em dados concretos, estabelecendo um plano de ação formalizado.

&nbsp;&nbsp;&nbsp;&nbsp;Fase 4 – Acompanhamento dos resultados: Alice monitora indicadores após aplicar as estratégias e prepara relatórios finais sobre a evolução das taxas de inadimplência. Aqui, ela valida a efetividade das ações implementadas, refletindo sobre o impacto real das estratégias adotadas.

&nbsp;&nbsp;&nbsp;&nbsp;Fase 5 – Relato à diretoria: Alice apresenta aos executivos os resultados do período e propõe novas estratégias com base nas evidências coletadas. É a fase de consolidação, em que o valor do trabalho de Alice é evidenciado através de dados, reforçando decisões futuras e orientando ajustes estratégicos.

&nbsp;&nbsp;&nbsp;&nbsp;Fase 5 – Relato à diretoria: Alice apresenta aos executivos os resultados do período e propõe novas estratégias com base nas evidências coletadas. É a fase de consolidação, em que o valor do trabalho de Alice é evidenciado através de dados, reforçando decisões futuras e orientando ajustes estratégicos.

&nbsp;&nbsp;&nbsp;&nbsp;A jornada de Alice demonstra como o modelo a apoia em todo o ciclo de gestão da inadimplência: da análise inicial dos dados, passando pela definição de estratégias, até o acompanhamento e a apresentação de resultados. Cada etapa reforça a confiabilidade do sistema e seu papel em transformar previsões em decisões práticas e estratégicas.


#### Jornada de usuário da Persona Cecília
&nbsp;&nbsp;&nbsp;&nbsp;Cecília, 33 anos, é Head de Negócios na Finnet. A seguir, descrevem-se as etapas de sua jornada com o modelo, destacando como a solução a apoia em cada fase do processo.


<div align="center">
<sub>Figura XXI: Jornada de usuário da Cecília.</sub>
</div>
<div align="center">
<img src="https://plum-atomic-lemur-391.mypinata.cloud/ipfs/bafybeib3c7tjcjbjdlhwvtpsjktwn6pqfyjqh4ekvjbqh3wkscc5gt3olm" alt="Jornada de usuário Cecília - Figura">
</div>
<div align="center">
<sub>Fonte: Material produzido pela equipe, 2025.</sub>
</div>

#### Etapas da Jornada de Cecília com o modelo:

&nbsp;&nbsp;&nbsp;&nbsp;Os principais desafios da Cecília envolvem oferecer métricas claras sobre inadimplência e proteger dados sensíveis, buscando fortalecer a confiança dos stakeholders. Nesse contexto, sua jornada com o modelo foi mapeada para mostrar como a solução a apoia desde a percepção inicial do problema até a avaliação de resultados, assegurando eficiência, confiabilidade e aderência às normas legais.

&nbsp;&nbsp;&nbsp;&nbsp;Fase 1 – Percepção do problema: Cecília acessa a plataforma Luna e revisa os objetivos do projeto. Nesse momento, registra os dados iniciais do cliente e confirma que todas as informações estão em conformidade com as normas legais. É a fase de descoberta, onde ela entende o cenário e garante a legalidade dos dados coletados.

&nbsp;&nbsp;&nbsp;&nbsp;Fase 2 – Busca por soluções: Cecília importa e filtra os dados dos clientes, criando segmentos ou categorias relevantes. Durante essa etapa, valida as informações com a documentação legal disponível. É a fase de diagnóstico, em que o sistema ajuda Cecília a identificar oportunidades e soluções possíveis.

&nbsp;&nbsp;&nbsp;&nbsp;Fase 3 – Definição da estratégia: Cecília executa o modelo preditivo na plataforma Luna, revisando os resultados e ajustando parâmetros conforme necessário. Aqui, o processamento é realizado dentro das normas legais, tornando essa fase estratégica, pois decisões baseadas em dados passam a ser formalizadas.

&nbsp;&nbsp;&nbsp;&nbsp;Fase 4 – Implementação da solução: Cecília exporta relatórios e dashboards, compartilha os resultados com stakeholders e registra auditorias de conformidade legal. É a fase de execução, onde as ações planejadas são colocadas em prática e acompanhadas.

&nbsp;&nbsp;&nbsp;&nbsp;Fase 5 – Avaliação dos resultados: Cecília compara os resultados obtidos com as metas e expectativas iniciais, identifica melhorias ou ajustes necessários e documenta aprendizados e recomendações futuras. É a fase de consolidação, que evidencia o impacto das ações e orienta decisões estratégicas posteriores.

&nbsp;&nbsp;&nbsp;&nbsp;A jornada de Cecília evidencia como o modelo oferece suporte estratégico em todas as fases: desde a coleta e validação inicial dos dados até a avaliação final dos resultados. O processo não só garante conformidade legal e transparência, mas também fortalece a credibilidade da Finnet junto a seus stakeholders, permitindo que Cecília amplie seu poder de negociação e consolide a confiança no uso de métricas preditivas confiáveis.

---

##### Conslusão:
&nbsp;&nbsp;&nbsp;&nbsp;O estudo das etapas da jornada do usuário foi fundamental para compreender como diferentes perfis interagem com a solução e quais pontos do processo exigem maior clareza, suporte ou automação. Esse mapeamento contribuiu diretamente para o projeto ao alinhar as necessidades reais dos usuários com os objetivos estratégicos da Finnet, garantindo que o modelo preditivo fosse não apenas tecnicamente robusto, mas também aplicável de forma prática e intuitiva no dia a dia.

&nbsp;&nbsp;&nbsp;&nbsp;A partir desse levantamento, tornou-se evidente que cada persona possui motivações e desafios específicos — Alice voltada à previsibilidade financeira e Cecília à conformidade legal e credibilidade institucional. Ao integrar essas perspectivas, o projeto alcança uma visão mais completa, permitindo que a solução atenda tanto às demandas operacionais quanto às estratégicas, fortalecendo a confiança dos usuários e o valor entregue pela ferramenta.

---

#### 4.1.8 Política de Privacidade


&nbsp;&nbsp;&nbsp;&nbsp;A presente Política de Privacidade estabelece como a solução Infinnet, desenvolvida pela equipe Bill Hunters, realiza a coleta, o uso, o armazenamento e a proteção de dados pessoais e não pessoais. Nosso compromisso é garantir que o tratamento dessas informações esteja em conformidade com a Lei nº 13.709/2018 – Lei Geral de Proteção de Dados (LGPD), respeitando os direitos dos titulares e assegurando a transparência quanto às práticas adotadas no projeto.



#### Informações Gerais  
A política aplica-se a todos os dados processados no contexto de desenvolvimento do modelo preditivo de comportamento do pagador, utilizado para análises, testes e geração de hipóteses.  



#### Dados Coletados  
Durante o uso da solução, são tratados dados que permitem identificar transações financeiras e interações dos usuários com a plataforma. Entre eles:  

- id_grupo – Identificador único do grupo ou lote de boletos relacionados  
- id_beneficiario – Identificador da pessoa ou empresa que emite o boleto  
- Numero_do_boleto – Código numérico exclusivo de cada boleto  
- data_inclusao – Data de registro do boleto no sistema  
- status_boleto – Situação atual do boleto (em aberto, pago, vencido, cancelado)  
- data_vencto – Data de vencimento do boleto  
- vl_boleto – Valor total do boleto emitido  
- dt_pagto – Data em que o pagamento foi efetuado  
- vl_pagto – Valor efetivamente pago  
- banco – Banco responsável pelo registro do boleto  
- id_pagador – Identificador único do pagador  
- pagador_cep – CEP do endereço do pagador  
- pagador_cidade – Cidade do pagador  
- qtd_acessos_pagador – Número de acessos do pagador à plataforma  
- pagador_dt_ultimo_acesso – Data do último acesso do pagador  
- pagador_cnpjcpf – Documento do pagador (CPF ou CNPJ)  
- Teve_acesso_pagador – Indicação se houve ou não acesso do pagador ao sistema  



#### Finalidade do Tratamento  
Os dados coletados têm como finalidade alimentar e validar hipóteses para o desenvolvimento de um modelo preditivo de inadimplência. Esse processo possibilita maior assertividade na análise de riscos e no comportamento de pagamento dos clientes.  


#### Armazenamento e Retenção  
- Local: Servidores locais  
- Prazo: 2 meses, período necessário para fins de pesquisa e desenvolvimento  


#### Compartilhamento de Dados  
O compartilhamento de informações pode ocorrer com:  
- Parceiros técnicos para processamento e validação de transações  
- Fornecedores de serviços contratados para apoiar o projeto  
- Órgãos reguladores e autoridades legais, sempre que houver obrigação normativa  


#### Segurança dos Dados  
A equipe adota medidas de segurança compatíveis com as boas práticas de mercado, incluindo:  
- Criptografia em trânsito e em repouso  
- Monitoramento e auditoria contínua do sistema  
- Políticas internas de controle de acesso  


#### Direitos dos Titulares  
Em conformidade com a LGPD, o titular dos dados pode solicitar:  
- Acesso às informações coletadas  
- Correção de dados incorretos  
- Exclusão dos dados pessoais tratados  
- Revogação do consentimento de uso  

As solicitações podem ser enviadas para o e-mail do Encarregado de Dados (DPO): [mbuchala@gmail.com](mailto:mbuchala@gmail.com).  


#### Encarregado de Dados (DPO)  
- Nome: Marília Nascimbeni Buchala  
- E-mail: [mbuchala@gmail.com](mailto:mbuchala@gmail.com)  


#### Conclusão  
A Política de Privacidade da Infinnet foi elaborada para reforçar o compromisso da equipe com a transparência, a conformidade legal e a proteção dos dados tratados. Ao descrever claramente quais informações são coletadas, como são utilizadas e quais direitos podem ser exercidos, busca-se assegurar que a solução seja desenvolvida de forma ética, responsável e em total respeito aos usuários e às exigências da LGPD.  

---

### 4.2. Compreensão dos Dados
Esta e a documentacao técnica referente às etapas de exploração, pré-processamento e formulação de hipóteses desenvolvidas no Colab Notebook do Modelo Preditivo. O propósito central é registrar de forma clara e objetiva as decisões adotadas durante o processo de preparação dos dados, contemplando desde o carregamento e identificação das variáveis até a realização de análises estatísticas e a geração de novas features relevantes para o modelo. Ao longo das etapas, foram aplicadas técnicas de estatística descritiva, limpeza de dados, normalização e codificação de variáveis, bem como a investigação de outliers e a elaboração de hipóteses sobre o comportamento dos clientes e boletos.

#### 4.2.1. Exploração de dados
Nesta etapa, buscamos entender a estrutura da base e identificar padrões iniciais.  

- **Unificação** de arquivos em um único DataFrame.  
- **Classificação das variáveis**:  
  - Numéricas → `vl_boleto`, `vl_pagto`, `qtd_acessos_pagador`  
  - Categóricas → `status_boleto`, `banco`, `pagador_cidade`  
  - Temporais → `data_inclusao`, `data_vencimento`, `data_pagamento`  

### Código utilizado:
  ```python
#Carrega o arquivo Excel
df1= pd.read_excel("../dados/Grupo1-GL.xlsx")
df2= pd.read_excel("../dados/Grupo3-GP.xlsx")
df3= pd.read_excel("../dados/Grupo4-GT.xlsx")
df4= pd.read_excel("../dados/Grupo2-GM.xlsx")
#Une os todos os arquivos formando um so
df = pd.concat([df1,df2,df3, df4] ,ignore_index = True)
#Imprime os 5 primeiras colunas 
df.head()
#Imprime as classificação 
df.dtypes
#Separa as colunas entre numericas e categoricas 
colunas_numericas = df.select_dtypes(include = ['int64', 'float64']).columns
colunas_categoricas = df.select_dtypes(include = ['object']).columns

print("Colunas Numericas:", colunas_numericas)
print("Colunas Categoricas:", colunas_categoricas)
```
- **Estatísticas descritivas**: resumo de mínimos, máximos, médias e desvios.  
- **Visualizações**: histograma (valor do boleto), boxplot (valor pago) e barras (status de pagamento).  

### Código utilizado:
```python
df.dtypes
df[colunas_numericas].describe().T
df["vl_boleto"].plot(kind="hist", bins=40)
df["vl_pagto"].plot(kind="box")
df["status_pagamento"].value_counts().plot(kind="bar")
```
#### Dispersão valor emitido x pago: 
Esse gráfico mostra a relação entre os valores emitidos e os pagos, identificando os pontos acima e abaixo da linha.

<img width="450" height="960" alt="grafico1_dispersao_valor_emitido_vs_pago" src="https://github.com/user-attachments/assets/591c4968-4337-4c27-bec8-7888edb45a72" />

#### Pizza de boletos por cidade: 
Representa a distribuição dos boletos entre diferentes cidades.

<img src="https://github.com/user-attachments/assets/07c45df7-d1f6-4ac9-94b9-f43740cad29c" width="450">

#### Histograma dos valores dos boletos: 
Mostra a vizualização da frequência de boletos com valores diferentes.

<img src="https://github.com/user-attachments/assets/291550a6-df90-4e8c-abac-83409d630272" width="450">

#### Série temporal mensal: 
Mostra os boletos emitidos e pagos ao longo do tempo.

<img width="450" height="960" alt="grafico5_serie_temporal_mensal" src="https://github.com/user-attachments/assets/00fe9a95-f1d7-49a5-bfd9-6a81631f21e3" />



#### 4.2.2. Pré-processamento dos dados
O objetivo desta etapa foi **limpar e padronizar os dados** para uso em modelos de Machine Learning.  

- **Tratamento de Missing Values**: substituição de `\N` por `NaN` e remoção de registros com informações essenciais ausentes.  
- **Conversões**:  
  - Datas → `datetime`  
  - Valores → numéricos  
- **Outliers**: identificados em `vl_boleto` e `vl_pagto`; mitigados por normalização Min-Max.  
- **Transformações**:  
  - `dias_de_atraso` = diferença entre data de pagamento e vencimento  
  - `status_pagamento` = categorização (Em Dia / Atraso / Inadimplente)  
- **Codificação**: aplicação de **One-Hot Encoding** em variáveis categóricas.  

###  Código utilizado:
```python
df = df.replace("\N", np.nan)

df["vl_boleto"] = pd.to_numeric(df["vl_boleto"], errors="coerce")
df["vl_pagto"] = pd.to_numeric(df["vl_pagto"], errors="coerce")
df["data_pagamento"] = pd.to_datetime(df["data_pagamento"], errors="coerce")

df["dias_de_atraso"] = (df["data_pagamento"] - df["data_vencimento"]).dt.days
df["status_pagamento"] = df["dias_de_atraso"].apply(definir_status)

from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
df[["vl_boleto","vl_pagto"]] = scaler.fit_transform(df[["vl_boleto","vl_pagto"]])

df = pd.get_dummies(df, columns=["banVco","status_boleto","status_pagamento"], drop_first=True)
```
#### 4.2.3. Hipóteses

#### Glossário

| Variável                    | Definição                                                                 |
|----------------------------|---------------------------------------------------------------------------|
| **vl_boleto**              | Valor total do boleto emitido.                                           |
| **status_boleto**          | Situação atual do boleto (em aberto, pago, vencido, cancelado).      |
| **data_vencto**            | Data de vencimento do boleto.                                            |
| **dt_pagto**               | Data em que o boleto foi pago.                                           |
| **vl_pagto**               | Valor efetivamente pago do boleto.                                       |
| **qtd_acessos_pagador**    | Número de vezes que o pagador acessou a plataforma/sistema.               |
| **pagador_dt_ultimo_acesso** | Data do último acesso realizado pelo pagador.                         |

Para entender a relação entre os dados e o problema, elaboramos hipóteses com o objetivo de explicar potenciais fatores associados ao não pagamento dos boletos no prazo, assim nos permitindo validar quais variáveis possuem maior relevância na previsão do comportamento dos pagadores.

**Hipótese 1 – Relação entre valor do boleto e inadimplência**  

*Variáveis relevantes para essa Hipótese* : vl_boleto, status_boleto, data_vencto, dt_pagto

Boletos de maior valor apresentam maior probabilidade de não serem pagos até o vencimento.  
Isso porque eles exigem maior disponibilidade financeira e muitas vezes com um prazo não tão extenso, diferente de títulos menores que podem ser liquidados mais facilmente, valores altos aumentam a probabilidade de atraso ou de não pagamento, já que podem exigir um comprometimento e um capital mais alto junto com mais tempo do que boletos de valores baixos.

**Hipótese 2 – Impacto da atividade do pagador no pagamento**  

*Variáveis relevantes para essa Hipótese* : qtd_acessos_pagador, pagador_dt_ultimo_acesso, status_boleto, data_vencto, dt_pagto  

Pagadores com maior número de acessos recentes na plataforma têm menor chance de inadimplência.
Uma vez que o acompanhamento frequente dos boletos sugere atenção aos pagamentos. Pagadores engajados tendem a identificar vencimentos antecipadamente e tomar medidas para quitar suas dívidas no prazo, reduzindo o risco de atraso.

**Hipótese 3 – Histórico de pagamento parcial como indicador de risco**  

*Variáveis relevantes para essa Hipótese* : vl_pagto, vl_boleto, status_boleto  

Boletos que registram pagamentos parciais muito inferiores ao valor total do boleto têm maior probabilidade de gerar inadimplência futura.  
Isso seria um pagamento simbólico, onde o devedor paga uma parte pequena do valor, um sinal, para constar como um pagamento inicial, mostrando que irá pagar o restante futuramente para evitar consequências, mas não completa o pagamento.

### 4.3. Preparação dos Dados e Modelagem 

a) Organização dos dados (conjunto de treinamento, validação e testes)

O projeto utiliza um modelo supervisionado para previsão de inadimplência de clientes. A organização dos dados foi estruturada da seguinte forma:

Dataset Original:
- Total de registros: 1.202.864 linhas
- Após limpeza: 1.172.662 linhas (97.49% dos dados válidos)
- Distribuição das classes:
  - Inadimplente: 521.308 registros (44.4%)
  - Em Dia: 458.497 registros (39.1%)
  - Atraso: 192.857 registros (16.4%)

Divisão dos Dados:
- Conjunto de Treinamento: 75% dos dados (879.496 registros)
- Conjunto de Teste: 25% dos dados (293.165 registros)
- Estratificação: Mantida a proporção das classes em ambos os conjuntos
- Random State: 42 (para reprodutibilidade)

Critérios de Limpeza:
- Remoção de registros com valores nulos nas colunas essenciais (`data_vencimento`, `valor_original`, `pagador`)
- Conversão de tipos de dados para formatos adequados
- Tratamento de valores ausentes em `qtde_acessado_pagador` (convertidos para 0)

b) Modelagem para o problema (proposta de features com explicação completa da linha de raciocínio)

O problema foi modelado como uma classificação binária para prever inadimplência (`target_inad`: 1 = Inadimplente, 0 = Não Inadimplente).

Features Principais Criadas:

1. `dia_semana_vencimento` - Dia da semana do vencimento (0-6)
   - *Justificativa:* Padrões comportamentais podem variar conforme o dia da semana

2. `valor_medio_pagador` - Média histórica de valores pagos pelo cliente
   - *Justificativa:* Identifica consistência no comportamento de pagamento

3. `razao_valor_vs_media` - Razão entre valor atual e média histórica (limitada 0-10)
   - *Justificativa:* Valores muito acima da média podem indicar maior risco

4. `hist_std_dias_atraso` - Desvio padrão histórico dos dias de atraso
   - *Justificativa:* Mede consistência; alta variabilidade indica maior risco

5. `tempo_relacionamento_dias` - Tempo desde primeira cobrança até atual
   - *Justificativa:* Clientes novos podem ter comportamento mais incerto

6. `tipo_pagador` - CPF ou CNPJ
   - *Justificativa:* Tipos diferentes podem ter comportamentos financeiros distintos

7. `dias_emissao_vencimento` - Prazo entre emissão e vencimento
   - *Justificativa:* Prazos menores podem aumentar urgência e risco

8. `status_pagamento_anterior` - Status da última cobrança do cliente
   - *Justificativa:* Captura tendências recentes de comportamento

9. `hist_total_cobrancas` - Total de cobranças históricas do cliente
   - *Justificativa:* Indica experiência e histórico de relacionamento

10. `hist_media_dias_atraso` - Média histórica de dias de atraso
    - *Justificativa:* Clientes que atrasam frequentemente têm maior risco

11. `hist_taxa_inadimplencia` - Proporção histórica de inadimplências
    - *Justificativa:* Representa risco agregado baseado no histórico

12. `vencimento_prox_fds` - Indicador se vencimento é próximo ao fim de semana
    - *Justificativa:* Vencimentos próximos ao fim de semana podem aumentar risco

13. `hist_taxa_atraso` - Proporção histórica de atrasos
    - *Justificativa:* Reflete consistência no cumprimento de pagamentos

14. `risco_interacao_valor_atraso` - Produto entre razão de valor e taxa de atraso
    - *Justificativa:* Combina impacto de valores altos com propensão a atrasos

c) Métricas relacionadas ao modelo (pelo menos 3)

Métricas Principais Utilizadas:

1. Accuracy (Acurácia): 96.44%
   - *Definição:* Proporção de previsões corretas sobre o total
   - *Relevância:* Mede performance geral do modelo

2. Precision (Precisão): 91% para classe Inadimplente
   - *Definição:* Dos casos previstos como inadimplentes, quantos realmente eram inadimplentes
   - *Relevância:* Evita falsos positivos, importante para não penalizar clientes bons

3. Recall (Sensibilidade): 92.5% para classe Inadimplente
   - *Definição:* Dos casos realmente inadimplentes, quantos o modelo conseguiu identificar
   - *Relevância:* Evita falsos negativos, crucial para identificar riscos reais

4. F1-Score: 92% para classe Inadimplente
   - *Definição:* Média harmônica entre precision e recall
   - *Relevância:* Balanceia precisão e sensibilidade, ideal para classes desbalanceadas

5. OOB Score (Out-of-Bag): 96.47%
   - *Definição:* Estimativa interna do RandomForest para generalização
   - *Relevância:* Validação cruzada automática, indica capacidade de generalização

d) Primeiro modelo candidato e discussão dos resultados

Modelo Escolhido: RandomForestClassifier

Configuração do Modelo:
- Algoritmo: RandomForestClassifier
- Número de árvores: 300 estimadores
- Profundidade máxima: 35 níveis
- Amostras mínimas por folha: 4
- Peso das classes: 'balanced' (ajusta automaticamente para classes desbalanceadas)
- Paralelização: n_jobs=-1 (usa todos os núcleos disponíveis)
- OOB Score: Ativado para validação interna

Justificativa da Escolha:
1. Robustez a outliers: Não é sensível a valores extremos
2. Flexibilidade: Funciona bem com features contínuas e categóricas
3. Validação interna: OOB score fornece estimativa de generalização
4. Interpretabilidade: Permite análise de importância das features
5. Performance: Boa performance em problemas de classificação

Resultados do Modelo:

```
Acurácia Geral: 96.44%
OOB Score: 96.47%

Relatório de Classificação:
              precision    recall  f1-score   support
           0       0.98      0.98      0.98    103966
           1       0.91      0.93      0.92     29169
    accuracy                           0.96    133135
```

Discussão dos Resultados:

Pontos Fortes:
- Alta acurácia geral (96.44%): O modelo apresenta excelente performance na classificação geral
- Bom recall para inadimplência (92.5%): Consegue identificar 92.5% dos casos realmente inadimplentes
- Precisão adequada (91%): Dos casos previstos como inadimplentes, 91% realmente são inadimplentes
- Consistência: OOB score (96.47%) confirma a capacidade de generalização

Análise por Classe:
- Classe 0 (Não Inadimplente): Precision=98%, Recall=98% - Excelente identificação de clientes bons
- Classe 1 (Inadimplente): Precision=91%, Recall=92.5% - Boa identificação de riscos

Implicações Práticas:
- O modelo é confiável para uso em produção
- Baixa taxa de falsos positivos (9%) evita penalizar clientes bons
- Alta taxa de detecção de inadimplência (92.5%) permite ações preventivas eficazes
- O balanceamento de classes funcionou adequadamente

Limitações Identificadas:
- O modelo ainda apresenta 8% de falsos negativos (inadimplentes não detectados)
- Pode ser necessário ajuste fino para otimizar ainda mais a detecção de riscos específicos

Conclusão:
O RandomForestClassifier demonstrou ser uma escolha adequada para o problema, oferecendo alta precisão e boa capacidade de generalização, sendo adequado para implementação em ambiente de produção.

### 4.4. Comparação de Modelos

#### Introdução

A seleção do modelo preditivo adequado para o problema de inadimplência da Finnet constitui uma etapa que demanda análise sistemática de múltiplas alternativas algorítmicas. Esta seção apresenta uma avaliação comparativa de modelos candidatos desenvolvidos para responder diferentes questões específicas do TAPI (Termo de Abertura de Projeto do INTELI), fundamentada em critérios técnicos objetivos e alinhada às necessidades específicas do negócio financeiro.

**Contexto dos Modelos Selecionados:**

Os modelos implementados foram projetados para atender diferentes requisitos analíticos do projeto, cada um respondendo uma pergunta específica de negócio com o algoritmo que demonstrou melhor performance:

- **Modelo 1 (Random Forest - modelo_1_%_inadimplencia.ipynb)**: Responde à pergunta "Qual % de inadimplência previsto para período?" - Selecionado entre Random Forest, XGBoost e Logistic Regression por apresentar a melhor combinação de métricas;
- **Modelo Definitivo (Consolidado - notebooks/modelo_definitivo.ipynb)**: Consolida, em um único pipeline, as quatro perguntas do TAPI; evolução do antigo `modelo_2.ipynb`;
- **Modelo 3 (Gradient Boosting - modelo-3-predicao-valores.ipynb)**: Responde à pergunta "Qual previsão de valores (R$) de recebimento dentro do período?" - Utiliza Gradient Boosting com otimização sistemática de hiperparâmetros via GridSearchCV.

Esta abordagem multi-modelo permite uma análise abrangente das capacidades preditivas de diferentes algoritmos aplicados a aspectos complementares do problema de inadimplência, fornecendo insights técnicos para a seleção da solução mais adequada às necessidades operacionais da Finnet.

A metodologia de avaliação implementada incorpora detecção sistemática de overfitting através de critérios quantitativos específicos para cada métrica, garantindo que os modelos selecionados mantenham performance consistente em dados não vistos. Esta abordagem é fundamental no contexto financeiro, onde modelos que apresentam degradação de performance em produção podem resultar em perdas significativas e comprometimento da estratégia de gestão de risco.

#### 4.4.1. Justificativa das métricas de avaliação

Para o problema de predição de inadimplência da Finnet, foram selecionadas cinco métricas fundamentais que atendem às necessidades específicas do negócio financeiro:

**Acurácia (Accuracy)**: Representa a proporção total de predições corretas sobre o conjunto de dados. No contexto de inadimplência, uma acurácia elevada indica que o modelo consegue classificar corretamente tanto clientes adimplentes quanto inadimplentes. Esta métrica foi estabelecida com critério mínimo de 80% para garantir confiabilidade operacional.

**Precisão (Precision)**: Mede a proporção de verdadeiros positivos entre todas as predições positivas. Para inadimplência, alta precisão significa que quando o modelo classifica um cliente como inadimplente, essa predição tem alta probabilidade de estar correta, reduzindo custos desnecessários de cobrança e evitando ações inadequadas contra clientes adimplentes.

**Recall (Sensibilidade)**: Quantifica a capacidade do modelo de identificar todos os casos de inadimplência real. Esta métrica é crítica para a Finnet, pois falsos negativos (inadimplentes não detectados) resultam em perdas financeiras diretas. Um recall elevado garante que a maioria dos casos de risco seja identificada preventivamente.

**F1-Score**: Representa a média harmônica entre precisão e recall, fornecendo uma métrica balanceada especialmente importante em datasets com classes desbalanceadas. No contexto financeiro, o F1-Score otimiza simultaneamente a detecção de inadimplentes e a redução de falsos alarmes.

**AUC-ROC (Area Under the Curve - Receiver Operating Characteristic)**: Avalia a capacidade discriminativa do modelo em diferentes thresholds de classificação. Para problemas de crédito, o AUC-ROC permite ajustar o ponto de corte conforme a estratégia de risco da instituição, sendo fundamental para calibração operacional do modelo.

#### 4.4.2. Modelos selecionados avaliados

Foram implementados e avaliados três modelos de aprendizado de máquina selecionados por apresentarem a melhor performance para suas respectivas questões de negócio do TAPI:

**Modelo 1: Random Forest Classifier (Classificação de Inadimplência)**

O Random Forest foi selecionado como algoritmo principal para predição de inadimplência por demonstrar superioridade entre os algoritmos testados (Random Forest, XGBoost, Logistic Regression) no notebook modelo_1_%_inadimplencia.ipynb. Este algoritmo ensemble baseado em árvores de decisão oferece robustez contra overfitting e capacidade de lidar com features heterogêneas. A configuração implementada utilizou parâmetros conservadores para maximizar a generalização:

**Configuração de Hiperparâmetros:**
- `n_estimators=100`: Número moderado de árvores para equilibrar performance e custo computacional
- `max_depth=20`: Limitação de profundidade para prevenir overfitting
- `min_samples_split=5`: Controle de divisões mínimas para regularização
- `min_samples_leaf=2`: Restrição de amostras por folha para estabilidade
- `random_state=42`: Garantia de reprodutibilidade dos resultados

**Métricas Alcançadas:**
- Acurácia: 99.74%
- Precisão: 98.84%
- Recall: 99.77%
- F1-Score: 99.30%
- AUC-ROC: 100.00%

**Modelo Definitivo: Random Forest Consolidado (notebooks/modelo_definitivo.ipynb)**

Consolida em um único notebook as respostas às quatro perguntas do TAPI, sendo a evolução direta do antigo `modelo_2.ipynb`.

**Configuração de Hiperparâmetros:**
- `n_estimators=300`
- `max_depth=35`
- `min_samples_leaf=4`
- `class_weight='balanced'`
- `oob_score=True`
- `n_jobs=-1`
- `random_state=42`

**Configuração Ótima Encontrada (RandomizedSearchCV, 3-fold, 10 iterações):**
- `n_estimators=373`
- `max_depth=16`
- `min_samples_split=8`
- `min_samples_leaf=2`
- `max_features='sqrt'`
- Acurácia média (CV): 94.71%

**Métricas Alcançadas (validação temporal - teste):**
- Acurácia no Conjunto de Teste: 94.28%
- Acurácia OOB: 95.86%
- Recall (classe Inadimplente): 80.12%
- Precisão (classe Inadimplente): 85%
- F1-Score (classe Inadimplente): 82%

> Decisão do grupo: os notebooks `modelo_1_%_inadimplencia.ipynb`, `modelo_2.ipynb` e `modelo-3-predicao-valores.ipynb` foram mantidos apenas na subpasta "notebooks antigos" dentro de "notebooks". Nesta documentação, permanecem as métricas do Modelo 1 e do Modelo 3 apenas para comparação com o `modelo_definitivo.ipynb`.

**Modelo 3: Gradient Boosting Classifier (Predição de Valores)**

O Gradient Boosting foi selecionado para predição de valores de recebimento no notebook modelo-3-predicao-valores.ipynb por sua capacidade superior de modelar relações não-lineares complexas. O modelo foi otimizado através de GridSearchCV, avaliando 48 combinações de hiperparâmetros com validação cruzada de 3 folds:

**Espaço de Busca GridSearchCV:**
- `learning_rate`: [0.05, 0.1] - Taxa de aprendizado para convergência
- `max_depth`: [2, 3, 5] - Profundidade máxima das árvores
- `n_estimators`: [100, 200] - Número de estimadores sequenciais
- `min_samples_leaf`: [10, 50] - Amostras mínimas por folha
- `min_samples_split`: [10] - Amostras mínimas para divisão
- `max_features`: ['sqrt'] - Número de features consideradas
- `subsample`: [0.8, 1.0] - Fração de amostras para treinamento

**Configuração Ótima Encontrada:**
- `learning_rate=0.1`: Taxa de aprendizado otimizada para convergência eficiente
- `max_depth=5`: Profundidade máxima das árvores para complexidade adequada
- `n_estimators=200`: Número ótimo de estimadores para performance máxima
- `min_samples_leaf=50`: Regularização por tamanho mínimo de folha
- `min_samples_split=10`: Controle de divisões mínimas para estabilidade
- `max_features='sqrt'`: Seleção de features por árvore para diversidade
- `subsample=1.0`: Utilização completa dos dados para máxima informação

**Métricas Alcançadas:**
- Acurácia: 96.19%
- Precisão: 97.43%
- Recall: 93.92%
- F1-Score: 95.64%

#### 4.4.3. Análise comparativa de performance

A análise comparativa dos três modelos selecionados revela diferenças em termos de capacidade preditiva e adequação aos respectivos problemas de negócio:

**Comparação por Questão de Negócio:**

**Modelo 1 (Classificação de Inadimplência - Random Forest):**
- Acurácia: 99.74%, Precisão: 98.84%, Recall: 99.77%, F1-Score: 99.30%
- Desempenho excepcional para detecção de inadimplência com equilíbrio ótimo entre precisão e recall

**Modelo Definitivo (Consolidado - Random Forest):**
- Acurácia: 94.28%, Acurácia OOB: 95.86%, Recall para Inadimplente: 80.12%
- Performance muito boa para classificação multiclasse com tratamento adequado de classes desbalanceadas

**Modelo 3 (Predição de Valores - Gradient Boosting):**
- Acurácia: 96.19%, Precisão: 97.43%, Recall: 93.92%, F1-Score: 95.64%
- Excelente capacidade de modelagem de relações não-lineares para predição de valores financeiros

**Análise de adequação específica:**

O Random Forest para classificação de inadimplência demonstrou superioridade excepcional, alcançando recall de 99.77% que garante detecção de praticamente todos os casos de inadimplência real, minimizando perdas financeiras. A precisão de 98.84% assegura controle eficaz de falsos positivos, evitando custos operacionais desnecessários.

O Modelo Definitivo (Random Forest consolidado) apresenta configuração específica para dados desbalanceados, com recall de 80.12% para inadimplentes representando performance adequada para classificação multiclasse complexa. A utilização de class_weight='balanced' e OOB score demonstra abordagem técnica apropriada.

O Gradient Boosting para predição de valores beneficia-se da otimização sistemática via GridSearchCV, resultando em modelo com capacidade superior de captura de padrões não-lineares. O F1-Score de 95.64% indica equilíbrio adequado para aplicações de regressão classificatória.

#### 4.4.4. Seleção do Modelo Final

Com base na análise comparativa e na consolidação das funcionalidades, o modelo final selecionado é o notebook `notebooks/modelo_definitivo.ipynb` (Random Forest consolidado), fundamentado nos seguintes critérios:

**Critérios de Seleção:**
- Cobertura integral das quatro perguntas do TAPI em um único pipeline;
- Desempenho consistente em validação temporal: Acurácia 94.28% (teste), Recall 80.12% para inadimplentes e OOB 95.86%;
- Robustez e reprodutibilidade (random_state fixo, class_weight='balanced', OOB);
- Simplicidade operacional e manutenção centralizada do fluxo.

**Decisão do Grupo e Organização dos Artefatos:**
Por decisão do grupo responsável pelo projeto, os notebooks intermediários foram mantidos apenas para histórico na subpasta `notebooks/notebooks antigos`. Nesta documentação, permanecem como baseline comparativo as métricas do Modelo 1 (`modelo_1_%_inadimplencia.ipynb`) e do Modelo 3 (`modelo-3-predicao-valores.ipynb`) frente ao `modelo_definitivo.ipynb`.

**Conclusão:**
O `modelo_definitivo.ipynb` foi adotado como solução final consolidada. Os demais notebooks permanecem apenas como referências históricas, e suas métricas (Modelos 1 e 3) são mantidas aqui para comparação objetiva com o modelo definitivo.

A abordagem multi-modelo desenvolvida estabelece uma base metodológica sólida para projetos futuros, demonstrando que diferentes questões de negócio requerem soluções algorítmicas específicas e adequadamente otimizadas.

### 4.5. Avaliação

&nbsp;&nbsp;&nbsp;&nbsp;A solução final desenvolvida consistiu em um modelo de classificação supervisionada baseado no algoritmo `Random Forest Classifier`, integrado ao pipeline de análise da plataforma Luna, da Finnet. A escolha deste modelo foi motivada por seu desempenho robusto em dados tabulares, sua capacidade de generalização e interpretabilidade relativa. Essas características são essenciais em um ambiente corporativo que demanda previsões confiáveis e explicáveis.

&nbsp;&nbsp;&nbsp;&nbsp;Durante o processo iterativo de desenvolvimento, o modelo passou por extensas etapas de feature engineering, balanceamento de classes e otimização de hiperparâmetros por meio de `GridSearchCV`, alcançando resultados consistentes. A acurácia média atingiu 94 %, conforme os critérios de sucesso definidos anteriormente (seção 4.1.3), com recall e precision otimizados para a classe de maior interesse: inadimplentes.

&nbsp;&nbsp;&nbsp;&nbsp;O modelo foi projetado para classificar cada título em três categorias – Em Dia, Atrasado ou Inadimplente – fornecendo também um score probabilístico de risco que auxilia o gestor financeiro na priorização de clientes. Essa camada de inteligência transforma o processo de cobrança da Finnet de reativo para preditivo, permitindo decisões antecipadas e estratégias personalizadas de mitigação.



#### Alinhamento com o Negócio e com as Personas

&nbsp;&nbsp;&nbsp;&nbsp;Conforme exposto na Seção 4.1, a inadimplência corporativa representa um risco macroeconômico relevante e afeta diretamente o fluxo de caixa de empresas B2B. O modelo responde a essa dor de negócio ao oferecer uma ferramenta de previsão integrada à Luna, possibilitando ao usuário identificar clientes de risco antes do vencimento e ajustar estratégias de cobrança de forma proativa.  

&nbsp;&nbsp;&nbsp;&nbsp;Sob a ótica das personas:  
- Cecília (Head de Negócios) passa a ter métricas explicáveis e conformes à LGPD para apresentação a stakeholders e diretoria.  
- David (Analista de Dados) encontra um modelo transparente e modular. Sendo facilmente re-treinável dentro da plataforma Luna.  
- Alice e Marcelo (usuários finais da plataforma) ganham ferramentas visuais para analisar riscos de pagamento e prever fluxos de receita com maior segurança.  

&nbsp;&nbsp;&nbsp;&nbsp;Dessa forma, a solução atende diretamente aos requisitos do negócio e às expectativas dos usuários, alinhando valor tecnológico e estratégico.


#### Plano de Contingência

&nbsp;&nbsp;&nbsp;&nbsp;Considerando a criticidade do uso de modelos preditivos em ambiente corporativo, foi elaborado um plano de contingência para eventuais falhas nas predições ou mudanças no padrão dos dados (model drift):

1. Monitoramento contínuo: Acurácia, recall e AUC-ROC serão avaliados mensalmente.  
2. Retreinamento programado: Atualização trimestral com novos dados transacionais da Finnet para manter a relevância do modelo.  
3. Fallback model: Regressão logística simplificada como modelo de backup para situações de falha do Random Forest.  
4. Alertas de desvio: Detecção automática de variações significativas nas predições em relação a valores históricos.  
5. Logs e auditoria: Registro das predições para rastreabilidade e diagnóstico rápido de anomalias.  


#### Explicabilidade do Modelo

&nbsp;&nbsp;&nbsp;&nbsp;Para garantir a transparência do modelo e facilitar a adoção pelos usuários, foram implementadas técnicas de explicabilidade utilizando SHAP (SHapley Additive exPlanations):  

- As variáveis de maior impacto nas predições foram: `valor_original`, `dias_ate_vencimento`, `qtde_acessos_pagador` e `histórico_de_pagamentos`.  
- Gráficos de importância e explicações locais foram incluídos no dashboard para tornar as decisões do modelo inteligíveis para gestores e analistas.  
 


#### Verificação de Hipóteses

| Hipótese | Situação | Evidência |
|-----------|-----------|-----------|
| H1 – O modelo é capaz de prever inadimplência com acurácia > 80 %. | Aceita | Acurácia = 94 % em dados de teste. |
| H2 – O modelo melhora a eficiência operacional dos usuários. | Aceita | Redução do tempo de análise manual em ≈ 60 %. |
| H3 – As predições são explicáveis e compreensíveis para usuários não técnicos. | Aceita | Visualizações SHAP integradas à Luna e feedback positivo de teste de usuários. |
| H4 – O modelo mantém desempenho em novos cenários de dados. | Em validação | Planejado monitoramento contínuo e re-treinamento trimestral. |


#### Conclusão

&nbsp;&nbsp;&nbsp;&nbsp;A solução preditiva FinSight atende plenamente aos requisitos de negócio da Finnet ao transformar a gestão de recebíveis em um processo baseado em dados. O modelo Random Forest demonstrou alta performance e robustez, sendo tecnicamente adequado e estrategicamente alinhado ao objetivo de reduzir inadimplência e aumentar a confiança dos clientes.

## <a name="c5"></a>5. Conclusões e Recomendações
```
Escreva, de forma resumida, sobre os principais resultados do seu projeto e faça recomendações formais ao seu parceiro de negócios em relação ao uso desse modelo. Você pode aproveitar este espaço para comentar sobre possíveis materiais extras, como um manual de usuário mais detalhado na seção “Anexos”. Não se esqueça também das pessoas que serão potencialmente afetadas pelas decisões do modelo preditivo e elabore recomendações que ajudem seu parceiro a tratá-las de maneira estratégica e ética. 

Remova este bloco ao final
```

## <a name="c6"></a>6. Referências

AGÊNCIA BRASIL. Pix foi o meio de pagamento mais popular do Brasil em 2023. Brasília, DF: EBC, 2024. Disponível em: https://agenciabrasil.ebc.com.br/economia/noticia/2024-03/pix-foi-o-meio-de-pagamento-mais-popular-do-brasil-em-2023. Acesso em: 10 agosto 2025. 

ALI, Rami. 7 predictive analytics challenges and how to troubleshoot them. Oracle NetSuite, 19 fev. 2025. Disponível em: https://www.netsuite.com/portal/resource/articles/financial-management/predictive-analytics-challenges.shtml. Acesso em: 6 ago. 2025.

AWARE. BC publica estatísticas de varejo e de cartões no Brasil. Aware Gestão, 2022. Disponível em: https://www.awaregestao.com/en/noticia/bc-publica-estatisticas-de-varejo-e-de-cartoes-no-brasil/. Acesso em: 10 agosto 2025. 

BRASIL 61. Serasa: mais de 31% das empresas do país começaram o ano endividadas. Brasil 61, 2025. Disponível em: https://brasil61.com/n/serasa-mais-de-31-das-empresas-do-pais-comecaram-o-ano-endividadas-bras2513405. Acesso em: 08 agosto 2025. 

CUNHA, Ana Raquel Fernandes. Desafios de modelos de ciência de dados. Medium, 31 out. 2024. Disponível em: https://medium.com/@anaraquel.fiap/desafios-de-modelos-de-ci%C3%AAncia-de-dados-775d5c6019db. Acesso em: 6 ago. 2025.

DISTRITO. Panorama do mercado de fintechs na América Latina em 2025. Distrito, 2025. Disponível em: https://distrito.me/blog/panorama-do-mercado-de-fintechs-na-america-latina-em-2025/. Acesso em: 10 agosto 2025. 

FEBRABAN. FEBRABAN recebe com otimismo medidas para aperfeiçoar marco legal de garantias. Portal Febraban, 2021. Disponível em: https://portal.febraban.org.br/noticia/3717/en-us. Acesso em: 08 de agosto 2025. 

FINNET. Finnet: Conectando grandes empresas ao futuro financeiro. 2024. Disponível em: https://finnet.com.br/. Acesso em: 08 de agosto 2025. 
FINNET. TAPI - Termo de Abertura de Projeto INTELI. Documento fornecido pela empresa. São Paulo, 2025. 
FINNET. Finnet: Finnet lança plataforma de cobranças e recebimentos que permite utilizar taxas já negociadas com os bancos. 2022. Disponível em: https://tiinside.com.br/06/10/2022/finnet-lanca-plataforma-de-cobrancas-e-recebimentos-que-permite-utilizar-taxas-ja-negociadas-com-os-bancos/. Acesso em: 28 de agosto 2025.
FINNET. Lançamento do Luna. 2025. Disponível em: https://finnet.com.br/conteudo-de-lancamento-luna-2/. Acesso em: 28 de agosto 2025.

FINSIDERS. Accesstage aposta na iniciação de pagamento para crescer seu ecossistema B2B. Finsiders, 2024. Disponível em: https://finsidersbrasil.com.br/reportagem-exclusiva-fintechs/accesstage-aposta-na-iniciacao-de-pagamento-para-crescer-seu-ecossistema-b2b/. Acesso em: 10 de agosto 2025. 

FINSIDERS. Fintechs recorrem cada vez mais à IA para mitigar riscos e avançar em crédito. Finsiders, 2025. Disponível em: https://finsidersbrasil.com.br/ia/fintechs-recorrem-cada-vez-mais-a-ia-para-mitigar-riscos-e-avancar-em-credito/. Acesso em: 10 de agosto 2025. 

FINSIDERS. Pix encosta nos cartões e bate 39% dos pagamentos em 2023, diz BC. Finsiders, 2024. Disponível em: https://finsidersbrasil.com.br/estudos-e-relatorios/pix-encosta-nos-cartoes-e-bate-39-dos-pagamentos-em-2023-diz-bc/. Acesso em: 08 de agosto 2025. 
INFOMONEY. Cada vez mais digitais, boletos movimentaram mais de R$ 6 tri no 1º semestre de 2024. Infomoney, 2024. Disponível em: https://www.infomoney.com.br/minhas-financas/cada-vez-mais-digitais-boletos-movimentaram-mais-de-r-6-tri-no-1o-semestre-de-2024/. Acesso em: 10 de agosto 2025. 
INTELI. Como é o primeiro ano dos alunos do Inteli. Inteli, 2025. Disponível em: https://www.inteli.edu.br/como-e-o-primeiro-ano-dos-alunos-no-inteli/. Acesso em: 28 de agosto 2025.

NUBANK. Inteligência Artificial aplicada a serviços financeiros. Building Nubank, 2022. Disponível em: https://building.nubank.com.br/pt-br/inteligencia-artificial-aplicada-a-servicos-financeiros/. Acesso em: 08 de agosto 2025. 

OAB CAMPINAS. LGPD e o impacto no setor bancário e financeiro. OAB Campinas, [s.d.]. Disponível em: https://oabcampinas.org.br/lgpd-e-o-impacto-no-setor-bancario-e-financeiro/. Acesso em: 10 de agosto 2025. 

O2OBOTS. Recuperação de crédito com IA no setor financeiro. O2OBOTS, 2025. Disponível em: https://www.o2obots.com/blog/recuperacao-de-credito-com-ia-no-setor-financeiro. Acesso em: 10 de agosto 2025. 
OKAI. LGPD: Impactos na economia e na governança corporativa. Okai, 2023. Disponível em: https://okai.com.br/blog/lgpd-impactos-na-economia-e-na-governanca-corporativa. Acesso em: 08 de agosto 2025. 

PORTO, P. C. et al. A ascensão das fintechs no Brasil: evidências a partir de dados de alta frequência. Texto para Discussão, n. 001, Instituto de Economia da UFRJ, 2024. Disponível em: https://www.ie.ufrj.br/images/IE/TDS/2024/TD_IE_001_2024_PORTO_MONTANI_BONATTI_ALBUQUERQUE_FERREIRA.pdf. Acesso em: 10 de agosto 2025. 

SERASA EXPERIAN. Ano de 2024 fecha com 6,9 milhões de empresas inadimplentes, revela Serasa Experian. Sala de Imprensa, 2025. Disponível em: https://www.serasaexperian.com.br/sala-de-imprensa/indicadores/ano-de-2024-fecha-com-69-milhoes-de-empresas-inadimplentes-revela-serasa-experian/. Acesso em: 08 de agosto 2025. 

TIINSIDE. Proteção de dados e governança: o papel da LGPD no setor financeiro. TI INSIDE, 2024. Disponível em: https://tiinside.com.br/24/10/2024/protecao-de-dados-e-governanca-o-papel-da-lgpd-no-setor-financeiro/. Acesso em: 10 de agosto 2025. 

BRASIL. Banco Central do Brasil. Resolução BCB Nº 80, de 25 de março de 2021. Disponível em: https://www.bcb.gov.br/estabilidadefinanceira/exibenormativo?tipo=Resolu%C3%A7%C3%A3o%20BCB&numero=80. Acesso em: 4 ago. 2025.

BRASIL. Banco Central do Brasil. Resolução BCB Nº 81, de 25 de março de 2021. Disponível em: https://www.bcb.gov.br/estabilidadefinanceira/exibenormativo?tipo=Resolu%C3%A7%C3%A3o%20BCB&numero=81. Acesso em: 4 ago. 2025.

BANCO CENTRAL DO BRASIL. Open Finance. Brasília, DF: Banco Central do Brasil, c2025. Disponível em: https://www.bcb.gov.br/estabilidadefinanceira/openfinance. Acesso em: 5 ago. 2025.
OPEN FINANCE BRASIL. Open Finance Brasil., c2025. Disponível em: https://openfinancebrasil.org.br/. Acesso em: 5 ago. 2025.

PWC; ABFINTECHS. Pesquisa Fintech Deep Dive 2024.: PwC, 2024. Disponível em: https://www.pwc.com.br/pt/estudos/setores-atividade/financeiro/2024/pesquisa-fintech-deep-dive-2024.html. Acesso em: 5 ago. 2025.

PWC; ABFINTECHS. The Fintech Deep Dive Survey 2023.: PwC, 2023. Disponível em: https://abfintechs.com.br/wp-content/uploads/2024/04/Pesq_Fintech_Deep_Dive_EN_2023-VF-30-10-1.pdf. Acesso em: 5 ago. 2025.
DISTRITO. FinTech Report 2024. São Paulo: Distrito, 2024. Disponível em: https://materiais.distrito.me/report/fintech-report-2024. Acesso em: 6 ago. 2025.

DISTRITO. Distrito FinTech Report 2023. São Paulo: Distrito, 2023. Disponível em: https://www.helmigroup.com/insights/brazils-fintech-landscape-key-takeaways-from-the-distrito-2023-report. Acesso em: 4 ago. 2025.

KPMG. Pulse of Fintech H2'24.: KPMG, 2025. Disponível em: https://assets.kpmg.com/content/dam/kpmg/be/pdf/BA-Pulse-of-Fintech-H2-2024-2025.pdf. Acesso em: 4 ago. 2025.

GRAND VIEW RESEARCH. Brazil ERP Software Market Size & Outlook, 2024-2030. San Francisco, CA: Grand View Research, 2024. Disponível em: https://www.grandviewresearch.com/horizon/outlook/erp-software-market/brazil. Acesso em: 5 ago. 2025.

MARI, Angelica. Oracle's ERP market share shrinks in Brazil. ZDNet, 26 maio 2021. Disponível em: https://www.zdnet.com/article/oracles-erp-market-share-shrinks-in-brazil/. Acesso em: 6 ago. 2025.

STARK BANK. API | STARK BANK Documentation. São Paulo: Stark Bank, c2025. Disponível em: https://starkbank.com/docs/api. Acesso em: 5 ago. 2025.

TOTVS. Lançamento de novo produto da TOTVS Techfin. São Paulo: TOTVS RI, c2021. Disponível em: https://ri.totvs.com/lancamento-de-novo-produto-totvs-techfin/. Acesso em: 6 ago. 2025.

CELCOIN. Banking as a Service (BaaS): TED & Pix Refund. Barueri, SP: Celcoin, c2025. Disponível em: https://www.celcoin.com.br/news/baas-ted-solutions-pix-refund-celcoin/. Acesso em: 6 ago. 2025.

NEOGRID. Accesstage e Neogrid anunciam parceria para impulsionar a produtividade da área financeira das empresas. São Paulo: Neogrid, 18 jun. 2024. Disponível em: https://neogrid.com/noticias/accesstage-e-neogrid-anunciam-parceria-para-impulsionar-a-produtividade-da-area-financeira-das-empresas/. Acesso em: 6 ago. 2025.

SAP. SAP S/4HANA Cloud para finanças centrais. Walldorf, DE: SAP, c2025. Disponível em: https://www.sap.com/brazil/products/financial-management/central-finance.html. Acesso em: 6 ago. 2025.

ORACLE. Oracle Fusion Cloud ERP. Austin, TX: Oracle, c2025. Disponível em: https://www.oracle.com/br/erp/. Acesso em: 6 ago. 2025.

FIELD, A. Descobrindo a Estatística Usando o SPSS. 2. ed. Porto Alegre: Penso, 2013.

GRUS, J. Data Science do Zero: Primeiras Regras com Python. Rio de Janeiro: Alta Books, 2019.

HAN, J.; PEI, J.; KAMBER, M. Data Mining: Concepts and Techniques. 3. ed. Waltham: Morgan Kaufmann, 2012.

LILLIEFORS, H. W. On the Kolmogorov-Smirnov test for normality with mean and variance unknown. Journal of the American Statistical Association, v. 62, n. 318, p. 399-402, 1967.

MÜLLER, A. C.; GUIDO, S. Introdução ao Machine Learning com Python: Um Guia para Cientistas de Dados. São Paulo: Novatec Editora, 2017.

MONTGOMERY, Douglas C.; RUNGER, George C. Applied Statistics and Probability for Engineers. 6. ed. New Jersey: Wiley, 2014.

MCKINNEY, W. Python para Análise de Dados: Tratamento de Dados com Pandas, NumPy e IPython. 2. ed. São Paulo: Novatec Editora, 2018.

PROVOST, F.; FAWCETT, T. Data Science para Negócios: O que você precisa saber sobre mineração de dados e pensamento analítico de dados. Rio de Janeiro: Alta Books, 2013.

# <a name="attachments"></a>Anexos

## Introdução

A análise da distribuição das variáveis quantitativas é uma etapa fundamental em projetos de modelagem preditiva, pois fornece informações estatísticas importantes para a preparação dos dados e para a escolha adequada de técnicas de pré-processamento. Muitos métodos estatísticos e algoritmos de aprendizado de máquina partem do pressuposto de que os dados seguem distribuições específicas, sendo a normal (gaussiana) a mais comum. Caso essa verificação não seja realizada, há o risco de introduzir vieses, reduzir a precisão dos modelos e comprometer a confiabilidade das conclusões.

No contexto do projeto desenvolvido em parceria com a Finnet, seram analisadas s seguir três variáveis centrais do dataset: **vl_boleto**, **vl_pagto** e **qtd_acessos_pagador**. Essas variáveis estão diretamente relacionadas ao comportamento financeiro dos clientes e, portanto, são determinantes para o desempenho do modelo de previsão de inadimplência. Para essa análise, formulamos hipóteses estatísticas e aplicamos o **teste de Lilliefors (1967)**, adequado quando média e desvio padrão da população são desconhecidos e precisam ser estimados a partir da amostra. Além dos testes formais, utilizamos **histogramas** e a comparação entre medidas de tendência central, como média e mediana, como formas complementares de interpretação. Esse cruzamento entre análises estatísticas e visuais enriquece a compreensão da estrutura dos dados e aumenta a confiabilidade das conclusões.

Ademais, outro ponto central dessa subseção é o **escalonamento das variáveis**, uma vez que atributos em escalas muito diferentes podem distorcer algoritmos sensíveis à magnitude dos dados, como KNN, regressão logística ou redes neurais. Com base nos resultados do teste de normalidade, optou-se pela **normalização Min-Max**, que transforma as variáveis para o intervalo [0,1]. Essa escolha se justifica porque, ao contrário da padronização, a normalização não parte do pressuposto de distribuição normal e garante que todos os atributos contribuam de forma equitativa para o modelo conforme presente na literatura (Han; Pei; Kamber, 2012).

Dessa forma, esta subseção documenta e fundamentada o processo de análise estatística e pré-processamento dos dados das três variáveis quantitativas citadas acima que estão presentes no dataset fornecido pela Finnet entitulado como **Grupo com vencimento 07-12 2024 - GF**. A validação da distribuição das variáveis, a aplicação de testes formais, a interpretação gráfica dos resultados e a decisão metodológica sobre o escalonamento asseguram não apenas a reprodutibilidade do trabalho, mas também o rigor ciêntifico que fundamenta a confiabilidade do modelo preditivo desenvolvido. Em última instância, esse rigor metodológico estabelece bases para que as análises e previsões realizadas possam ser aplicadas com segurança em cenários reais da Finnet, reforçando a confiabilidade e a aplicabilidade do projeto.

---

## 1. Distribuição normal e teste de hipóteses

---

### 1.1. Definição de hipóteses 
Nesta seção, serão estabelecidas as hipóteses estatísticas que orientam a análise de normalidade das variáveis quantitativas do conjunto de dados. O objetivo central é verificar se as distribuições dessas variáveis podem ser consideradas normais, uma vez que esse é um pressuposto fundamental em diversos métodos estatísticos e modelos matemáticos.

A formulação de hipóteses segue a lógica de definir uma hipótese nula (H₀), que assume que os dados seguem uma distribuição normal, e uma hipótese alternativa (H₁), que assume que os dados não seguem essa distribuição. Essa etapa é essencial, pois permite aplicar testes estatísticos formais — neste caso, o teste de Lilliefors — para avaliar, com base em evidências empíricas, se há suporte para a normalidade ou se ela deve ser rejeitada.

Além disso, a definição de hipóteses serve como ponto de partida para as demais análises desenvolvidas neste trabalho. Após a aplicação dos testes de normalidade, os resultados serão comparados com análises gráficas (histogramas) e com medidas de tendência central (média e mediana), de modo a enriquecer a interpretação. Com isso, busca-se não apenas aplicar os testes estatísticos de forma mecânica, mas compreender em profundidade o comportamento das variáveis e suas implicações para as análises subsequentes.

##### Validação das Hipóteses

Para validar as hipóteses formuladas, utilizamos o valor de **p-value**, que representa a probabilidade de observar os dados coletados (ou algo ainda mais extremo), considerando que a hipótese nula (H₀) seja verdadeira. Em termos práticos, o p-value indica o grau de compatibilidade dos dados com a hipótese de normalidade.  

Neste trabalho, o cálculo do p-value é realizado por meio do **teste de Lilliefors**, aplicado às variáveis quantitativas selecionadas.  

Adotamos um nível de significância **α = 0,05 (5%)**, que estabelece o critério de decisão para aceitar ou rejeitar H₀:  

- **Se p-value > 0,05** → não rejeitamos H₀, ou seja, não existem evidências suficientes para descartar a normalidade.  
- **Se p-value ≤ 0,05** → rejeitamos H₀, concluindo que os dados não seguem uma distribuição normal.  

##### Hipótese 1: <br>
H₀: A variável *vl_boleto* (valor do boleto) segue a distribuição normal 
H₁: A variável *vl_boleto* (valor do boleto) não segue a distribuição normal 


``` python

# Calculando p_value da hipótese 1 
stat, p_value = lilliefors(df['vl_boleto'])
print("o valor de p_value é:", p_value)

```

O *p_value* referente a distribuiçã normal da variável *vl_boleto* é de 0.00099999. Logo *p_value* é menor do que o nível de significância 0.005 e por isso a hipótese H₁ (A variável *vl_boleto* não segue a distribuição normal), é a correta.

##### Hipótese 2: <br>
H₀: A variável  *vl_pagto* (valor do pagamento) segue a distribuição normal 
H₁: A variável *vl_pagto* (valor do pagamento) não segue a distribuição normal 


``` python

# Calculando p_value da hipótese 2
df['vl_pagto'] = df['vl_pagto'].replace('\\N', np.nan)
stat, p_value1 = lilliefors(df['vl_pagto'].dropna().astype(float))
print("o valor de p_value é:", p_value1)

```
*p_value* = 0.0009999999999998899

 *p_value* < 0,005 : Não segue a distribuição normal (Hipótese H₁).

##### Hipótese 3: <br>
H₀: A variável  qtd_acessos_pagador (quantidade de acessos do pagador) segue a distribuição normal
H₁: A variável qtd_acessos_pagador não segue a distribuição normal


``` python

# calculando p_value da hipóese 3
df['qtd_acessos_pagador'] = df['qtd_acessos_pagador'].replace('\\N', np.nan)
stat, p_value1 = lilliefors(df['qtd_acessos_pagador'].dropna().astype(float))
print("o valor de p_value é:", p_value1)

```

o valor de *p_value* = 0.0009999999999998899
 *p_value* < 0,005 : Não segue a distribuição normalc(Hipótese H₁)

---

## 1.2. Construção de histograma das variaveis

#### Valor do boleto *(vl_boleto)*

```python

df['vl_boleto'].plot(kind='hist', bins=40, figsize=(5, 3))
media_boleto = df['vl_boleto'].mean()
print("Média do valor do boleto:", media_boleto)
mediana_boleto = df['vl_boleto'].median()
print("Mediana do valor do boleto:", mediana_boleto)

```
Média do valor do boleto: 303.65
Mediana do valor do boleto: 305.17

<div align="center">
<sub>Figura XX: Gráfico da distribuição da variável vl_boleto.</sub>
</div>
<div align="center">
<img src="https://plum-atomic-lemur-391.mypinata.cloud/ipfs/bafkreiclotajd6vaep4sbhdfj3sw7ecwkdjracofprt3u2bo3qn64mbyua" alt="Histograma 1" width="500px">

<sub>Fonte: Material produzido pela equipe utilizando a biblioteca de python matplotlib, 2025.</sub>

</div>


O valor da média (303,65) e da mediana (305,17) da variável de valor do boleto (vl_pagto) são que sugere uma distribuição que se aproxima da normalidade, o que é visível no gráfco em que a distribuição de valores aparenta seguir uma simetria. No entanto, após a  aplicação do teste de normalidade, utilizando a biblioteca lilliefors, calculou-se  que a distribuição da variável não é normal. Isso ocorre pois em amostras grandes pequenos desvios de normalidade são dectectados pelo teste, mesmo que isso não sejá visível a olho.

---

#### Valor do pagamento *(vl_pagto)*

```python

df['vl_pagto'] = pd.to_numeric(df['vl_pagto'], errors='coerce')
df['vl_pagto'].plot(kind='hist', bins=40, figsize=(5, 3))
media_pagto = df['vl_pagto'].mean()
print("Média do valor do pagamento:", media_pagto)
mediana_pagto = df['vl_pagto'].median()
print("Mediana do valor do pagamento:", mediana_pagto)

```
Média do valor do pagamento: 300.16
Mediana do valor do pagamento: 300.90


<div align="center">
<sub>Figura XX: Gráfico da distribuição da variável vl_pagto.</sub>
</div>
<div align = "center">
<sub></sub>
<img src="https://plum-atomic-lemur-391.mypinata.cloud/ipfs/bafkreihanpoily26qnbpmkxjlfhl57ouikvjjovaboxip3xavtpcztahhy" alt="Histograma 1" width="500px" >

<sub>Fonte: Material produzido pela equipe utilizando a biblioteca de python matplotlib, 2025.</sub>
</div>

O valor da média (300,17) e da mediana (300,9) da variável de valor de pagamento (vl_pagto) são bem próximos o que sugere uma distribuição simétrica que se aproxima da normalidade, o que é visível no histograma da variável. No entanto, após a aplicação do teste de normalidade, utilizando a biblioteca lilliefors, calculou-se que a distribuição da variável não é normal.

---

#### Valor do boleto *(vl_boleto)*

```python

df['qtd_acessos_pagador'] = pd.to_numeric(df['qtd_acessos_pagador'], errors='coerce')
qtd_acessos_pagador_mean = df['qtd_acessos_pagador'].mean()
qtd_acessos_pagador_median = df['qtd_acessos_pagador'].median()
print("Média da quantidade de acessos dos pagadores:", qtd_acessos_pagador_mean)
print("Mediana da quantidade de acessos dos pagadores:", qtd_acessos_pagador_median)
df['qtd_acessos_pagador'].plot(kind='hist', bins=30, figsize=(5, 3))

```
Média da quantidade de acessos dos pagadores: 3.19
Mediana da quantidade de acessos dos pagadores: 2.00

<div align="center">
<sub>Figura XX: Gráfico da distribuição da variável qtd_acessos_pagador.</sub>
</div>
<div align="center">
<img src="https://plum-atomic-lemur-391.mypinata.cloud/ipfs/bafkreifiyklavej6gyfsw5tquzetb7avsajrl42ldvmfgflq3z7q3ljwti" alt="Histograma 1" width="500px">

<sub>Fonte: Material produzido pela equipe utilizando a biblioteca de python matplotlib, 2025.</sub>
</div>

A média (3,19) e mediana (2,0) da variável que representa a quantidade de acessos do pagador (qtd_acessos_pagador) possuem valores consideravelmente distantes sugerindo uma distribuição não normal, que é também visiível no gráfico da variável e comprovado pelo teste de normalidade que foi utilizado utilizando a biblioteca lilliefors.

---

## 2. Escalonamento de variáveis quantitativas

---

## 2.1. Definição do Tipo de Escalonamento para as Variáveis Quantitativas

### Introdução
No contexto do desenvolvimento de modelos preditivos, a etapa de pré-processamento de dados é fundamental para a performance e a confiabilidade do resultado final de um modelo. Conforme é documentado na literatura de ciência de dados, a grande maioria dos algoritmos de aprendizado de máquina não interpreta o significado semântico das variáveis, tratando-as apenas como valores numéricos (MÜLLER; GUIDO, 2017).  

Dentro deste processo, o escalonamento de variáveis quantitativas é considerada como uma técnica indispensável, cuja omissão pode introduzir vieses e levar a conclusões equivocadas. Algoritmos que se baseiam em medidas de distância, como o **K-Nearest Neighbors (KNN)**, ou que utilizam métodos de otimização por gradiente descendente, como a **regressão logística** e as **redes neurais**, são particularmente sensíveis às magnitudes das variáveis de entrada.  

A existência de escalas diferentes entre os atributos — por exemplo, uma variável representando valores monetários na casa dos milhões e outra representando uma contagem de acessos na casa das dezenas — pode fazer com que a variável de maior magnitude domine a função de custo do modelo, diminuindo a contribuição das demais variáveis (GRUS, 2019).  

O objetivo desta seção é, portanto, determinar e justificar, por meio de uma análise estatística, a técnica de escalonamento mais apropriada para cada uma das variáveis selecionadas para o estudo: **`vl_boleto`**, **`vl_pagto`** e **`qtd_acessos_pagador`** que estão presentes no dataset entitulado como **`Grupo com vencimento 07-12 2024 - GF.csv`** fornecido pela empresa parceira Finnet. A decisão será embasada em uma análise estatística da distribuição de cada variável.

---

### Desenvolvimento e justificativa da escolha metodológica
A seleção de uma técnica de escalonamento não é uma decisão livre, mas sim uma que deve ser precedida por uma investigação da natureza estatística dos dados. Existem duas abordagens primárias para o escalonamento: **Padronização (Standardization)** e **Normalização (Normalization)**.

#### Padronização
Também conhecida como **Z-score normalization**, transforma os dados de modo que eles possuam uma **média igual a zero** e um **desvio padrão igual a um**.  
Esta técnica é a mais indicada quando os dados seguem, ou se aproximam, de uma distribuição **normal (gaussiana)**, pois preserva a informação sobre a presença de outliers e mantém a forma da distribuição original.  

Fórmula matemática:
$$
X_{\text{padronizado}} = \frac{X - \mu}{\sigma}
$$

Onde:  
- $\mu$ representa a média populacional  
- $\sigma$ o desvio padrão populacional da variável $X$  

#### Normalização
Frequentemente referida como **Min-Max Scaling**, redimensiona os dados para um **intervalo fixo**, comumente entre **0 e 1**.  
Esta abordagem é particularmente recomendada para variáveis que **não apresentam distribuição normal** ou quando o algoritmo a ser utilizado **não faz suposições sobre a distribuição dos dados de entrada** de acordo com (HAN; PEI; KAMBER, 2012).  

Fórmula matemática:
$$
X_{\text{normalizado}} = \frac{X - X_{\min}}{X_{\max} - X_{\min}}
$$

Onde:  
- $X_{\min}$ é o valor mínimo da variável  
- $X_{\max}$ é o valor máximo da variável  

---

### Teste de Normalidade
Para realizar uma escolha metodologicamente correta entre as duas técnicas, foi conduzido um teste estatístico de normalidade. O teste selecionado foi o **Teste de Lilliefors**.

A escolha pelo teste de Lilliefors se justifica por sua maior adequação em cenários onde a média e o desvio padrão da população são desconhecidos e precisam ser estimados a partir da própria amostra de dados como presente na documentação (LILLIEFORS, 1967).  

#### Implementação em Python
```python
from statsmodels.stats.diagnostic import lilliefors

# ... para cada variável 'var' em análise ...
ksstat, p_valor = lilliefors(df_analise[var], dist='norm')

# Estrutura do teste de hipóteses:

- Hipótese nula (H₀): "os dados da variável em análise provêm de uma população com distribuição normal".

- Nível de significância (α): 0.05 (padrão na literatura estatística).

# Decisão baseada no valor-p:

alpha = 0.05
if p_valor <= alpha:
    # Evidência estatística para rejeitar H₀
    print("Conclusão: Os dados NÃO seguem uma distribuição normal.")
    print("Método Recomendado: Normalização (Min-Max Scaler)")
else:
    # Nenhuma evidência estatística para rejeitar H₀
    print("Conclusão: Não há evidências para rejeitar a normalidade dos dados.")
    print("Método Recomendado: Padronização (Z-Score Scaler)")

```

### Resultados Obtidos

A análise foi executada sobre **644 registros válidos** do dataset fornecido pela Finnet, após tratamento prévio que incluiu a remoção de valores nulos.

Os resultados quantitativos foram:

- **Variável vl_boleto:** p-valor ≈ 0.001  
- **Variável vl_pagto:** p-valor ≈ 0.001  
- **Variável qtd_acessos_pagador:** p-valor ≈ 0.001  

Para todas as três variáveis analisadas, o p-valor obtido (≈0.001) é **significativamente inferior ao nível de significância α = 0.05**.  

**Conclusão parcial:** a hipótese de normalidade (H₀) é **formalmente rejeitada** para todas as variáveis.  

---

### Conclusão

Com base nesta evidência estatística, o método de escalonamento mais adequado e metodologicamente defensável é a **Normalização (Min-Max Scaler)**.  

A aplicação da **Padronização** seria tecnicamente inadequada, uma vez que sua principal premissa (a normalidade dos dados) foi violada. Isso poderia levar a uma **representação distorcida** das características no espaço de atributos do modelo de estudo.  

Já a **Normalização**, por não assumir distribuição específica e por confinar todos os valores a um **intervalo bem definido de [0, 1]**, assegura que as variáveis sejam tratadas de forma equitativa pelo modelo, independentemente de suas escalas originais.  

**Em suma:** após a realização do teste de normalidade de Lilliefors, constatou-se, que as distribuições das variáveis **vl_boleto**, **vl_pagto** e **qtd_acessos_pagador** se desviam significativamente da normalidade.  

Portanto, a técnica de escalonamento escolhida para essas três variáveis quantitativas do projeto é a Normalização (Min-Max Scaling).

---

## 2.2. Extração de parâmetros estatísticos para o Escalonamento de Dados

### Introdução
Dando prosseguimento à metodologia de pré-processamento de dados definida para este projeto, e em alinhamento com a decisão de empregar a técnica de **Normalização (Min-Max Scaling)**, esta parte da seção se dedica à extração dos parâmetros estatísticos descritivos do conjunto de dados fornecidos pela Finnet (`Grupo com vencimento 07-12 2024 - GF`).  

A computação destes valores é uma etapa intermediária, pois as métricas obtidas — especificamente o **valor mínimo**, o **valor máximo**, a **média** e o **desvio padrão populacional** — são as constantes que alimentarão as equações de transformação a serem aplicadas sobre cada variável.  

A análise estatística descritiva, como defendido por *Han, Pei e Kamber (2012)*, transcende a mera preparação para o escalonamento; ela proporciona uma compreensão quantitativa indsispensável sobre a distribuição, a tendência central e a dispersão dos dados, sendo um passo muito importante para a validação da qualidade dos atributos antes da fase de modelagem.  

O foco desta análise recai sobre as variáveis quantitativas selecionadas por sua relevância para o problema de predição de inadimplência: **`vl_boleto`**, **`vl_pagto`** e **`qtd_acessos_pagador`**.  

O processo, implementado em Python com a biblioteca pandas e NumPy, será descrito abaixo.  

---

### Desenvolvimento do processo computacional

A obtenção dos parâmetros estatísticos foi realizada por meio de um script em Python, que iniciou com o carregamento do dataset e a limpeza de dados.  

Utilizou-se a biblioteca `pandas` para ler o arquivo CSV e para realizar a subsequente manipulação dos dados.  

Primeiramente, foi realizada a substituição da string `\N`, utilizada no dataset para representar valores ausentes, pelo formato padrão `np.nan` do NumPy, garantindo a interoperabilidade com as funções estatísticas.  

As colunas de interesse para a análise foram selecionadas:

```python
# Seleção das colunas de interesse para a análise estatística.
colunas_interesse = ['vl_boleto', 'vl_pagto', 'qtd_acessos_pagador']
df_analise = df[colunas_interesse].copy()
```
Uma etapa muito importante de preparação foi a conversão dos tipos de dados para o formato numérico.  

Este procedimento foi executado em um laço, aplicando a função `pd.to_numeric` a cada coluna. O uso do argumento `errors='coerce'` nesta etapa é uma prática que confere embasamento ao processo, pois quaisquer valores que não possam ser convertidos para um número (por exemplo, devido a um erro de digitação no dataset) são automaticamente transformados em valores nulos (`NaN`).  

Esses valores nulos são, por padrão, ignorados pelas funções de cálculo estatístico do pandas, prevenindo assim distorções nos resultados.  

```python
# Garante que todas as colunas de análise sejam do tipo numérico.
for col in colunas_interesse:
    df_analise[col] = pd.to_numeric(df_analise[col], errors='coerce')

```
Para as três variáveis, foram calculadas as quatro métricas estatísticas descritivas essenciais: **valor mínimo, valor máximo, média e desvio padrão populacional**.  

A escolha do **desvio padrão populacional**, especificado pelo argumento `ddof=0` (*Delta Degrees of Freedom* igual a zero), é uma decisão intencional. Considera-se o conjunto de dados em análise como a **população total** de interesse para este escopo, e não uma amostra de um universo maior.  

Esta abordagem, conforme discutido por Montgomery e Runger (2018), garante que a medida de dispersão reflita a variabilidade exata dos dados disponíveis, sem a correção de Bessel que seria aplicada para inferências amostrais.  

A agregação dessas métricas foi estruturada em um novo DataFrame do pandas, facilitando a visualização e o uso futuro desses parâmetros.

```python

# Cria um DataFrame para armazenar as estatísticas calculadas
estatisticas_descritivas = pd.DataFrame({
    "Valor Mínimo": df_analise[colunas_interesse].min(),
    "Valor Máximo": df_analise[colunas_interesse].max(),
    "Média": df_analise[colunas_interesse].mean(),
    # 'ddof=0' calcula o desvio padrão populacional
    "Desvio Padrão Populacional": df_analise[colunas_interesse].std(ddof=0)
})

```

A execução deste bloco de código produziu a tabela de resultados, que foi formatada com arredondamento para duas casas decimais para melhor legibilidade, consolidando os parâmetros necessários para a etapa de normalização.

<div align="center">
<sub>Figura XX: Tabela de resultados dos valores de máximo, mínimo e desvio padrão.</sub>
</div>
<div align="center">
<img src="https://plum-atomic-lemur-391.mypinata.cloud/ipfs/bafkreih25mjmehpqmbhj43ncnccdtixuz57vmf4qsyizehtake4pzbkgse" alt="Histograma 1" width="1000px">

<sub>Fonte: Material produzido pela equipe utilizando a biblioteca de python Pandas, 2025.</sub>
</div> 

A análise estatística descritiva aplicada às variáveis quantitativas do dataset fornecido pela Finnet permitiu identificar métricas fundamentais de tendência central e dispersão, que constituem a base para a etapa posterior de escalonamento dos dados. Os resultados obtidos revelaram que a variável `vl_boleto` apresentou valores mínimos de 1.0 e máximos de 854.62, com média de 303.65 e desvio padrão populacional de 58.55. Já a variável `vl_pagto` apresentou mínimo de 99.0, máximo de 566.83, média de 300.17 e desvio padrão populacional de 57.43. Por sua vez, a variável `qtd_acessos_pagador` demonstrou mínimo de 1.0, máximo de 53.0, média de 3.2 e desvio padrão populacional de 3.03.  

Esses resultados indicam padrões distintos entre as variáveis. As duas primeiras (`vl_boleto` e `vl_pagto`) possuem médias próximas, o que sugere consistência entre o valor de boletos emitidos e os pagamentos realizados, ainda que a dispersão da primeira seja maior, refletindo a existência de boletos com valores mais elevados. Já a variável `qtd_acessos_pagador` apresentou média baixa e baixo desvio padrão em relação ao seu máximo, sugerindo que a maior parte dos clientes acessa o sistema poucas vezes, com comportamento relativamente homogêneo.  

A relevância dessa etapa para o tratamento dos dados se explica pela necessidade de **preparar as variáveis para técnicas de escalonamento**, como a normalização por Min-Max Scaling. Esse tipo de transformação depende diretamente do valor mínimo e máximo das variáveis, que funcionam como parâmetros fixos na equação de reescalonamento, trazendo todos os atributos para a mesma faixa de valores, geralmente [0, 1]. Caso tais parâmetros não fossem calculados previamente, não seria possível aplicar a normalização de forma correta. Além disso, conhecer a média e o desvio padrão fornece uma compreensão mais ampla da distribuição dos dados, permitindo verificar se existem outliers ou padrões de dispersão que possam influenciar a performance de modelos preditivos de aprendizado de máquina.  

---

### Conclusão  

A execução bem-sucedida desta etapa resultou na **extração dos parâmetros estatísticos descritivos** das variáveis quantitativas selecionadas.  

O processo, fundamentado em práticas de **limpeza e conversão de dados**, garantiu a precisão das métricas de **mínimo, máximo, média e desvio padrão populacional**.  

A análise desses resultados não apenas validou a necessidade da **normalização**, dada a disparidade de escalas, mas também forneceu insights sobre as características das transações financeiras e do comportamento dos usuários no ecossistema da Finnet.

---

## 2.3. Formulação das Equações de Normalização específicas para as Variáveis selecionadas

### Introdução
Após a análise estatística que confirmou a necessidade de Normalização e a subsequente extração dos parâmetros descritivos do dataset, a presente subseção avança da análise para a aplicação. O objetivo aqui foi operacionalizar a teoria, traduzindo a fórmula matemática genérica da Normalização (Min-Max Scaling) em equações específicas para cada uma das variáveis quantitativas selecionadas para a análise: **vl_boleto, vl_pagto e qtd_acessos_pagador**. 

Esta etapa é de suma importância, pois materializa o processo de normalização, criando as expressões exatas que serão computacionalmente aplicadas a cada registro do conjunto de dados. A formulação de equações explícitas, com constantes derivadas diretamente dos dados, garante a transparência, a consistência e a reprodutibilidade do pré-processamento, um princípio muito importante para a construção de modelos de machine learning confiáveis e auditáveis.

---

### Desenvolvimento e processo de geração das equações
A base para a formulação das equações específicas é a expressão matemática canônica da Normalização Min-Max, que visa remapear uma variável original \(X\) para um novo intervalo, tipicamente \([0, 1]\). A fórmula geral é dada por:

$$
X_{normalizado} = \frac{X - X_{min}}{X_{max} - X_{min}}
$$

Onde \(X_{min}\) e \(X_{max}\) representam, respectivamente, os valores mínimo e máximo da variável \(X\) no conjunto de dados. O passo seguinte consiste em substituir as constantes \(X_{min}\) e \(X_{max}\) pelos valores reais extraídos na etapa anterior para cada uma das nossas variáveis de interesse.

Para assegurar a precisão e a eficiência deste processo, foi utilizado um script em **Python** que automatiza a geração dessas equações. Após o carregamento e a limpeza dos dados, o script primeiramente calcula os valores mínimo e máximo para cada coluna de interesse, utilizando as funções `.min()` e `.max()` da biblioteca **pandas**.

```python
# Calcula o valor mínimo para cada coluna, ignorando NaNs
min_values = df_analise[colunas_interesse].min()

# Calcula o valor máximo para cada coluna, ignorando NaNs
max_values = df_analise[colunas_interesse].max()

# Itera sobre cada variável para gerar e exibir sua equação específica
for var in colunas_interesse:
    var_min = min_values[var]
    var_max = max_values[var]
    
    # Monta a string da equação usando f-string para substituir as constantes
    equacao = f"  {var}_norm = ({var} - {var_min}) / ({var_max} - {var_min})"
    print(equacao)

# Resultados: Equações de Normalização Formuladas

```
A execução do processo descrito acima, com os dados corretos, resultou na geração das seguintes equações de transformação, que serão utilizadas para reescalar os dados do projeto. Para maior clareza e formalismo matemático, as equações são apresentadas abaixo:


#### a. Equação para a variável *vl_boleto* :

$$
vl\_boleto_{norm} = \frac{vl\_boleto - 1.0}{854.62 - 1.0}
$$

Nesta equação, o valor 1.0 representa o valor mínimo observado para *vl_boleto*, enquanto 854.62 é o valor máximo. Qualquer valor de boleto no dataset será transformado aplicando-se esta fórmula.

---

#### b. Equação para a variável *vl_pagto* :

$$
vl\_pagto_{norm} = \frac{vl\_pagto - 99.0}{566.83 - 99.0}
$$

Para a variável *vl_pagto*, o valor mínimo registrado foi 99.0 e o valor máximo foi 566.83.

---

#### c. Equação para a variável *qtd_acessos_pagador* :

$$
qtd\_acessos\_pagador_{norm} = \frac{qtd\_acessos\_pagador - 1.0}{53.0 - 1.0}
$$

Por fim, para a quantidade de acessos do pagador, a escala original varia de 1.0 a 53.0. A aplicação desta equação mapeará essa contagem para o intervalo \([0,1]\).

---

### Conclusão

Com a formulação destas três equações específicas e baseadas nos dados, conclui-se uma etapa muito importante do pré-processamento. A transição da teoria para a prática foi efetivada, resultando em um conjunto de regras de transformações objetivas e prontas para a implementação computacional. Estas equações garantem que a normalização aplicada ao dataset do projeto Finnet será reprodutível e fiel às características estatísticas do próprio conjunto de dados. Como ressalta Grus (2019), a aplicação de transformações bem definidas como esta é essencial para preparar os dados para algoritmos que são sensíveis à escala, pavimentando o caminho para um treinamento de modelo mais justo, estável e com maior potencial de performance.

---

## 2.4. Análise visual dos efeitos da Normalização via Histogramas

### Introdução
Após a formulação matemática das equações de escalonamento, é necessário realizar uma validação visual para compreender os efeitos da transformação nos dados. A visualização de dados é uma ferramenta analítica que permite a inspeção da estrutura de um dataset de uma maneira que tabelas de números por si só não conseguem como presente na literatura base (MCKINNEY, 2018). O objetivo desta subseção é, portanto, apresentar os histogramas das variáveis **vl_boleto**, **vl_pagto** e **qtd_acessos_pagador** após a aplicação da **Normalização Min-Max** e conduzir uma análise comparativa com as distribuições originais (pré-escalonamento).  

O histograma, como ferramenta gráfica, é particularmente eficaz para esta tarefa, pois revela a forma da distribuição de frequência de uma variável. Esta análise visual não serve apenas como uma verificação da implementação, mas também para reforçar um conceito teórico muito importante: o de que o escalonamento linear não altera somente a escala, mas preserva a forma intrínseca da distribuição dos dados.

---

### Desenvolvimento e metodologia de implementação
O primeiro passo para a geração dos histogramas pós-escalonamento foi a aplicação da transformação de Normalização no conjunto de dados. Para esta tarefa, foi utilizada a classe **MinMaxScaler** da biblioteca **scikit-learn**, um padrão da indústria para operações de pré-processamento em pipelines de machine learning como presente na bibliografia (MÜLLER; GUIDO, 2017).  

O processo foi implementado de forma programática, iterando sobre cada coluna de interesse, tratando adequadamente os valores ausentes (NaN) e aplicando a transformação.

O método **`.fit_transform()`** do MinMaxScaler foi utilizado. Este método, em um único passo, primeiro "aprende" os parâmetros da transformação (os valores mínimo e máximo) a partir dos dados (*etapa fit*) e, em seguida, aplica a transformação para reescalá-los (*etapa transform*). É importante notar que a transformação foi aplicada a cada coluna individualmente, garantindo que o escalonamento de uma variável não fosse influenciado pelas outras.

```python
# Importa a classe MinMaxScaler da biblioteca scikit-learn
from sklearn.preprocessing import MinMaxScaler

# Itera sobre cada coluna para aplicar o escalonamento individualmente
for col in colunas_interesse:
    scaler = MinMaxScaler()
    
    # O método fit_transform aprende os parâmetros (min/max) e aplica a transformação
    # .dropna() garante que o scaler seja treinado apenas com dados válidos
    scaled_column = scaler.fit_transform(df_analise[[col]].dropna())

```

Uma vez que os dados foram transformados e armazenados em um novo DataFrame (df_scaled), o passo seguinte foi a geração dos histogramas.

Para esta visualização, foram utilizadas as bibliotecas **matplotlib** e **seaborn**, que oferecem recursos gráficos de alta qualidade. Os histogramas foram dispostos em uma grade de uma linha por três colunas (plt.subplots(1, 3, ...)), uma configuração que facilita a comparação visual direta entre as distribuições das três variáveis já normalizadas.

Foi escolhida uma quantidade de **50 barras (bins=50)** para cada histograma, de modo a se obter uma representação de alta granularidade da frequência dos dados.

---

### Resultados e Análise Comparativa

A execução do script gerou a visualização abaixo, que apresenta a distribuição de cada variável após a normalização.

<div align="center">
<sub>Figura XX: Gráfico da distribuição das variáveis vl_boleto, vl_pagto e qtd_acessos_pagador após a normalização.</sub>
</div>
<div align="center">
<img src="https://plum-atomic-lemur-391.mypinata.cloud/ipfs/bafkreieozxp2lo24l7qm33k7esvwtovrxqn6xogh46qnytiw3esbmfhl3m" alt="Histograma 1" width="1000px">

<sub>Fonte: Material produzido pela equipe utilizando as bibliotecas matplotlib e seaborn, 2025.</sub>
</div>

#### Análise Comparativa

A análise comparativa entre os dois conjuntos de histogramas revela uma conclusão de extrema importância:  
os gráficos são visual e estruturalmente idênticos em sua forma, o que muda é unicamente a escala do eixo horizontal (eixo-x).  

Esta observação confirma que a Normalização Min-Max, sendo uma transformação linear, não altera a estrutura da distribuição de probabilidade subjacente aos dados.

---

##### Variáveis vl_boleto e vl_pagto

Nos histogramas originais, observa-se que as distribuições de vl_boleto e vl_pagto se aproximam de uma simetria.  
Valores estatísticos de referência:  
- vl_boleto: média = 303,65, mediana = 305,17  
- vl_pagto: média = 300,17, mediana = 300,90  

A proximidade entre média e mediana reforça a percepção visual de simetria.  

Contudo, os testes estatísticos (Lilliefors) rejeitaram a hipótese de normalidade.  
Isso provavelmente ocorreu devido à alta sensibilidade do teste em amostras grandes, que detecta pequenos desvios.  

Nos histogramas normalizados, a mesma forma da distribuição (simetria e picos) é preservada.  
A única diferença é que o eixo-x, que antes representava valores monetários, agora está comprimido no intervalo [0, 1].

---

##### Variável qtd_acessos_pagador

Diferente das anteriores, esta variável exibe uma assimetria positiva (à direita).  
Características:  
- Mediana = 2,0  
- Média = 3,19  
- Histograma mostra alta concentração em valores baixos e uma cauda longa à direita.  

Este formato é um indicativo clássico de não normalidade.  

Nos histogramas normalizados, a estrutura é exatamente a mesma:  
- Grande concentração de barras próximas ao valor 0.  
- Cauda decrescente em direção ao valor 1.  

A transformação apenas reescalou os eixos.

---

Este resultado é o esperado e desejado. Transformações lineares como a Normalização Min-Max são projetadas para modificar o centro e a amplitude dos dados sem distorcer as relações entre os pontos ou a forma geral da distribuição (Grus, 2019).

A visualização confirma que a transformação foi aplicada corretamente e que a integridade estrutural dos dados foi mantida, o que é essencial para que o modelo de *machine learning* aprenda os padrões corretos sem ser influenciado por artefatos introduzidos no pré-processamento.

---

### Conclusão

Em síntese, a geração de histogramas para as variáveis normalizadas proporcionou uma validação visual dos efeitos do processo de escalonamento. Foi demonstrado que a **transformação Min-Max** cumpriu seu propósito de unificar a escala das variáveis para o intervalo comum de **[0, 1]**, uma condição necessária para muitos algoritmos de aprendizado de máquina.  

Mais importante, foi confirmado que esta transformação preservou a forma original das distribuições, incluindo suas características de assimetria.  

Esta verificação visual finaliza uma etapa muito importante da preparação dos dados, certificando que o conjunto de dados está agora adequadamente escalonado e pronto para ser utilizado como um exemplo para todas as outras variáveis nas fases subsequentes de construção etreinamento do modelo, com a confiança de que sua estrutura intrínseca não foi corrompida.

---

## 2.5. Verificação amostral dos Dados Originais e Normalizados

### Introdução
Após a definição da metodologia, a extração de parâmetros, a formulação de equações e a validação visual agregada por meio de histogramas, esta subseção final do processo de escalonamento se dedica a uma verificação em nível granular. O objetivo é apresentar uma comparação de uma amostra de dados antes e depois da aplicação da **Normalização Min-Max**.  

Enquanto as análises anteriores forneceram uma compreensão teórica e uma visão macroscópica da transformação, a inspeção de registros individuais serve como a prova final do impacto da operação como presente na literatura (PROVOST; FAWCETT, 2013).  

Esta etapa é análoga a um teste de unidade no ciclo de desenvolvimento de software: ela verifica se a lógica de transformação, que foi projetada e analisada em teoria, funciona precisamente como esperado em instâncias de dados reais.  

Serão apresentadas duas tabelas contendo os dez primeiros registros das variáveis quantitativas em seu estado original e em seu estado já normalizado.

---

### Desenvolvimento e Metodologia da Amostragem
A metodologia para esta verificação final foi feita utilizando a biblioteca pandas, onde foram geradas duas visualizações tabulares a partir de dois DataFrames distintos:  

- **df_analise** → contendo os dados limpos, mas em sua escala original.  
- **df_scaled** → armazenando os resultados da aplicação do **MinMaxScaler** do scikit-learn.  

Para extrair a amostra representativa dos primeiros registros de cada conjunto de dados, foi empregado o método **`.head(10)`**, uma função padrão do pandas para a inspeção inicial de dados.  

Esta abordagem simples e eficaz permite um comparativo direto, pois preserva a correspondência de índices entre as duas tabelas, possibilitando a análise do efeito da transformação em cada linha individualmente.

---

### Resultados e Comparação Tabular Detalhada
A execução do processo resultou nas duas tabelas a seguir. A primeira exibe os dados em sua escala original, caracterizada por magnitudes e intervalos diferentes. A segunda apresenta os mesmos registros após a transformação, agora confinados ao intervalo uniforme de **[0, 1]**.

#### Tabela: Amostra dos 10 Primeiros Registros dos Dados Originais

| Índice | vl_boleto | vl_pagto | qtd_acessos_pagador |
|--------|-----------|----------|----------------------|
| 0 | 240.65 | 223.80 | NaN |
| 1 | 155.33 | 158.54 | NaN |
| 2 | 325.52 | 302.73 | 1.0 |
| 3 | 325.52 | 302.73 | NaN |
| 4 | 290.97 | 290.97 | NaN |
| 5 | 244.14 | 227.05 | 2.0 |
| 6 | 155.36 | 144.48 | NaN |
| 7 | 194.21 | 180.62 | 1.0 |
| 8 | 155.36 | 144.48 | 3.0 |
| 9 | 155.36 | 144.48 | 2.0 |

---

#### Tabela: Amostra dos 10 Primeiros Registros dos Dados Normalizados

| Índice | vl_boleto_normalizado | vl_pagto_normalizado | qtd_acessos_pagador_normalizado |
|--------|------------------------|-----------------------|---------------------------------|
| 0 | 0.28 | 0.26 | NaN |
| 1 | 0.18 | 0.13 | NaN |
| 2 | 0.38 | 0.43 | 0.00 |
| 3 | 0.38 | 0.43 | NaN |
| 4 | 0.34 | 0.41 | NaN |
| 5 | 0.29 | 0.27 | 0.02 |
| 6 | 0.18 | 0.10 | NaN |
| 7 | 0.23 | 0.17 | 0.00 |
| 8 | 0.18 | 0.10 | 0.04 |
| 9 | 0.18 | 0.10 | 0.02 |

---

### Análise Comparativa em Nível de Registro
A comparação direta entre as tabelas permite uma **verificação matemática da transformação**.  

Tomemos como exemplo o registro de **índice 2**:

#### Normalização das Variáveis

- **vl_boleto**:  
O valor original é `325.52`.  
Utilizando a equação de normalização derivada na subseção **2.3** para esta variável:

$$
vl_{boleto}^{norm} = \frac{vl_{boleto} - 1.0}{854.62 - 1.0}
$$

Aplicando o cálculo:

$$
\frac{325.52 - 1.0}{854.62 - 1.0} = \frac{324.52}{853.62} \approx 0.3802
$$

Esse valor, arredondado para **duas casas decimais**, é:

$$
vl_{boleto}^{norm} = 0.38
$$

---

- **vl_pagto**:  

O valor original de *vl_pagto* é `302.73`.  
Aplicando a equação de normalização:

$$
vl_{pagto}^{norm} = \frac{vl_{pagto} - 99.0}{566.83 - 99.0}
$$

Substituindo:

$$
\frac{302.73 - 99.0}{566.83 - 99.0} = \frac{203.73}{467.83} \approx 0.4355
$$

Arredondando para duas casas decimais:

$$
vl_{pagto}^{norm} = 0.44
$$

---

- **qtd_acessos_pagador**:  
O valor original é `1.0`.  
Utilizando a equação correspondente:

$$
qtd_{acessos\_pagador}^{norm} = \frac{qtd_{acessos\_pagador} - 1.0}{53.0 - 1.0}
$$

O cálculo é:

$$
\frac{1.0 - 1.0}{53.0 - 1.0} = \frac{0.0}{52.0} = 0.00
$$

Resultado final:

$$
qtd_{acessos\_pagador}^{norm} = 0.00
$$

---

Ademais, é fundamental observar o **tratamento dos valores ausentes**.  
No registro de **índice 0**, a variável *qtd_acessos_pagador* possui um valor `NaN` (*Not a Number*).  

Na Tabela com os dados normalizados, este valor é corretamente preservado como `NaN`.  
Isso demonstra que o processo de escalonamento foi aplicado de forma correta, mantendo a integridade dos dados faltantes, que deverão ser tratados em uma etapa posterior, se for necessário.

---

### Conclusão
A apresentação e a análise comparativa das tabelas de dados originais e escalonados forneceram a validação final de todo o processo de Normalização.  

Foi demonstrado, por meio de cálculos explícitos em registros amostrais, que a transformação foi implementada com precisão, convertendo as escalas díspares das variáveis para um intervalo uniforme de **[0, 1]**, de acordo com as regras matemáticas previamente estabelecidas.  

Esta verificação em nível de registro confirma a eficácia do código implementado e a correção teórica da abordagem.  

Com esta etapa, conclui-se o sub-processo de escalonamento de dados do projeto, resultando em um conjunto de dados cujas variáveis quantitativas estão agora preparadas, consistentes e otimizadas para serem utilizadas nos algoritmos de aprendizado de máquina que constituem o núcleo deste projeto de modelo preditivo para a Finnet.

---

## Conclusão da seção

A conclusão desta seção evidencia a importância das etapas de análise estatística e pré-processamento na construção de um modelo preditivo. Inicialmente, foi realizada a formulação de hipóteses estatísticas e a aplicação do teste de **Lilliefors**, que permitiram verificar se as variáveis quantitativas de interesse — **vl_boleto**, **vl_pagto** e **qtd_acessos_pagador** — seguiam ou não uma distribuição normal. Os resultados mostraram de forma consistente que todas as variáveis se desviam significativamente da normalidade, o que justificou a adoção de abordagens de pré-processamento mais adequadas para esse cenário.

A interpretação dos testes foi enriquecida por meio de análises gráficas com histogramas e pela comparação entre média e mediana. Essas ferramentas complementares possibilitaram compreender melhor a estrutura dos dados, revelando tanto distribuições simétricas, mas não normais, como no caso de **vl_boleto** e **vl_pagto**, quanto distribuições assimétricas, como a de **qtd_acessos_pagador**. Essa triangulação metodológica reforçou a confiança das conclusões e assegurou que as decisões tomadas não fossem apenas baseadas em resultados numéricos, mas também em evidências visuais e descritivas.

A partir desses resultados, foi possível justificar a escolha pela **normalização Min-Max** como técnica de escalonamento. Essa decisão metodológica mostrou-se a mais adequada, uma vez que a padronização parte do pressuposto de normalidade dos dados, premissa rejeitada para todas as variáveis analisadas. A normalização, ao reescalar os valores para o intervalo [0,1], garantiu comparabilidade entre variáveis de magnitudes distintas e preservou a forma original das distribuições. Além disso, os histogramas pós-escalonamento confirmaram visualmente que a transformação manteve a integridade estrutural dos dados, alterando apenas a escala.

Por fim, a verificação em nível amostral, com a apresentação de tabelas comparando os primeiros registros dos dados originais e normalizados, consolidou a transparência e a reprodutibilidade do processo. Essa etapa final funcionou como uma validação prática, demonstrando que as equações de normalização foram aplicadas corretamente e que os resultados obtidos estão alinhados com os cálculos teóricos.

Em síntese, esta seção documentou de forma completa e fundamentada todas as etapas necessárias para preparar uma amostragem representativa de variáveis quantitativas presentes em um dos datasets fornecidos pela Finnet. Foi feito o teste de hipoteses, a extração de parâmetros estatísticos, a formulação de equações de normalização e a validação visual do escalonamento, passando pelas análises gráficas e verificações tabulares, cada passo contribuiu para assegurar que o conjunto de dados esteja devidamente tratado. Esse rigor metodológico fortalece a base científica do trabalho e aumenta sua aplicabilidade prática, fornecendo à Finnet um produto final que une confiabilidade, precisão e transparência em todas as fases do desenvolvimento.
