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
- **Duplicados eliminados** → se encontró 1 fila duplicada que podría distorsionar el análisis
- **Columna Row ID eliminada** → identificador sin valor analítico
- **Fechas convertidas** → Order Date y Ship Date llegaron como texto y se convirtieron a datetime
- **Features creadas:**
  - `Profit Margin` → ratio ganancia/ventas para medir rentabilidad real
  - `Order Month` y `Order Year` → para análisis de estacionalidad
  - `Days to Ship` → para analizar eficiencia logística

## 5. Pipeline

raw CSV → load_csv() → clean() → build_features() → visualizaciones → processed CSV