import requests

# #https://openweathermap.org
# Api key = 0779cf052efa2bd0ec9751d949a52a15

ciudad = input("Enter your city:  ")
API_key =  '0779cf052efa2bd0ec9751d949a52a15'
lang= 'sp' 
url = f'https://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={API_key}&units=metric&lang={lang}'  
Params = dict(city=ciudad,API_Key = API_key)
res = requests.post(url, params=Params)

data = res.json() 
print(data) 

temp_min = data["main"]["temp_min"]
temp_max = data["main"]["temp_max"]
vel_viento = data["wind"]["speed"]

latitud = data["coord"]["lat"]
longitud = data["coord"]["lon"]

descripcion = data["weather"][0]["description"]

print("Tempreratura minima: ", temp_min)
print("Tempreratura máxima: ", temp_max)
print(f"Velocidad del viento: {vel_viento} m/s")
print(f"Latitud: {latitud}")
print(f"Longitud: {longitud}")
print(f"Descripción: {descripcion}")




import matplotlib.pyplot as plt


