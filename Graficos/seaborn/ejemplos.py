#%% EJEMPLOS
# Importar la librería seaborn
import seaborn as sns
import matplotlib.pyplot as plt

# Cargar un dataset de ejemplo
titanic = sns.load_dataset("titanic")

# Visualizar un histograma de la edad de los pasajeros del Titanic
sns.histplot(data=titanic, x="age", bins=20)

# Mostrar el gráfico
plt.show()
#%%
# Importar la librería seaborn
import seaborn as sns
import matplotlib.pyplot as plt

# Cargar un dataset de ejemplo
titanic = sns.load_dataset("titanic")

# Visualizar la relación entre la edad y el precio del boleto pagado por los pasajeros
sns.scatterplot(data=titanic, x="age", y="fare")

# Mostrar el gráfico
plt.show()
#%%
# Importar la librería seaborn
import seaborn as sns

# Cargar un dataset de ejemplo
titanic = sns.load_dataset("titanic")

# Visualizar la cantidad de pasajeros por clase y género
sns.catplot(data=titanic, x="class", hue="sex", kind="count")

# Mostrar el gráfico
plt.show()
#%%
# Importar la librería seaborn
import seaborn as sns

# Cargar un dataset de ejemplo
tips = sns.load_dataset("tips")

# Visualizar la relación entre la propina y el total de la factura, con diferencias en el día de la semana
sns.relplot(data=tips, x="total_bill", y="tip", hue="day")

# Mostrar el gráfico
plt.show()


# %%
