"""
Normalización y Clustering de clientes:
- Escalado de variables con StandardScaler
- Aplicación de K-Means
- Selección del número de clusters con Elbow Method
"""

import os
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

# Detectar raíz del proyecto automáticamente
base_path = os.path.dirname(os.path.dirname(__file__))
file_path = os.path.join(base_path, "data", "customers_features.csv")

# Cargar dataset de features
df = pd.read_csv(file_path)

# Seleccionar variables para clustering
X = df[['Frequency', 'TotalSpend', 'Recency']]

# Normalización
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Elbow Method para definir número de clusters
inertia = []
K_range = range(1, 11)

for k in K_range:
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(X_scaled)
    inertia.append(kmeans.inertia_)

# Guardar gráfico del Elbow Method
visuals_path = os.path.join(base_path, "visuals")
if not os.path.exists(visuals_path):
    os.makedirs(visuals_path)

plt.figure(figsize=(6,4))
plt.plot(K_range, inertia, marker='o')
plt.title("Elbow Method para selección de clusters")
plt.xlabel("Número de clusters (k)")
plt.ylabel("Inercia")
plt.savefig(os.path.join(visuals_path, "elbow_method.png"))
plt.close()

# Elegir número óptimo de clusters (ejemplo: 3)
optimal_k = 3
kmeans = KMeans(n_clusters=optimal_k, random_state=42)
df['Cluster'] = kmeans.fit_predict(X_scaled)

# Guardar dataset con clusters asignados
output_path = os.path.join(base_path, "data", "customers_clusters.csv")
df.to_csv(output_path, index=False)

print(" Clustering completado. Archivo generado:", output_path)
print("Clusters asignados:", df['Cluster'].unique())
