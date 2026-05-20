import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import matplotlib.pyplot as plt
import seaborn as sns

def plot_ventas_categoria(df):
    # Se visualizan las ventas por categoría para identificar
    # cuál genera mayor volumen de ingresos
    plt.figure(figsize=(8, 5))
    sns.barplot(data=df, x='Category', y='Sales', estimator='sum', errorbar=None)
    plt.title('Ventas Totales por Categoria')
    plt.xlabel('Categoria')
    plt.ylabel('Ventas ($)')
    plt.tight_layout()
    plt.show()

def plot_ventas_tiempo(df):
    # Se agrupa por mes para visualizar la evolución temporal
    # de las ventas e identificar estacionalidad
    df_monthly = df.groupby(pd.Grouper(key='Order Date', freq='ME'))['Sales'].sum().reset_index()
    plt.figure(figsize=(12, 5))
    plt.plot(df_monthly['Order Date'], df_monthly['Sales'], marker='o', linewidth=2)
    plt.title('Evolucion de Ventas Mensuales')
    plt.xlabel('Fecha')
    plt.ylabel('Ventas ($)')
    plt.tight_layout()
    plt.show()

def plot_descuento_ganancia(df):
    # Se visualiza la relación entre descuento y ganancia para
    # identificar el punto donde los descuentos generan pérdidas
    plt.figure(figsize=(10, 5))
    sns.scatterplot(data=df, x='Discount', y='Profit', alpha=0.4)
    plt.axhline(y=0, color='red', linestyle='--', label='Profit = 0')
    plt.title('Relacion entre Descuento y Ganancia')
    plt.xlabel('Descuento')
    plt.ylabel('Ganancia ($)')
    plt.legend()
    plt.tight_layout()
    plt.show()
