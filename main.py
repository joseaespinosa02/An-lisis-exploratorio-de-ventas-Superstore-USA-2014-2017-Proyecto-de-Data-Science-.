from src.config import RAW_PATH, OUT_PATH
from src.io import load_csv
from src.cleaning import clean
from src.features import build_features
from src.utils import assert_columns, resumen
from src.viz import plot_ventas_categoria, plot_ventas_tiempo, plot_descuento_ganancia

def main():
    # Se carga el dataset original desde la carpeta raw
    df = load_csv(RAW_PATH)
    
    # Se limpia el dataset eliminando duplicados y corrigiendo tipos
    df = clean(df)
    
    # Se valida que las columnas necesarias existen antes de continuar
    assert_columns(df, ['Sales', 'Profit', 'Discount', 'Order Date', 'Category'])
    
    # Se crean las nuevas features para enriquecer el análisis
    df = build_features(df)
    
    # Se muestra un resumen del dataset final
    resumen(df)
    
    # Se generan las visualizaciones principales del análisis
    plot_ventas_categoria(df)
    plot_ventas_tiempo(df)
    plot_descuento_ganancia(df)
    
    # Se exporta el dataset limpio y con features a la carpeta processed
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(OUT_PATH, index=False)
    print(f"Dataset guardado en: {OUT_PATH}")

if __name__ == "__main__":
    main()
    