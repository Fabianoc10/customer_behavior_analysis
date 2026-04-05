"""
Visualización de segmentos de clientes:
- Scatter plot interactivo con Plotly (incluye Membership Type y City)
- Gráficos comparativos de gasto y frecuencia por cluster
"""

import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

# Detectar raíz del proyecto automáticamente
base_path = os.path.dirname(os.path.dirname(__file__))
clusters_path = os.path.join(base_path, "data", "customers_clusters.csv")
original_path = os.path.join(base_path, "data", "customers.csv")

# Cargar datasets
df_clusters = pd.read_csv(clusters_path)
df_original = pd.read_csv(original_path)

# Unir datasets por Customer ID
df = df_clusters.merge(
    df_original[['Customer ID','Membership Type','City']],
    on='Customer ID',
    how='left'
)

# Crear carpeta visuals si no existe
visuals_path = os.path.join(base_path, "visuals")
if not os.path.exists(visuals_path):
    os.makedirs(visuals_path)

# 1. Scatter plot interactivo con Plotly
fig = px.scatter(
    df,
    x="Frequency",
    y="TotalSpend",
    color="Cluster",
    size="Recency",
    hover_data=["Customer ID", "Membership Type", "City"],
    title="Segmentación de clientes por Clusters"
)
fig.write_html(os.path.join(visuals_path, "clusters_scatter.html"))
fig.write_image(os.path.join(visuals_path, "clusters_scatter.png"))

# 2. Gasto promedio por cluster
plt.figure(figsize=(6,4))
sns.barplot(x="Cluster", y="TotalSpend", data=df, estimator="mean")
plt.title("Gasto promedio por cluster")
plt.savefig(os.path.join(visuals_path, "avg_spend_cluster.png"))
plt.close()

# 3. Frecuencia promedio por cluster
plt.figure(figsize=(6,4))
sns.barplot(x="Cluster", y="Frequency", data=df, estimator="mean")
plt.title("Frecuencia promedio por cluster")
plt.savefig(os.path.join(visuals_path, "avg_frequency_cluster.png"))
plt.close()

print("✅ Visualizaciones generadas en la carpeta 'visuals/'")
