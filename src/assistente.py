import os
import json
from groq import Groq
from dotenv import load_dotenv

# Carregando a chave da API com segurança
env_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '.env')
load_dotenv(dotenv_path=env_path)

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("❌ GROQ_API_KEY não encontrada! Verifique seu arquivo .env.")

client = Groq(api_key=api_key)

# Carregando a base de conhecimento
def carregar_conhecimento():
    caminho = os.path.join(os.path.dirname(__file__), '..', 'data', 'copa_mundo.json')
    with open(caminho, 'r', encoding='utf-8') as f:
        return json.load(f)

# Criando o prompt do sistema
def criar_system_prompt(conhecimento):
    return f"""
Você é o CopaCast, um assistente virtual especializado em Copa do Mundo FIFA.

Seu objetivo é responder perguntas sobre a Copa do Mundo de forma clara, 
precisa e animada, como um comentarista esportivo!

Use APENAS as informações da base de conhecimento abaixo para responder.
Se não souber a resposta, diga: "Não tenho essa informação na minha base de dados."
Nunca invente informações!

BASE DE CONHECIMENTO:
{json.dumps(conhecimento, ensure_ascii=False, indent=2)}

REGRAS:
- Responda sempre em português
- Seja animado e use linguagem esportiva
- Seja direto e objetivo
- Use emojis relacionados ao futebol quando apropriado ⚽🏆🥇
"""

# Função principal do chat
def chat():
    conhecimento = carregar_conhecimento()
    system_prompt = criar_system_prompt(conhecimento)
    historico = []
    
    print("=" * 50)
    print("⚽ BEM-VINDO AO COPACAST! ⚽")
    print("Seu assistente virtual da Copa do Mundo!")
    print("Digite 'sair' para encerrar")
    print("=" * 50)
    
    while True:
        pergunta = input("\nVocê: ").strip()
        
        if pergunta.lower() == 'sair':
            print("\nCopaCast: Até a próxima! ⚽🏆")
            break
            
        if not pergunta:
            continue
        
        # Adicionando pergunta ao histórico
        historico.append({
            "role": "user",
            "content": pergunta
        })
        
        # Chamando a API do Groq
        resposta = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": system_prompt},
                *historico
            ]
        )
        
        # Pegando a resposta
        resposta_texto = resposta.choices[0].message.content
        
        # Adicionando resposta ao histórico
        historico.append({
            "role": "assistant", 
            "content": resposta_texto
        })
        
        print(f"\nCopaCast: {resposta_texto}")

# Rodando o assistente
if __name__ == "__main__":
    chat()