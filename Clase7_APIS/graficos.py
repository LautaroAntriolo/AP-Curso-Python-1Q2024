#%%
import matplotlib.pyplot as plt

tminima = [23.69, 23.96, 18.81, 19.58, 19.27, 20.43, 21.35, 22.49, 23.77, 20.34, 22.7, 20.47, 23.31, 22.0, 19.8]
tmaxima = [37.12, 25.2, 27.3, 29.24, 35.99, 37.72, 26.9, 37.48, 31.38, 30.78, 26.34, 30.32, 27.43, 31.03, 36.95]

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.plot(tminima, color='tab:orange')
ax.plot(tmaxima, color='tab:red')
# ax.set_xlim([0, 14,])
plt.xticks(range(0,15,1))
plt.yticks(range(17,40,3))
ax.grid()
plt.show
# %%
import matplotlib.pyplot as plt
import numpy as np

tminima = [23.69, 23.96, 18.81, 19.58, 19.27, 20.43, 21.35, 22.49, 23.77, 20.34, 22.7, 20.47, 23.31, 22.0, 19.8]
tmaxima = [37.12, 25.2, 27.3, 29.24, 35.99, 37.72, 26.9, 37.48, 31.38, 30.78, 26.34, 30.32, 27.43, 31.03, 36.95]

etiquetas = range(1,16)

x = np.arange(len(etiquetas))  
print(f'x es {x}')

ancho = 0.50  
fig, ax = plt.subplots()
rects1 = ax.barh(x - ancho/2, tminima, ancho, label='minima')
rects2 = ax.barh(x + ancho/2, tmaxima, ancho, label='maxima')


ax.set_ylabel('Días')
ax.set_xlabel('Temperaturas')
ax.set_title('Temperatura a 15 días')
plt.xticks(range(0,43,2))

ax.bar_label(rects1)
ax.bar_label(rects2)
plt.savefig("Grafica de días.png")
plt.show()



# %%
