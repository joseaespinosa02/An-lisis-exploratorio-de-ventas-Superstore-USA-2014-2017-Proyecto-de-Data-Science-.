import pandas as pd

def build_features(df: pd.DataFrame) -> pd.DataFrame:
    # Se calcula el margen de ganancia para identificar qué productos
    # son realmente rentables más allá del volumen de ventas
    df['Profit Margin'] = (df['Profit'] / df['Sales']).round(4)
    
    # Se extrae el mes y año de la orden para poder analizar
    # la estacionalidad y tendencias de ventas en el tiempo
    df['Order Month'] = df['Order Date'].dt.month
    df['Order Year'] = df['Order Date'].dt.year
    
    # Se calcula los días que tardó el envío para analizar
    # la eficiencia logística del negocio
    df['Days to Ship'] = (df['Ship Date'] - df['Order Date']).dt.days
    
    print(f"Features creadas: Profit Margin, Order Month, Order Year, Days to Ship")
    return df