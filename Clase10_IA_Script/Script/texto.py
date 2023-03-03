import openai
import os
from dotenv import load_dotenv

load_dotenv()

def prompt(preg_men):
  openai.api_key = os.getenv('clave_API')
  response = openai.Completion.create(
    model="text-davinci-003",
    prompt=f'{preg_men}',
    temperature=0.99,
    max_tokens=20,
    top_p=1,
    frequency_penalty=0.6,
    presence_penalty=0.0,
  )
  rta = response.choices[0].text.strip()
  return (f'{rta}')

print(prompt('que es el agua'))