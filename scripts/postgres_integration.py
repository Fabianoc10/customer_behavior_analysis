"""
Integración con PostgreSQL:
- Conexión a la base de datos con SQLAlchemy
- Creación de tabla 'customers_clusters'
- Inserción de datos desde CSV
- Ejecución de queries de validación
"""

import os
import pandas as pd
from sqlalchemy import create_engine, text

# Configuración de conexión (ajusta con tus credenciales)
DB_USER = "postgres"
DB_PASSWORD = "NESfa19929"
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "customer_analysis"

# Crear conexión con SQLAlchemy
engine = create_engine(f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}")

# Ruta del dataset procesado
base_path = os.path.dirname(os.path.dirname(__file__))
file_path = os.path.join(base_path, "data", "customers_clusters.csv")

# Cargar dataset
df = pd.read_csv(file_path)

# Normalizar nombres de columnas a minúsculas
df.columns = [c.lower() for c in df.columns]

# Subir datos a PostgreSQL (crea tabla si no existe)
df.to_sql("customers_clusters", engine, if_exists="replace", index=False)

# Subir datos a PostgreSQL (crea tabla si no existe)
df.to_sql("customers_clusters", engine, if_exists="replace", index=False)

print("✅ Datos cargados en la tabla 'customers_clusters'")

# Ejemplo de queries de validación
with engine.connect() as conn:
    # Total de clientes por cluster
    result = conn.execute(text("SELECT cluster, COUNT(*) AS total_clientes FROM customers_clusters GROUP BY cluster"))
    print("\n Clientes por cluster:")
    for row in result:
        print(row)

    # Gasto promedio por cluster
    result = conn.execute(text("SELECT cluster, AVG(totalspend) AS gasto_promedio FROM customers_clusters GROUP BY cluster"))
    print("\n Gasto promedio por cluster:")
    for row in result:
        print(row)

