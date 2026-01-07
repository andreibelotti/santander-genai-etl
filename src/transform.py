from openai import OpenAI
from config.settings import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)

def generate_marketing_message(user):
    nome = user["name"]

    prompt = f"""
    Crie uma mensagem curta e personalizada de marketing bancário
    para o cliente {nome}, destacando a importância dos investimentos.
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Especialista em marketing financeiro."},
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content
