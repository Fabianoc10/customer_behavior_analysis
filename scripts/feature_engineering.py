"""
Feature Engineering para análisis de clientes:
- Frecuencia: número de compras por cliente
- Monto total: suma de compras
- Recencia: días desde la última compra
"""

import os
import pandas as pd

# Detectar raíz del proyecto automáticamente
base_path = os.path.dirname(os.path.dirname(__file__))
file_path = os.path.join(base_path, "data", "customers.csv")

# Cargar dataset
df = pd.read_csv(file_path)

# Feature Engineering
features = df.groupby('Customer ID').agg(
    Frequency=('Items Purchased', 'sum'),       # número de ítems comprados (proxy de frecuencia)
    TotalSpend=('Total Spend', 'sum'),          # monto total gastado
    AvgDaysSinceLast=('Days Since Last Purchase', 'mean')  # promedio de días desde última compra
).reset_index()

# Renombrar columna de recencia
features = features.rename(columns={'AvgDaysSinceLast': 'Recency'})

# Guardar DataFrame limpio
output_path = os.path.join(base_path, "data", "customers_features.csv")
features.to_csv(output_path, index=False)

print("✅ Archivo generado:", output_path)

