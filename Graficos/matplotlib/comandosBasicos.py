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
