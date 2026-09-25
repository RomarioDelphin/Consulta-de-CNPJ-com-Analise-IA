<div align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&height=250&section=header&text=FISCAL%20RISK%20AI&fontSize=60&fontAlignY=35&desc=Compliance%20Engine%20|%20An%C3%A1lise%20Preditiva%20de%20CNPJ&descAlignY=55&descSize=18&fontColor=ffffff&customColorList=06b6d4,000205&animation=fadeIn" width="100%"/>
</div>

<div align="center">
  <br />
  
  <a href="https://github.com/RomarioDelphin">
    <img src="https://img.shields.io/badge/DEV-ROMARIO%20DELPHIN-000205?style=for-the-badge&logo=github&logoColor=06b6d4&labelColor=000205&color=06b6d4" />
  </a>
  <img src="https://img.shields.io/badge/BACKEND-PYTHON%20FLASK-000205?style=for-the-badge&logo=flask&logoColor=ffffff&labelColor=000205&color=000000" />
  <img src="https://img.shields.io/badge/AI-RISK%20ANALYSIS-000205?style=for-the-badge&logo=openai&logoColor=00ff9d&labelColor=000205&color=00ff9d" />

</div>

<br />

## ⚡ Sobre o Projeto

O **Fiscal Risk AI** é um protótipo de consulta de CNPJ com interface web, backend Flask e classificação indicativa baseada em duas regras explícitas.

O backend consulta a API ReceitaWS e sinaliza quando a situação cadastral não está ativa ou quando a empresa tem menos de um ano de abertura. Não há modelo de aprendizado de máquina, avaliação de risco de crédito ou validação para tomada de decisões comerciais. A consulta depende da disponibilidade e das condições da API externa.

### 🎯 Funcionalidades Core
* **🌡️ Sinalização por regras:** Situação cadastral diferente de `ATIVA` recebe alerta vermelho; abertura há menos de um ano, alerta laranja. Outros casos recebem verde. Capital social não participa da classificação.
* **🔌 Backend Flask:** Repassa dados da API externa e acrescenta a sinalização. A configuração atual habilita CORS amplo e modo debug ao executar diretamente; requer revisão antes de qualquer implantação pública.
* **📑 Dados cadastrais:** A interface exibe campos retornados pela API, cuja cobertura e atualidade devem ser conferidas na fonte.
* **🖥️ Interface Reativa:** Frontend limpo e responsivo para uso corporativo.

---

## 🛠️ Stack Tecnológica

A arquitetura evoluiu de um simples frontend para uma solução robusta de Engenharia de Software.

<div align="center">
  <img src="https://skillicons.dev/icons?i=python,flask,html,css,js&perline=10" />
</div>

| Camada | Tecnologia | Função |
| :--- | :--- | :--- |
| **Backend** | `Python 3 + Flask` | Consulta à API externa e aplicação das duas regras. |
| **Frontend** | `Vanilla JS + CSS3` | Interface do Usuário e Renderização Dinâmica. |
| **Integração** | `Requests + CORS` | Requisição à API externa e liberação de acesso do navegador. |
| **Dados** | `ReceitaWS` | Serviço de terceiros consultado pelo protótipo. |

---

## 🚀 Como Rodar o Projeto

Siga os passos abaixo para executar a aplicação Full-Stack em seu ambiente local.

### 📋 Pré-requisitos
* Python 3.10 ou superior.
* Git instalado.

### 1. Instalação

```bash
# Clone o repositório
git clone https://github.com/RomarioDelphin/Consulta-de-CNPJ-com-Analise-IA.git

# Entre na pasta
cd Consulta-de-CNPJ-com-Analise-IA

# Crie um ambiente virtual (Recomendado)
python -m venv venv

# Ative o ambiente:
# No Windows:
.\venv\Scripts\activate
# No Linux/Mac:
# source venv/bin/activate

# Instale as dependências
pip install -r requirements.txt

```

### 2. Execução (Backend)

```bash
# Inicie o servidor Flask
python app.py

```

*O terminal exibirá: `Running on http://127.0.0.1:5000/`. Mantenha esta janela aberta.*

### 3. Execução (Frontend)

* Vá até a pasta do projeto.
* Abra o arquivo `index.html` no seu navegador.
* Digite um CNPJ para consultar os dados e ver os alertas produzidos pelas duas regras.

---

## 📈 Evolução do Projeto

Este protótipo demonstra a evolução de uma interface estática para uma aplicação com backend e regras explícitas.

A sinalização é indicativa e não mede inadimplência, capacidade de pagamento nem confiabilidade de parceiros. Para uso operacional, seria necessário validar a fonte, tratar privacidade e erros, definir critérios com especialistas e testar a solução com dados adequados.

---

<div align="center">
<p>Desenvolvido por <strong>Romário Delphin</strong>.</p>
</div>
