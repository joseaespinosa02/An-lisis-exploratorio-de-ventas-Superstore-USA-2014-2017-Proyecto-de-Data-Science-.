import pandas as pd
from src.config import RAW_PATH

def load_csv(path=RAW_PATH):
    # Se parsean las fechas al cargar para evitar conversiones manuales después
    df = pd.read_csv(path, parse_dates=['Order Date', 'Ship Date'])
    
    # Se ordena por fecha de orden para facilitar el análisis temporal
    df = df.sort_values('Order Date').reset_index(drop=True)
    
    print(f"Dataset cargado: {df.shape[0]} filas, {df.shape[1]} columnas")
    return df