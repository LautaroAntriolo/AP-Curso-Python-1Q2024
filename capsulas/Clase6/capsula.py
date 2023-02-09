#%%
import pandas as pd 
datafram = pd.DataFrame([[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5]])
serie = pd.Series([1,2,3,4,5])
print(type(serie.values))
print(datafram)

# Todos los datos que obtengamos con Pandas los vamos a obtener en este formato
path = "JugadoresSeleccion_2.xlsx"
jugadores = pd.read_excel(path, sheet_name="segunda hoja")

# print(jugadores["Nombre"])
# print(jugadores[jugadores['Nombre'] == "Lionel"])
# %%
# print(jugadores["Edad"]) #Obtengo los valores y su indice
print(jugadores["Edad"].values) #Obtengo solo los valores
promEdad= sum(jugadores["Edad"])/len(jugadores["Edad"])
print(promEdad)
orden = jugadores["Edad"].sort_values(ascending=True) # Obtengo en orden la edad de los jugadores
print(len(orden))
#%%
import matplotlib.pyplot as plt
promEdad= sum(jugadores["Edad"])/len(jugadores["Edad"])

plt.plot(jugadores["Apellido"],jugadores["Edad"])
plt.plot([promEdad]*len(jugadores))

plt.xlabel('Jugadores')
plt.ylabel('Edad')

plt.show()
# %%
