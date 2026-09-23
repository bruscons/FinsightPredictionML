# Sistema de Predição de Inadimplência - Finnet Corp
# Script de inicialização para PowerShell

Write-Host "===========================================" -ForegroundColor Blue
Write-Host " Sistema de Predicao de Inadimplencia" -ForegroundColor Blue
Write-Host " Finnet Corp - Bill Hunters" -ForegroundColor Blue
Write-Host "===========================================" -ForegroundColor Blue
Write-Host ""

Write-Host "Verificando arquivos necessarios..." -ForegroundColor Yellow

# Verificar se o modelo existe
if (-not (Test-Path "notebook\modelos salvos\modelo_bill_hunters_latest.joblib")) {
    Write-Host "ERRO: Modelo nao encontrado!" -ForegroundColor Red
    Write-Host "Verifique se o arquivo 'modelo_bill_hunters_latest.joblib' esta na pasta 'notebook\modelos salvos\'" -ForegroundColor Red
    Read-Host "Pressione Enter para sair"
    exit 1
}

# Verificar se os dados existem
if (-not (Test-Path "dados\dados_treino_com_predicoes.csv")) {
    Write-Host "ERRO: Dados nao encontrados!" -ForegroundColor Red
    Write-Host "Verifique se o arquivo 'dados_treino_com_predicoes.csv' esta na pasta 'dados\'" -ForegroundColor Red
    Read-Host "Pressione Enter para sair"
    exit 1
}

Write-Host "Arquivos OK!" -ForegroundColor Green
Write-Host ""

Write-Host "Instalando dependencias..." -ForegroundColor Yellow
pip install -r requirements_flask.txt

Write-Host ""
Write-Host "Iniciando aplicacao Flask..." -ForegroundColor Green
Write-Host "Acesse: http://localhost:5000" -ForegroundColor Cyan
Write-Host ""
Write-Host "Para parar a aplicacao, pressione Ctrl+C" -ForegroundColor Yellow
Write-Host ""

python app_flask.py