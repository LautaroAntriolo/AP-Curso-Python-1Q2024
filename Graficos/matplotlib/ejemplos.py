##################### EJEMPLOS ##################### 
#%% Gráfico lineal común
# Importar la librería matplotlib
import matplotlib.pyplot as plt
import numpy as np

# Crear un array de valores x para la función
x = np.linspace(0, 10, 100)

# Crear un array de valores y para la función
y = np.sin(x)

# Crear el gráfico
plt.plot(x, y)

# Agregar títulos y etiquetas
plt.title("Función seno")
plt.xlabel("Valores de x")
plt.ylabel("Valores de y")

# Mostrar el gráfico
plt.show()
#%% Gráfco de dispersión con tamaño y color personalizado

# Importar la librería matplotlib
import matplotlib.pyplot as plt
import numpy as np

# Crear un array de valores x y y para los puntos
x = np.random.rand(50)
y = np.random.rand(50)

# Crear un array de valores de tamaño para los puntos
size = np.random.randint(10, 100, size=50)

# Crear un array de valores de color para los puntos
color = np.random.rand(50)

# Crear el gráfico
plt.scatter(x, y, s=size, c=color)

# Agregar títulos y etiquetas
plt.title("Gráfico de dispersión")
plt.xlabel("Valores de x")
plt.ylabel("Valores de y")

# Mostrar el gráfico
plt.show()

#%% Gráfico de barras horizontales con etiquetas personalizadas

# Importar la librería matplotlib
import matplotlib.pyplot as plt

# Crear un array de valores para las barras
values = [10, 8, 6, 4, 2]

# Crear un array de etiquetas para las barras
labels = ["A", "B", "C", "D", "E"]

# Crear el gráfico
plt.barh(range(len(values)), values, tick_label=labels)

# Agregar títulos y etiquetas
plt.title("Gráfico de barras horizontal")
plt.xlabel("Valores")
plt.ylabel("Etiquetas")

# Mostrar el gráfico
plt.show()

#%% GRáfico de pastel con porcentajes y sombras

# Importar la librería matplotlib
import matplotlib.pyplot as plt

# Crear un array de valores para los sectores
values = [25, 40, 20, 15]

# Crear un array de etiquetas para los sectores
labels = ["A", "B", "C", "D"]
shadows = [0.1, 0, 0, 0]

# Crear el gráfico
plt.pie(values, labels=labels, autopct="%1.1f%%", shadow=True, startangle=90, explode=shadows)
 
#Agregamos el título
plt.title("Gráfico de pastel con porcentajes y sombras")
plt.show()


# %%
