from pathlib import Path

# Se define la raíz del proyecto de forma dinámica para que las rutas
# funcionen correctamente independientemente de donde se ejecute el código
ROOT = Path(__file__).resolve().parent.parent

# Se define la ruta del archivo CSV original que contiene los datos crudos
RAW_PATH = ROOT / "data" / "raw" / "Sample - Superstore.csv"

# Se define la ruta donde se guardará el dataset ya limpio y procesado
OUT_PATH = ROOT / "data" / "processed" / "superstore_clean.csv"