from flask import Flask, render_template, request, jsonify
import pandas as pd
import numpy as np
from datetime import datetime
import json

app = Flask(__name__)

# Dados hardcoded para 3 pagadores específicos
PAGADORES_DATA = {
    "2793444": {
        "nome": "João Silva",
        "perfil_risco": "Baixo Risco",
        "total_boletos": 15,
        "inadimplencia_historica": 0.1,
        "valor_medio": 1500.00,
        "historico": [
            {"data": "2024-01-15", "valor": 1200.00, "status": "Em Dia"},
            {"data": "2024-02-15", "valor": 1500.00, "status": "Em Dia"},
            {"data": "2024-03-15", "valor": 1300.00, "status": "Atraso"},
            {"data": "2024-04-15", "valor": 1600.00, "status": "Em Dia"},
            {"data": "2024-05-15", "valor": 1400.00, "status": "Em Dia"},
        ]
    },
    "4606075": {
        "nome": "Maria Santos",
        "perfil_risco": "Médio Risco",
        "total_boletos": 20,
        "inadimplencia_historica": 0.4,
        "valor_medio": 2500.00,
        "historico": [
            {"data": "2024-01-20", "valor": 2200.00, "status": "Em Dia"},
            {"data": "2024-02-20", "valor": 2800.00, "status": "Atraso"},
            {"data": "2024-03-20", "valor": 2500.00, "status": "Inadimplente"},
            {"data": "2024-04-20", "valor": 2300.00, "status": "Em Dia"},
            {"data": "2024-05-20", "valor": 2700.00, "status": "Atraso"},
        ]
    },
    "5362811": {
        "nome": "Carlos Oliveira",
        "perfil_risco": "Alto Risco",
        "total_boletos": 12,
        "inadimplencia_historica": 0.8,
        "valor_medio": 4500.00,
        "historico": [
            {"data": "2024-01-25", "valor": 4200.00, "status": "Inadimplente"},
            {"data": "2024-02-25", "valor": 4800.00, "status": "Inadimplente"},
            {"data": "2024-03-25", "valor": 4500.00, "status": "Atraso"},
            {"data": "2024-04-25", "valor": 4300.00, "status": "Inadimplente"},
            {"data": "2024-05-25", "valor": 4700.00, "status": "Em Dia"},
        ]
    }
}

def calcular_predicao_simples(pagador_id, valor_boleto, dias_vencimento):
    """Função simples para calcular risco de inadimplência"""
    pagador_data = PAGADORES_DATA.get(str(pagador_id))
    if not pagador_data:
        return 0.5, "Médio"
    
    # Base risk from historical data
    base_risk = pagador_data["inadimplencia_historica"]
    
    # Adjust based on value vs average
    valor_medio = pagador_data["valor_medio"]
    if valor_boleto > valor_medio * 1.5:
        base_risk += 0.2
    elif valor_boleto < valor_medio * 0.5:
        base_risk -= 0.1
    
    # Adjust based on days to payment
    if dias_vencimento < 10:
        base_risk += 0.2
    elif dias_vencimento > 30:
        base_risk -= 0.1
    
    # Ensure it's between 0 and 1
    risk_score = max(0.05, min(0.95, base_risk))
    
    # Classify risk
    if risk_score < 0.3:
        categoria = "Baixo"
    elif risk_score < 0.6:
        categoria = "Médio"
    else:
        categoria = "Alto"
    
    return risk_score, categoria

@app.route('/')
def index():
    return render_template('index_simples.html')

@app.route('/api/pagadores')
def get_pagadores():
    """Retorna lista de pagadores disponíveis"""
    pagadores_list = []
    for pagador_id, data in PAGADORES_DATA.items():
        pagadores_list.append({
            'id': pagador_id,
            'nome': data['nome'],
            'perfil_risco': data['perfil_risco'],
            'total_boletos': data['total_boletos'],
            'valor_medio': data['valor_medio'],
            'inadimplencia_historica': data['inadimplencia_historica'] * 100
        })
    
    return jsonify(pagadores_list)

@app.route('/api/pagador/<pagador_id>')
def get_pagador_detalhes(pagador_id):
    """Retorna detalhes de um pagador específico"""
    pagador_data = PAGADORES_DATA.get(pagador_id)
    if not pagador_data:
        return jsonify({'error': 'Pagador não encontrado'}), 404
    
    return jsonify({
        'id': pagador_id,
        'nome': pagador_data['nome'],
        'perfil_risco': pagador_data['perfil_risco'],
        'total_boletos': pagador_data['total_boletos'],
        'valor_medio': pagador_data['valor_medio'],
        'inadimplencia_historica': pagador_data['inadimplencia_historica'] * 100,
        'historico': pagador_data['historico']
    })

@app.route('/api/predict', methods=['POST'])
def predict_inadimplencia():
    """Faz predição de inadimplência para um novo boleto"""
    try:
        data = request.get_json()
        
        pagador_id = data.get('pagador_id')
        valor_boleto = float(data.get('valor_boleto', 0))
        dias_vencimento = int(data.get('dias_vencimento', 30))
        
        if not pagador_id or pagador_id not in PAGADORES_DATA:
            return jsonify({'error': 'Pagador inválido'}), 400
        
        # Calculate prediction
        risk_score, categoria_risco = calcular_predicao_simples(pagador_id, valor_boleto, dias_vencimento)
        
        # Get payer info
        pagador_info = PAGADORES_DATA[pagador_id]
        
        result = {
            'pagador_id': pagador_id,
            'pagador_nome': pagador_info['nome'],
            'valor_boleto': valor_boleto,
            'dias_vencimento': dias_vencimento,
            'probabilidade_inadimplencia': round(risk_score * 100, 2),
            'categoria_risco': categoria_risco,
            'recomendacao': get_recomendacao(categoria_risco, risk_score),
            'detalhes': {
                'perfil_historico': pagador_info['perfil_risco'],
                'inadimplencia_historica': round(pagador_info['inadimplencia_historica'] * 100, 2),
                'valor_medio_historico': pagador_info['valor_medio'],
                'relacao_valor': round((valor_boleto / pagador_info['valor_medio']) * 100, 2)
            }
        }
        
        return jsonify(result)
    
    except Exception as e:
        return jsonify({'error': f'Erro na predição: {str(e)}'}), 500

def get_recomendacao(categoria_risco, probabilidade):
    """Retorna recomendação baseada no risco"""
    if categoria_risco == "Baixo":
        return "Risco baixo. Acompanhamento padrão."
    elif categoria_risco == "Médio":
        return "Risco moderado. Considere contato proativo 5 dias antes do vencimento."
    else:
        return "Alto risco! Recomenda-se contato imediato e acompanhamento próximo."

if __name__ == '__main__':
    print("=== APLICAÇÃO SUPER SIMPLES DE PREDIÇÃO DE INADIMPLÊNCIA ===")
    print("\nDados carregados para 3 pagadores:")
    for pid, pdata in PAGADORES_DATA.items():
        print(f"  - ID {pid}: {pdata['nome']} ({pdata['perfil_risco']})")
    
    print("\nAplicação iniciando em: http://localhost:5000")
    print("API endpoints disponíveis:")
    print("  - GET  /api/pagadores")
    print("  - GET  /api/pagador/<id>")
    print("  - POST /api/predict")
    
    app.run(debug=True, port=5000)