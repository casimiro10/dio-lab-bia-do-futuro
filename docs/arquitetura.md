# Arquitetura do CopaCast ⚽🏆

O projeto foi desenvolvido utilizando a linguagem Python e a API do Groq para processamento de linguagem natural, criando um assistente conversacional focado em dados esportivos.

## Estrutura e Componentes
* **Assistente (`src/assistente.py`)**: Arquivo principal contendo a lógica de conversação, o sistema de prompt e a conexão com o modelo LLM (Llama 3).
* **Base de Conhecimento (`data/copa_mundo.json`)**: Arquivo com os dados estruturados sobre as edições da Copa do Mundo, atuando como o cérebro de informações do assistente para evitar alucinações.
* **Variáveis de Ambiente (`.env`)**: Arquivo responsável por armazenar a chave da API com segurança, devidamente ignorado pelo Git.