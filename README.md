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

O **Fiscal Risk AI** é uma aplicação Full-Stack desenvolvida para ir além da simples consulta de dados. Ela atua como uma ferramenta de **Compliance Automatizado**.

Diferente de consultas comuns, este sistema utiliza um Backend robusto em **Python (Flask)** para processar os dados brutos da Receita Federal e aplicar uma camada de inteligência ("Termômetro IA"). O algoritmo classifica a saúde fiscal da empresa em tempo real, permitindo tomada de decisão imediata para concessão de crédito ou parcerias.

### 🎯 Funcionalidades Core
* **🌡️ Termômetro de Risco IA:** Algoritmo proprietário que cruza dados (Idade da empresa, Capital Social, Situação Cadastral) para classificar o CNPJ em:
    * 🟢 **Saudável:** Seguro para negócios.
    * 🟡 **Ponto de Atenção:** Requer análise humana.
    * 🔴 **Risco Elevado:** Indícios de irregularidade ou baixa confiabilidade.
* **🔒 Backend Seguro:** Substituição de proxies instáveis por um servidor Flask que gerencia as requisições de forma segura.
* **📑 Dossiê Completo:** Extração detalhada de Sócios (QSA), Endereços e Atividade Econômica (CNAE).
* **🖥️ Interface Reativa:** Frontend limpo e responsivo para uso corporativo.

---

## 🛠️ Stack Tecnológica

A arquitetura evoluiu de um simples frontend para uma solução robusta de Engenharia de Software.

<div align="center">
  <img src="https://skillicons.dev/icons?i=python,flask,html,css,js&perline=10" />
</div>

| Camada | Tecnologia | Função |
| :--- | :--- | :--- |
| **Backend** | `Python 3 + Flask` | API Gateway, Regras de Negócio e Lógica de IA. |
| **Frontend** | `Vanilla JS + CSS3` | Interface do Usuário e Renderização Dinâmica. |
| **Integração** | `Requests + CORS` | Comunicação segura com APIs governamentais. |
| **Dados** | `ReceitaWS` | Fonte primária de dados públicos. |

---

## 🚀 Como Rodar o Projeto

Siga os passos abaixo para executar a aplicação Full-Stack em seu ambiente local.

### 📋 Pré-requisitos
* Python 3.10 ou superior.
* Git instalado.

### 1. Instalação

```bash
# Clone o repositório
git clone [https://github.com/RomarioDelphin/Consulta-de-CNPJ-com-Analise-IA.git](https://github.com/RomarioDelphin/Consulta-de-CNPJ-com-Analise-IA.git)

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
* Digite um CNPJ e veja a mágica da IA acontecer.

---

## 📈 Evolução do Projeto

Este software representa um marco na transição de **Frontend Development** para **Backend Engineering & Data Science**.

A implementação do "Termômetro IA" demonstra a capacidade de transformar dados brutos em **Informação Estratégica**, princípio fundamental da **RAM.IO Holdings**.

---

<div align="center">
<p>Desenvolvido por <strong>Romário Delphin</strong>.</p>
</div>
