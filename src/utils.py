import pandas as pd

def assert_columns(df: pd.DataFrame, columns: list):
    # Se verifica que las columnas necesarias existen en el dataset
    # para evitar errores silenciosos en el análisis
    missing = [col for col in columns if col not in df.columns]
    if missing:
        raise ValueError(f"Faltan columnas: {missing}")
    print(f"Validación correcta: todas las columnas existen")

def resumen(df: pd.DataFrame):
    # Se muestra un resumen rápido del dataset para verificar
    # que los datos se cargaron y limpiaron correctamente
    print(f"Filas: {df.shape[0]}")
    print(f"Columnas: {df.shape[1]}")
    print(f"Nulos: {df.isnull().sum().sum()}")
    print(f"Duplicados: {df.duplicated().sum()}")