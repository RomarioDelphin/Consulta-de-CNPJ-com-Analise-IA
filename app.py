from flask import Flask, jsonify
from flask_cors import CORS
import requests
from datetime import datetime

app = Flask(__name__)
CORS(app)

def analisar_risco(data):
    """Função de IA baseada em regras para analisar os dados do CNPJ."""
    if data.get('status') == "ERROR":
        return {"saude": "Desconhecida", "cor": "grey", "detalhes": data.get('message')}

    pontos_atencao = []
    cor = "green"
    saude = "Saudável"

    if data.get('situacao') != "ATIVA":
        pontos_atencao.append("Situação cadastral não está ATIVA.")
        cor = "red"
    
    try:
        data_abertura = datetime.strptime(data.get('abertura'), '%d/%m/%Y')
        if (datetime.now() - data_abertura).days < 365:
            pontos_atencao.append("Empresa com menos de 1 ano de atividade.")
            if cor != "red": cor = "orange"
    except (ValueError, TypeError):
        pass

    if cor == "red":
        saude = "Risco Elevado"
    elif cor == "orange":
        saude = "Ponto de Atenção"

    return {"saude": saude, "cor": cor, "detalhes": " | ".join(pontos_atencao) if pontos_atencao else "Nenhum ponto de atenção detectado."}

@app.route('/consultar/<string:cnpj>')
def consultar_cnpj(cnpj):
    try:
        url = f"https://www.receitaws.com.br/v1/cnpj/{cnpj}"
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        
        # AQUI A MÁGICA ACONTECE: chamamos a função de análise
        analise_ia = analisar_risco(data)
        data['analise_ia'] = analise_ia
        
        return jsonify(data)
    except requests.exceptions.RequestException as e:
        return jsonify({"status": "ERROR", "message": f"Erro ao contatar a API: {e}"}), 500

if __name__ == '__main__':
    app.run(debug=True)