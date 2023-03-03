#%%
import pandas as pd
import numpy as np

path = "JugadoresSeleccion.xlsx"
pd.read_excel(path)
path2 = "JugadoresSeleccion_2.xlsx"
pd.read_excel(path2, sheet_name="segunda hoja")

jugadores = pd.read_excel(path)
print(jugadores["Nombre"])
print(jugadores[jugadores['Nombre'] == "Lionel"])



# %%
path = "JugadoresSeleccion.xlsx"
jugadores = pd.read_excel(path)
promEdad= sum(jugadores["Edad"])/len(jugadores["Edad"])
print(f'El promedio de edad es de: {promEdad}')
maschicos = jugadores[jugadores['Edad']<=promEdad]
masgrandes = jugadores[jugadores['Edad']>=promEdad]
print(f'Lo mas chicos son: ')
print(maschicos)
print()
print(f'los mas grandes son:')
print(masgrandes)

# %%
import matplotlib.pyplot as plt

plt.figure()

# %%
fig = plt.Figure()
# ax.set(title='An Axes Title', xlim=[0.5, 4.5], ylim=[-3, 7], ylabel='Y-Axis Label', xlabel='X-Axis Label')
plt.show()
# %%
x = [1.3, 2.9, 3.1, 4.7, 5.6, 6.5, 7.4, 8.8, 9.2, 10]
y = [95, 42, 69, 11, 49, 32, 74, 62, 25, 32]
plt.plot(x, y)
plt.xlabel('X-axis Label')
plt.ylabel('Y-axis Label')
plt.show()
# %%
path = "JugadoresSeleccion.xlsx"
jugadores = pd.read_excel(path)

promEdad= sum(jugadores["Edad"])/len(jugadores["Edad"])

maschicos = jugadores[jugadores['Edad']<=promEdad]
xc = maschicos["Nombre"]
yc = maschicos["Edad"]


masgrandes = jugadores[jugadores['Edad']>=promEdad]
xg = masgrandes["Nombre"]
yg = masgrandes["Edad"]

plt.plot(xc, yc)
plt.plot(xg,yg)

plt.xlabel('Jugadores')
plt.ylabel('Edad')

plt.show()
# %%
path = "JugadoresSeleccion.xlsx"
jugadores = pd.read_excel(path)

promEdad= sum(jugadores["Edad"])/len(jugadores["Edad"])

plt.plot(jugadores["Apellido"],jugadores["Edad"])
plt.plot([promEdad]*len(jugadores))

plt.xlabel('Jugadores')
plt.ylabel('Edad')

plt.show()

# %%
