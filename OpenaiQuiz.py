from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

# Aqui vamos escolher o tema do quiz.
tema = input("Escolha o tema: ")

messages = [{"role": "system", "content": f"Você é um mestre de quiz que faz perguntas sobre o {tema}"},
            {"role": "system", "content" : "Faça perguntas no modelo de 4 alternativas."}]

MAX_PERGUNTAS = 5
MAX_TOKENS = 150

for i in range(MAX_PERGUNTAS):

    messages.append({"role": "user", "content": f"Faça uma nova pergunta sobre o {tema}"})
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        max_tokens=MAX_TOKENS
    )
    
    pergunta = response.choices[0].message.content
    print(f"\nPergunta {i+1}: {pergunta}")
    
    messages.append({"role": "assistant", "content": pergunta})
    
    resposta_usuario = input("Sua resposta: ")
    messages.append({"role": "user", "content": f"Avalie esta resposta: '{resposta_usuario}'"})
    
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        max_tokens=MAX_TOKENS
    )
    
    feedback = response.choices[0].message.content
    print("Feedback do modelo:", feedback)
    messages.append({"role": "assistant", "content": feedback})

messages.append({"role": "user", "content": "Mostre uma contagem, mostrando quantos acertos o usuário conseguiu"})

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=messages,
    max_tokens=MAX_TOKENS
    )

feedback_geral = response.choices[0].message.content
messages.append({"role": "assistant", "content": feedback_geral})
print(feedback_geral)    
