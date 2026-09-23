# Inteli - Instituto de Tecnologia e Liderança

<p align="center">
<a href= "https://www.inteli.edu.br/"><img src="assets/inteli.png" alt="Inteli - Instituto de Tecnologia e Liderança" border="0"></a>
</p>

# FinSight - Modelo Preditivo de Inadimplência

## Bill Hunters

## :student: Integrantes:
- <a href="https://www.linkedin.com/in/bruno-martins-2b6742269/">Bruno Discacciati Vieiralves Martins</a>
- <a href="https://www.linkedin.com/in/bruno-gabriel-giordano-guilherme-kadayan-ab86762a0/">Bruno Gabriel Giordano Guilherme Kadayan
- <a href="http://www.linkedin.com/in/carlosicaro">Carlos Icaro Kauã Coelho Paiva
- <a href="http://www.linkedin.com/in/danilo-de-castro-neto">Danilo de Castro Neto
- <a href="https://www.linkedin.com/in/enzorezende/">Enzo de Araujo Rezende</a>
- <a href="https://www.linkedin.com/in/matheusscapolan/">Matheus Henrique Scapolan Silva</a>
- <a href="https://www.linkedin.com/in/victor-garcia-dos-santos/">Víctor Garcia dos Santos

## :teacher: Professores:
### Orientador(a)
- <a href="https://www.linkedin.com/in/fabiana-martins-de-oliveira-8993b0b2/">Fabiana Martins de Oliveira</a>
### Instrutores
- <a href="https://www.linkedin.com/in/rafaelwill/">Rafael Will Macedo de Araujo</a>
- <a href="https://www.linkedin.com/in/profclaudioandre/">Claudio Fernando André</a> 
- <a href="https://www.linkedin.com/in/gui-cestari/">Guilherme Henrique de Oliveira Cestari</a>
- <a href="https://www.linkedin.com/in/luciano-galdino-26191b36/">Luciano Galdino</a>
- <a href="https://www.linkedin.com/in/natalia-k-37a62052/">Natalia Varela da Rocha Kloeckner</a>

## Sobre o Projeto

O FinSight é um projeto desenvolvido em parceria com a Finnet, empresa líder em soluções de conectividade financeira B2B no Brasil, que processa anualmente mais de R$ 2,1 trilhões em transações e conecta mais de 3,2 milhões de CNPJs. O projeto foi desenvolvido no âmbito do Módulo 3 do curso de Sistemas de Informação do Inteli - Instituto de Tecnologia e Liderança, focado em "Lógica para Predição com Inteligência Artificial".

O problema central abordado é a gestão de inadimplência na plataforma de cobranças da Finnet. A inadimplência representa um risco direto ao fluxo de caixa e à saúde financeira das empresas clientes, sendo um desafio crítico no setor de gestão de recebíveis.

A solução proposta consiste no desenvolvimento de um sistema preditivo que poderá serintegrado à plataforma Luna da Finnet, que utiliza técnicas de machine learning para antecipar comportamentos de inadimplência. O modelo analisa dados transacionais históricos de cobranças para identificar padrões e fornecer insights preditivos que permitem ações preventivas.

Os principais objetivos do projeto incluem:
- Desenvolver modelos de classificação para prever tendências de pagamento (Em Dia, Atraso, Inadimplente)
- Criar um sistema de score de risco probabilístico para apoiar decisões de cobrança
- Implementar funcionalidades de predição de valores de recebimento e percentual de inadimplência por período

As tecnologias de machine learning utilizadas incluem algoritmos de classificação como Random Forest, XGBoost e Regressão Logística, implementados em Python com bibliotecas como Pandas, NumPy, Scikit-learn e XGBoost. O desenvolvimento foi realizado em Jupyter Notebooks para facilitar a exploração interativa dos dados e documentação do processo.

## Demonstração

Confira uma demonstração da nossa solução em funcionamento:

