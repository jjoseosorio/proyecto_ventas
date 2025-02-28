import pandas as pd
import matplotlib.pyplot as plt

# Cargar los datos desde el archivo CSV
df = pd.read_csv('ventas_productos.csv')

# Calcular el precio total por producto
df['Precio Total'] = df[' Cantidad'] * df[' Precio ']

# Mostrar los primeros registros
print(df.head())

# Crear un gráfico de barras para visualizar el precio total por producto
plt.bar(df['Producto'], df['Precio Total'])
plt.xlabel('Producto')
plt.ylabel('Precio Total')
plt.title('Precio Total por Producto')
plt.xticks(rotation=45)

# Guardar el gráfico como PNG
plt.savefig('grafico_precios.png')
plt.show()



