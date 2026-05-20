import pandas as pd

def clean(df: pd.DataFrame) -> pd.DataFrame:
    # Se eliminan duplicados para evitar contar órdenes más de una vez
    df = df.drop_duplicates().reset_index(drop=True)
    
    # Se elimina Row ID porque no aporta valor al análisis
    if 'Row ID' in df.columns:
        df = df.drop(columns=['Row ID'])
    
    # Se convierten las fechas porque llegaron como texto en el CSV
    df['Order Date'] = pd.to_datetime(df['Order Date'])
    df['Ship Date'] = pd.to_datetime(df['Ship Date'])
    
    # Se ordena por fecha de orden para el análisis de series temporales
    df = df.sort_values('Order Date').reset_index(drop=True)
    
    print(f"Datos limpios: {df.shape[0]} filas, {df.shape[1]} columnas")
    return df