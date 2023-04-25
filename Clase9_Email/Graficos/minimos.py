import numpy as np
import matplotlib.pyplot as plt

# Gráfico de lineas
x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 6, 8, 10])

plt.plot(x, y)
plt.show()

#Gráfico de dispersión 
x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 6, 8, 10])

plt.scatter(x, y)
plt.show()


# Gráfico de barras
x = np.array(["Manzana", "Naranja", "Banana", "Mango"])
y = np.array([20, 14, 22, 16])

plt.bar(x, y)
plt.show()

#Gráfico pastel 
labels = np.array(["Manzana", "Naranja", "Banana", "Mango"])
sizes = np.array([20, 14, 22, 16])

plt.pie(sizes, labels=labels)
plt.show()
