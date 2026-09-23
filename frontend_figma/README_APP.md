# 🏦 Sistema de Predição de Inadimplência - Finnet Corp

Uma aplicação web desenvolvida em Streamlit para predição de inadimplência de boletos bancários, utilizando o modelo de Machine Learning treinado no projeto Bill Hunters.

## 📋 Funcionalidades

- **Análise de Pagadores Existentes**: Visualize o histórico completo de boletos de clientes já cadastrados
- **Predição para Novos Boletos**: Faça predições de inadimplência para novos boletos
- **Classificação de Risco**: Sistema automático de classificação (Baixo, Médio, Alto)
- **Recomendações Inteligentes**: Sugestões de ações baseadas no nível de risco
- **Interface Intuitiva**: Dashboard interativo e fácil de usar

## 🚀 Como Executar

### Pré-requisitos

- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)

### Instalação

1. Clone o repositório e navegue até o diretório:
```bash
cd 2025-2A-T18-IN03-G05
```

2. Instale as dependências:
```bash
pip install -r requirements_app.txt
```

3. Execute a aplicação:
```bash
streamlit run app_predicao_inadimplencia.py
```

4. Acesse a aplicação no seu navegador:
```
http://localhost:8501
```

## 📊 Estrutura de Dados

A aplicação utiliza os seguintes dados:

### Dados de Entrada (Boleto)
- **Número do Boleto**: Identificador único
- **Valor Original**: Valor do boleto em R$
- **Data de Inclusão**: Data de criação do boleto
- **Data de Vencimento**: Data limite para pagamento
- **ID do Pagador**: Identificador do cliente
- **ID do Grupo**: Grupo do beneficiário
- **ID do Beneficiário**: Identificador do beneficiário

### Dados Históricos (Automaticamente Calculados)
- Quantidade de cobranças históricas
- Valor médio histórico
- Taxa de inadimplência histórica
- Taxa de atraso histórica
- Tempo desde primeira cobrança
- Desvio padrão dos valores

## 🎯 Como Usar

### 1. Análise de Pagador Existente

1. No menu lateral, selecione "Pagador Existente"
2. Escolha um pagador da lista dropdown
3. Visualize o histórico completo de boletos
4. Analise as métricas resumidas (total de boletos, valor total, taxa de inadimplência)

### 2. Predição para Novo Boleto

1. Preencha os dados do novo boleto:
   - Número do boleto
   - Valor original
   - Data de inclusão
   - Data de vencimento
   - IDs do grupo e beneficiário

2. Clique em "Fazer Predição de Inadimplência"

3. Analise os resultados:
   - **Classificação de Risco**: Alto, Médio ou Baixo
   - **Probabilidade**: Percentual de chance de inadimplência
   - **Predição**: Adimplente ou Inadimplente
   - **Recomendações**: Ações sugeridas baseadas no risco

## 📈 Interpretação dos Resultados

### Classificação de Risco

- **🔴 ALTO (>70%)**: Requer ação imediata
  - Contato preventivo com cliente
  - Condições especiais de pagamento
  - Redução de limite de crédito

- **🟡 MÉDIO (30-70%)**: Monitoramento necessário
  - Acompanhamento próximo
  - Lembretes de vencimento
  - Análise adicional do perfil

- **🟢 BAIXO (<30%)**: Cliente confiável
  - Processo padrão de cobrança
  - Possível oferta de produtos adicionais

## 🔧 Arquivos Necessários

Certifique-se de que os seguintes arquivos estejam presentes:

```
├── app_predicao_inadimplencia.py          # Aplicação principal
├── requirements_app.txt                    # Dependências
├── notebook/modelos salvos/
│   └── modelo_bill_hunters_latest.joblib  # Modelo treinado
└── dados/
    └── dados_treino_com_predicoes.csv     # Dados históricos
```

## 🛠️ Tecnologias Utilizadas

- **Streamlit**: Framework para aplicação web
- **Pandas**: Manipulação de dados
- **NumPy**: Computação numérica
- **Scikit-learn**: Machine Learning
- **Joblib**: Serialização do modelo

## 📝 Observações Importantes

1. **Modelo**: Utiliza RandomForestClassifier treinado no notebook `modelo_definitivo.ipynb`
2. **Dados Históricos**: Para pagadores existentes, usa dados históricos para melhor precisão
3. **Novos Pagadores**: Para clientes novos, usa valores padrão baseados no boleto atual
4. **Performance**: Modelo com 96.44% de acurácia e 92.5% de recall

## 🔄 Próximos Passos

- Integração com APIs de bancos de dados
- Sistema de alertas automáticos
- Dashboard gerencial com métricas agregadas
- Módulo de retreinamento automático do modelo
- Exportação de relatórios em PDF

## 🆘 Troubleshooting

### Erro: "Modelo não encontrado"
- Verifique se o arquivo `modelo_bill_hunters_latest.joblib` está na pasta correta
- Certifique-se de que o caminho no código está correto

### Erro: "Dados não encontrados"
- Verifique se o arquivo `dados_treino_com_predicoes.csv` está na pasta `dados/`
- Confirme se o arquivo não está corrompido

### Erro de dependências
- Execute: `pip install --upgrade -r requirements_app.txt`
- Use ambiente virtual (venv) para evitar conflitos

---

**Desenvolvido por**: Equipe Bill Hunters  
**Projeto**: Sistema de Predição de Inadimplência - Finnet Corp  
**Ano**: 2025