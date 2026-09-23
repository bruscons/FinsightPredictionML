# 🏦 Sistema de Predição de Inadimplência - Finnet Corp

Sistema web completo para predição de inadimplência de boletos bancários, utilizando o modelo de Machine Learning desenvolvido pela equipe Bill Hunters.

## 🚀 Aplicações Disponíveis

### 1. Aplicação Flask (Recomendada)
Interface web completa com dashboard interativo.

**Para iniciar:**
```bash
# Método 1: Script automático (Windows)
iniciar_app.bat

# Método 2: PowerShell (Windows)
.\iniciar_app.ps1

# Método 3: Manual
pip install -r requirements_flask.txt
python app_flask.py
```

**Acesse:** http://localhost:5000

### 2. Aplicação Streamlit (Alternativa)
Interface moderna e responsiva.

```bash
pip install -r requirements_app.txt
streamlit run app_predicao_inadimplencia.py
```

**Acesse:** http://localhost:8501

## 📋 Funcionalidades

### 🔍 Análise de Pagadores Existentes
- Visualização completa do histórico de boletos
- Métricas consolidadas (total de boletos, valor total, taxa de inadimplência)
- Tabela detalhada com todos os boletos do pagador
- Identificação automática de padrões de comportamento

### 🎯 Predição para Novos Boletos
- Formulário intuitivo para entrada de dados
- Validação automática de campos obrigatórios
- Cálculo de features automatizadas (dias para vencimento, etc.)
- Utilização de dados históricos quando disponíveis

### 📊 Sistema de Classificação de Risco
- **🟢 RISCO BAIXO (<30%)**: Cliente confiável
- **🟡 RISCO MÉDIO (30-70%)**: Monitoramento necessário  
- **🔴 RISCO ALTO (>70%)**: Ações imediatas recomendadas

### 💡 Recomendações Inteligentes
- Sugestões personalizadas baseadas no nível de risco
- Estratégias de cobrança preventiva
- Orientações para gestão de relacionamento com cliente

## 📈 Como Usar

### Passo 1: Seleção do Pagador
1. **Pagador Existente**: Escolha da lista de pagadores cadastrados
2. **Novo Pagador**: Insira um novo ID de pagador

### Passo 2: Visualização do Histórico (Para Pagadores Existentes)
- Métricas resumidas aparecem automaticamente
- Histórico detalhado de todos os boletos
- Análise de comportamento de pagamento

### Passo 3: Predição para Novo Boleto
1. Preencha os dados obrigatórios:
   - Número do boleto
   - Valor original
   - Data de inclusão
   - Data de vencimento
   - IDs do grupo e beneficiário

2. Clique em "Fazer Predição de Inadimplência"

3. Analise os resultados:
   - Classificação de risco
   - Probabilidade percentual
   - Predição final (Adimplente/Inadimplente)
   - Recomendações específicas

## 🎯 Interpretação dos Resultados

### Métricas Principais
- **Probabilidade**: Percentual de chance de inadimplência (0-100%)
- **Classificação**: Baixo, Médio ou Alto risco
- **Predição**: Adimplente (≤50%) ou Inadimplente (>50%)

### Ações Recomendadas por Nível de Risco

#### 🔴 ALTO (>70%)
- Contato imediato com o cliente
- Oferecimento de condições especiais de pagamento
- Redução preventiva de limite de crédito
- Implementação de cobrança preventiva

#### 🟡 MÉDIO (30-70%)
- Monitoramento próximo do comportamento
- Envio de lembretes próximo ao vencimento
- Análise adicional do perfil do cliente
- Acompanhamento de tendências

#### 🟢 BAIXO (<30%)
- Processo padrão de cobrança
- Cliente considerado confiável
- Possibilidade de ofertas de produtos adicionais
- Manutenção do relacionamento

## 📊 Dados Utilizados