**[Link para o Vídeo de Demonstração no YouTube](https://youtu.be/8iCDw3Zmq18)**

## Estrutura do Repositório

```
├── art_matematica/
│   ├── artefato_mat_pt1.ipynb
│   └── artefato_mat_pt2.ipynb
├── assets/
│   ├── Graficos de adequação de modelos.png
│   ├── JornadaUsuario-Alice.jpg
│   ├── JornadaUsuario-Cecilia.jpg
│   ├── Matriz de Risco.png
│   ├── Persona_Cecilia.png
│   ├── Persona_David.png
│   ├── SWOT.jpg
│   ├── canvaPropostaValor.png
│   ├── inteli.png
│   ├── persona_alice.jpg
│   ├── persona_marcelo.jpg
│   └── art_matematica/
├── notebooks/
│   ├── modelo_definitivo.ipynb
│   └── Notebooks Antigos/
│       ├── modelo_1_%_inadimplencia.ipynb
│       ├── modelo_2.ipynb
│       ├── modelo-3-predicao-valores.ipynb
│       ├── notebook-decision-tree-score.ipynb
│       ├── notebook-random-forest-regressor.ipynb
│       ├── notebook-xgboost-score.ipynb
│       └── notebook.ipynb
├── frontend/
│   ├── documentacao.md
│   ├── assets/
│   │   ├── finnet.png
│   │   ├── lua.png
│   │   └── modelo_preditivo.png
│   ├── app.py
│   ├── README.md
│   ├── requirements.txt
│   └── run.py
├── dados/
│   └── [arquivos de dados CSV]
├── documents/
│   ├── documentacao.md
│   └── extras/
├── .gitattributes
├── .gitignore
└── README.md
```

## Como Executar

### Pré-requisitos

- Python 3.10 ou superior
- Jupyter Lab ou Jupyter Notebook

### Instalação das Dependências

1. Clone o repositório:
```bash
git clone [URL_DO_REPOSITORIO]
cd [NOME_DO_REPOSITORIO]
```

2. Instale as dependências necessárias:
```bash
pip install pandas numpy matplotlib seaborn scikit-learn xgboost openpyxl jupyterlab
```

### Execução dos Notebooks

1. Inicie o Jupyter Lab:
```bash
jupyter lab
```

2. Navegue até a pasta `notebooks/` e abra o notebook principal:
   - `modelo_definitivo.ipynb` - Modelo definitivo

3. Execute as células sequencialmente usando `Shift + Enter` ou utilize "Run All Cells" no menu Cell.

### Dados

Os dados necessários estão localizados nas pastas `notebooks/` e `dados/`. Certifique-se de que os arquivos CSV estejam no local correto antes de executar os notebooks.

## Histórico de Lançamentos

### Sprint 1 - 15/08/2025
- **Entendimento do negócio**: Contexto Setorial + 5 Forças de Porter
- **Análise SWOT**: Avaliação de forças, fraquezas, oportunidades e ameaças
- **Planejamento Geral da Solução**: Definição da arquitetura e escopo
- **Value Proposition Canvas**: Mapeamento de proposta de valor
- **Matriz de Riscos**: Identificação e mitigação de riscos do projeto
- **Política de Privacidade – LGPD**: Adequação às normas de proteção de dados
- **Entendimento da Experiência do Usuário I**: Desenvolvimento de Personas

### Sprint 2 - 29/08/2025
- **Desenvolvimento da Programação**: Exploração de Dados, Pré-processamento e Levantamento de Hipóteses
- **Entendimento da Experiência do Usuário Parte II**: Criação de Jornadas de Usuário
- **Artefato de Matemática**: Análise e teste de normalidade das variáveis quantitativas
- **Escalonamento**: Padronização ou normalização nas variáveis quantitativas

### Sprint 3 - 12/09/2025
- **Entrega do Primeiro modelo candidato**: Preparação dos Dados e Modelagem inicial

### Sprint 4 - 26/09/2025
- **Apresentação de um Notebook com a Comparação de modelos**: Avaliação comparativa de diferentes algoritmos

### Sprint 5 - 09/10/2025
- **Entrega do Modelo Final**: Implementação da solução completa
- **Adequação do Projeto com os Critérios de Publicação**: Finalização da documentação
- **Apresentação do Pitch final**: Apresentação dos resultados e impactos

## Licença

Este projeto é licenciado sob a Licença Creative Commons Attribution 4.0 International. 

<p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/Inteli-College/2025-1B-T18-IN02-G03.git">Finsight</a> by <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://github.com/Inteli-College/2025-1B-T18-IN02-G03.git">INTELI, BRUNO DISCACCIATI VIEIRALVES MARTINS, BRUNO GABRIEL GIORDANO GUILHERME KADAYAN, CARLOS ICARO KAUÃ COELHO PAIVA, DANILO DE CASTRO NETO, ENZO ARAUJO DE REZENDE, MATHEUS HENRIQUE SCAPOLAN SILVA, VÍCTOR GARCIA DOS SANTOS</a> is licensed under <a href="https://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Creative Commons Attribution 4.0 International<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1" alt=""><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1" alt=""></a></p>
