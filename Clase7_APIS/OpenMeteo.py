#%%
import requests
#%%
# En la APi tenemos que buscar las coordenadas de Bs As
# # y reemplazar

latitud,longitud = 28.4578025, -16.3563748
params = dict(latitude=latitud, longitude=longitud, hourly='temperature_2m')
url = 'https://api.open-meteo.com/v1/forecast'
#%%

response = requests.get(url, params=params)

#Agregamos la url correcta, los detalles van despues del signoo ? 
# ?latitude=28.4578025&longitude=-16.3563748&hourly=temperature_2m'

# response.url
# 'https://api.open-meteo.com/v1/forecast?latitude=28.4578025&longitude=-16.3563748&hourly=temperature_2m'


data = response.json()

print(type(data)) # dict
#%%
# Nosotros
print(data.keys())

# %%
temperatures = data['hourly']['temperature_2m']

# Las temperaturas también incluyen el día de hoy
for i, temp in enumerate(temperatures[24:48], start=1):
    print(f'{temp:4.1f}', end=' ')
    if i % 6 == 0:
        print()
        print(i)
# %%
import requests
# En la APi tenemos que buscar las coordenadas de Bs As
# # y reemplazar

latitud,longitud = 28.4578025, -16.3563748
params = dict(latitude=latitud, longitude=longitud, hourly='temperature_2m')
url = 'https://api.open-meteo.com/v1/forecast'

response = requests.get(url, params=params)
print(type(response)) # <class 'requests.models.Response'>
data = response.json()
print(type(data)) # dict

temperaturas = data['hourly']['temperature_2m']
print(temperaturas)
# Las temperaturas también incluyen el día de hoy
for i, temp in enumerate(temperaturas[23:49], start=1):
    print(f'{temp:4.1f}', end=' ')
    if i % 6 == 0:
        print()
# %%
