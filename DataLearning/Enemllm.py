from openai import OpenAI
from dotenv import load_dotenv
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def avaliar_redacao(texto_redacao: str) -> str:
    prompt = f"""
Você é um corretor do ENEM.
Avalie a redação abaixo nas 5 competências (0-200 cada), justificando e dando melhorias.
Devolva no formato:

C1: nota - justificativa
C2: nota - justificativa
C3: nota - justificativa
C4: nota - justificativa
C5: nota - justificativa
Total: soma
Melhorias: lista de 5 itens

REDAÇÃO:
{texto_redacao}
""".strip()

    resp = client.responses.create(
        model="gpt-4.1-mini",
        input=prompt
    )
    return resp.output_text

feedback = avaliar_redacao(redacoes[0])
print(feedback)