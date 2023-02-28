#%% Gráficos Simples con matplotlib
import matplotlib.pyplot as plt
import numpy as np
#%% Gráficos de linea
# Acepta tanto tuplas como listas o arrays
# La principal diferencia entre las variables declaradas con () (TUPLAS) y [] (ARRAYS) es que las tuplas son colecciones ordenadas e inmutables de elementos, mientras que las listas son colecciones ordenadas y mutables de elementos.

# x = (4,8,13,17,20)
x = [4,8,13,17,20]
y = (54, 67, 98, 78, 45)


plt.plot(x,y)
plt.show()
# %% GRafico de dispersión

x = np.linspace(0,len(y),200)
y = [54,72,43,2,8,98,109,5,35,28,48,83,94,84,73,11,464,75,200,54]
plt.scatter(x,y)
plt.show()


# %%
