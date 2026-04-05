from sqlalchemy import create_engine

DB_USER = "postgres"
DB_PASSWORD = "NESfa19929"   # sin acentos ni caracteres raros
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "customer_analysis"

engine = create_engine(f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}")

try:
    with engine.connect() as conn:
        print("✅ Conexión exitosa a PostgreSQL")
except Exception as e:
    print(" Error de conexión:", e)
