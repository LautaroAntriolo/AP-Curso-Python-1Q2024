import openai
def prompt(preg_men):
  openai.api_key = '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'
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

## Prueba de funcionalidad
mensaje = prompt("como sumar en python")
print(mensaje)
import os
clave = os.getenv("API_KEY")
print(clave)

