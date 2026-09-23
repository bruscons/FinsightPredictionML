# Bill Hunters - Dashboard de Predição de Inadimplência

## 🚀 Como Executar

### Opção 1: Execução Automática
```bash
cd frontend
python run.py
```

### Opção 2: Execução Manual
```bash
cd frontend
pip install -r requirements.txt
streamlit run app.py
```

## 📊 Funcionalidades

- **Dashboard Interativo**: Visualização completa dos dados de predição
- **Filtros Dinâmicos**: Filtre por tipo de dados, status e predições
- **Métricas em Tempo Real**: Acurácia, recall, precision e F1-score
- **Gráficos Interativos**: Distribuições, análises temporais e correlações
- **Análise de Features**: Importância das variáveis no modelo
- **Download de Dados**: Exporte os resultados em CSV

## 🎯 Métricas Disponíveis

- Taxa de Inadimplência
- Acurácia do Modelo
- Recall para Inadimplentes
- Precision e F1-Score
- Distribuição de Probabilidades
- Análise Temporal
- Importância das Features

## 📁 Estrutura

```
frontend/
├── app.py              # Aplicação principal Streamlit
├── run.py              # Script de execução automática
├── requirements.txt    # Dependências Python
└── README.md          # Este arquivo
```

## 🌐 Acesso

Após executar, acesse: http://localhost:8501
