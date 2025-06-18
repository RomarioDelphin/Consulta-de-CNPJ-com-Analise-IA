# Consulta de CNPJ com Análise de Risco por IA

Este projeto é uma aplicação web full-stack que vai além de uma simples consulta de dados. Ele utiliza um backend em Python (Flask) para consumir a API da ReceitaWS e aplicar uma camada de inteligência, gerando uma análise de risco simplificada ("Termômetro IA") em tempo real.

![Demo do Projeto]

---

## ✨ Funcionalidades Principais

-   **Análise de Risco com IA ("Termômetro do CNPJ"):** O sistema analisa os dados retornados pela API (como situação cadastral e idade da empresa) e, através de um sistema de regras, classifica a "saúde" do CNPJ em `Saudável`, `Ponto de Atenção` ou `Risco Elevado`.
-   **Backend Robusto em Python:** Substituição de proxies de CORS não confiáveis por um servidor Flask local, que gerencia as chamadas de API de forma segura e profissional, abrindo portas para lógicas complexas.
-   **Consulta de Dados Completos:** Exibição de todas as informações públicas de um CNPJ, incluindo dados cadastrais, atividade principal, endereço, quadro de sócios e administradores.
-   **Interface Web Reativa:** Uma interface de usuário limpa e simples construída com HTML, CSS e JavaScript vanilla.

---

## 🛠️ Arquitetura e Tecnologias

-   **Frontend:** HTML5, CSS3, JavaScript (Vanilla JS)
-   **Backend:** Python 3, Flask, Flask-CORS, Requests
-   **Análise de IA:** Lógica de negócios e sistema de regras em Python
-   **API Externa:** [ReceitaWS](https://www.receitaws.com.br/)

---

## 🚀 Como Rodar o Projeto

Siga os passos abaixo para executar o projeto em seu ambiente local.

### Pré-requisitos
-   [Python 3.10+](https://www.python.org/downloads/)
-   [Git](https://git-scm.com/downloads)

### Instalação e Execução

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/RomarioDelphin/consultacnpj.git](https://github.com/RomarioDelphin/consultacnpj.git)
    ```

2.  **Navegue até a pasta do projeto:**
    ```bash
    cd consultacnpj
    ```

3.  **Crie e ative um ambiente virtual:**
    ```bash
    # Criar o ambiente
    python -m venv venv

    # Ativar no Windows
    .\venv\Scripts\activate

    # Ativar no Mac/Linux
    # source venv/bin/activate
    ```

4.  **Instale as dependências do Python:**
    ```bash
    pip install -r requirements.txt
    ```

5.  **Inicie o servidor backend:**
    ```bash
    python app.py
    ```
    O terminal mostrará que o servidor está rodando em `http://127.0.0.1:5000/`. Deixe este terminal aberto.

6.  **Abra o frontend:**
    Abra o arquivo `index.html` em seu navegador de preferência.

Agora você pode inserir um CNPJ e testar a aplicação completa, incluindo a análise de IA!

---

## Evolução do Projeto

Este projeto evoluiu de uma simples aplicação frontend para uma solução full-stack, demonstrando a capacidade de construir não apenas interfaces, mas também a lógica de servidor e a implementação de regras de negócio inteligentes. A camada de "Termômetro IA" é o primeiro passo para análises mais complexas que podem ser desenvolvidas futuramente.
