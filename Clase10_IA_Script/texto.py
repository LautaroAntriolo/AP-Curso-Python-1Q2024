import openai
def prompt():
  openai.api_key = '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'
  preg_men = input("Escribí tu pregunta acá: \n")
  response = openai.Completion.create(
    model="text-davinci-003",
    prompt=f'{preg_men}',
    temperature=0.99,
    max_tokens=1500,
    top_p=1,
    frequency_penalty=0.6,
    presence_penalty=0.0,
  )
  rta = response.choices[0].text.strip()
  return (f'{rta}')


mensaje = prompt()
print(mensaje)