### Features Principais
- **Valor do boleto**: Valor original da cobrança
- **Dias para vencimento**: Prazo entre emissão e vencimento
- **Dados temporais**: Mês, ano, dia da emissão e vencimento
- **Histórico do pagador**: Comportamento passado (quando disponível)

### Features Históricas (Para Pagadores Existentes)
- Quantidade de cobranças anteriores
- Valor médio histórico
- Taxa de inadimplência histórica
- Taxa de atraso histórica
- Desvio padrão dos valores
- Tempo desde primeira cobrança

## ⚙️ Especificações Técnicas

### Modelo de Machine Learning
- **Algoritmo**: RandomForestClassifier
- **Acurácia**: 96.44%
- **Recall**: 92.5%
- **Precision**: 91%
- **F1-Score**: 92%

### Tecnologias
- **Backend**: Flask/Streamlit + Python
- **Machine Learning**: Scikit-learn
- **Dados**: Pandas + NumPy
- **Frontend**: Bootstrap + HTML/CSS/JavaScript
- **Serialização**: Joblib

### Arquivos Necessários
```
├── app_flask.py                           # Aplicação Flask
├── app_predicao_inadimplencia.py         # Aplicação Streamlit
├── templates/index.html                   # Interface web
├── requirements_flask.txt                 # Dependências Flask
├── requirements_app.txt                   # Dependências Streamlit
├── iniciar_app.bat                       # Script Windows
├── iniciar_app.ps1                       # Script PowerShell
├── notebook/modelos salvos/
│   └── modelo_bill_hunters_latest.joblib # Modelo treinado
└── dados/
    └── dados_treino_com_predicoes.csv    # Dados históricos
```

## 🔧 Troubleshooting

### ❌ "Modelo não encontrado"
**Solução**: Verifique se o arquivo `modelo_bill_hunters_latest.joblib` está em `notebook/modelos salvos/`

### ❌ "Dados não encontrados"  
**Solução**: Confirme se `dados_treino_com_predicoes.csv` está na pasta `dados/`

### ❌ Erro de dependências
**Solução**: 
```bash
pip install --upgrade pip
pip install -r requirements_flask.txt
```

### ❌ Erro de porta ocupada
**Solução**: 
- Flask: Mude a porta no arquivo `app_flask.py` (linha final)
- Streamlit: Use `streamlit run app_predicao_inadimplencia.py --server.port 8502`

### ❌ Erro de memória
**Solução**: Para datasets muito grandes, considere usar amostragem dos dados históricos

## 🔒 Considerações de Segurança

- ✅ Validação de entrada de dados
- ✅ Tratamento de erros robusto  
- ✅ Logs de predições (em desenvolvimento)
- ⚠️ **Importante**: Esta é uma versão de demonstração. Para produção, implemente:
  - Autenticação de usuários
  - Criptografia de dados sensíveis
  - Auditoria de acessos
  - Rate limiting

## 📈 Próximas Versões

- [ ] Dashboard gerencial com métricas agregadas
- [ ] Integração com APIs de bancos de dados
- [ ] Sistema de alertas automáticos por email/SMS
- [ ] Módulo de retreinamento automático
- [ ] Exportação de relatórios (PDF/Excel)
- [ ] API REST para integração com outros sistemas
- [ ] Análise de tendências temporais
- [ ] Segmentação automática de clientes

## 📞 Suporte

**Equipe**: Bill Hunters  
**Projeto**: Sistema de Predição de Inadimplência  
**Cliente**: Finnet Corp  
**Ano**: 2025

Para suporte técnico, consulte a documentação completa no notebook `modelo_definitivo.ipynb` ou entre em contato com a equipe de desenvolvimento.

---

**⚡ Quick Start:**
1. Execute `iniciar_app.bat` (Windows) ou `python app_flask.py`
2. Acesse http://localhost:5000
3. Selecione um pagador existente ou crie um novo
4. Preencha os dados do boleto
5. Clique em "Fazer Predição"
6. Analise os resultados e recomendações