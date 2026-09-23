# 🚀 FINNET BILL HUNTERS - Deploy Vercel

## Estrutura Final para Deploy

Esta é a versão limpa e otimizada para deploy no Vercel com apenas os arquivos essenciais.

### 📁 Arquivos Principais:

- **`app.py`** - Aplicação Flask principal
- **`app_super_simples.py`** - Versão local (backup)
- **`templates/index_simples.html`** - Interface web
- **`requirements.txt`** - Dependências Python
- **`vercel.json`** - Configuração do Vercel
- **`.vercelignore`** - Arquivos ignorados no deploy

### 📦 Para Deploy no Vercel:

1. **Conectar ao Git**: Faça push para um repositório GitHub
2. **Importar no Vercel**: Conecte o repositório
3. **Deploy Automático**: O Vercel detectará o `vercel.json`

### 🎯 Funcionalidades:

- ✅ 3 pagadores com perfis de risco diferentes
- ✅ Predição de inadimplência em tempo real
- ✅ Interface moderna com tema escuro
- ✅ Dashboard com métricas
- ✅ Footer profissional
- ✅ Design responsivo

### 🔧 Tecnologias:

- **Backend**: Flask + Python
- **Frontend**: HTML5 + Bootstrap + JavaScript
- **Deploy**: Vercel Serverless

### 📊 Pagadores Disponíveis:

- **João Silva** (ID: 2793444) - Baixo Risco
- **Maria Santos** (ID: 4606075) - Médio Risco  
- **Carlos Oliveira** (ID: 5362811) - Alto Risco

### 🌐 Endpoints da API:

- `GET /` - Interface principal
- `GET /api/pagadores` - Lista de pagadores
- `GET /api/pagador/<id>` - Detalhes do pagador
- `POST /api/predict` - Predição de inadimplência

Pronto para deploy! 🚀