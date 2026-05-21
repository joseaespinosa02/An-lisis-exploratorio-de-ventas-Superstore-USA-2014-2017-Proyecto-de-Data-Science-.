# Superstore Sales - Análisis Exploratorio de Datos

## 1. Objetivo
Analizar las ventas y ganancias de un Superstore de retail en USA 
durante el período 2014-2017 para identificar patrones de negocio, 
detectar ineficiencias y proponer recomendaciones basadas en evidencia.

## 2. Dataset
- **Fuente:** [Kaggle - Superstore Sales Dataset](https://www.kaggle.com/datasets/vivek468/superstore-dataset-final)
- **Filas:** 9,993 | **Columnas:** 20
- **Período:** Enero 2014 - Diciembre 2017
- **Archivo:** `data/raw/Sample - Superstore.csv`

## 3. Preguntas de negocio
1. ¿Qué categoría genera más ventas y ganancia?
2. ¿Cómo han evolucionado las ventas a lo largo del tiempo?
3. ¿Qué regiones son las más rentables?
4. ¿Cómo afectan los descuentos a la ganancia?
5. ¿Qué segmento de clientes es el más valioso?

## 4. Limpieza y transformaciones

El dataset presentaba varios problemas que fue necesario resolver antes del análisis:

| Problema | Solución |
|---|---|
| 1 fila duplicada | Eliminada con `drop_duplicates()` para no contar órdenes dos veces |
| `Order Date` y `Ship Date` en formato texto | Convertidas a `datetime` con `pd.to_datetime()` para análisis temporal |
| Columna `Row ID` sin valor analítico | Eliminada con `drop()` para simplificar el dataset |

## 4.1 Features creadas

Se construyeron 4 nuevas variables para enriquecer el análisis:

| Feature | Descripción |
|---|---|
| `Profit Margin` | Ratio ganancia/ventas para medir rentabilidad real más allá del volumen |
| `Order Month` | Mes de la orden para identificar patrones de estacionalidad |
| `Order Year` | Año de la orden para analizar tendencias de crecimiento |
| `Days to Ship` | Días entre orden y envío para medir eficiencia logística |

## 5. Pipeline

raw CSV → load_csv() → clean() → build_features() → visualizaciones → processed CSV

## 6. Hallazgos principales

**1. Technology es la categoría más rentable**
Technology lidera con ~$840K en ventas y ~$145K en ganancia.
Furniture genera ventas similares (~$740K) pero solo ~$18K en ganancia — 
un margen del 2.4% — debido a los descuentos excesivos aplicados en esta categoría.
Office Supplies es la categoría más eficiente con ~$122K en ganancia sobre ~$720K en ventas.
Ver gráfico 1.

**2. Las ventas crecen con estacionalidad clara**
Las ventas aumentaron de ~$480K en 2014 a ~$730K en 2017 — un crecimiento del 52%.
Se identifican picos recurrentes en noviembre/diciembre y caídas en enero/febrero.
El mejor mes registrado fue noviembre 2017 con ~$120K en ventas.
Ver gráfico 2.

**3. Descuentos superiores al 20% destruyen rentabilidad**
Con descuentos entre 0%-20% las órdenes son mayoritariamente rentables.
A partir del 30% de descuento la mayoría de órdenes generan pérdidas,
llegando hasta -$6,500 por orden con descuentos del 80%.
La región Central y la categoría Furniture concentran los descuentos más altos,
explicando su baja rentabilidad.
Ver gráfico 4.