# ⚽ CopaCast: Assistente Virtual da Copa do Mundo

Este projeto é um assistente virtual interativo especializado em dados da Copa do Mundo FIFA. Construído com Python e integrado com a inteligência artificial do Groq, o CopaCast responde perguntas usando uma base de conhecimento local em JSON, garantindo precisão e evitando alucinações.

## 🚀 Funcionalidades
* **Respostas Baseadas em Fatos:** Utiliza dados estruturados sobre as Copas para fornecer respostas corretas.
* **Integração com LLM:** Usa a API ultrarrápida do Groq (modelo Llama 3) para processamento de linguagem natural.
* **Interface Via Terminal:** Chat interativo direto no console.
* **Personalidade:** O assistente age como um comentarista esportivo animado.

## 📁 Estrutura do Projeto
* `src/`: Código principal do assistente (`assistente.py`).
* `data/`: Base de conhecimento em JSON (`copa_mundo.json`).
* `docs/`: Documentação sobre a arquitetura do projeto.

## 🛠️ Como rodar o projeto localmente
1. Clone este repositório.
2. Crie um arquivo `.env` na raiz do projeto e adicione sua chave de API:
   `GROQ_API_KEY=sua_chave_aqui`
3. Instale as dependências (Groq e python-dotenv).
4. Execute o assistente com o comando:
   `python src/assistente.py`