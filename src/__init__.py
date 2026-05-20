# Se importan las funciones principales del módulo src para que
# puedan ser llamadas directamente desde cualquier parte del proyecto
from src.io import load_csv
from src.cleaning import clean
from src.features import build_features
from src.viz import plot_ventas_categoria, plot_ventas_tiempo, plot_descuento_ganancia
from src.utils import assert_columns, resumen