Customer Behavior Analysis
Objetivo
Analizar el comportamiento de clientes a partir de un dataset de compras, con el fin de identificar patrones de gasto, satisfacción y segmentación que permitan proponer estrategias de negocio y fidelización.

Estructura del Proyecto
data/ → dataset original (customers.csv) y datasets procesados (customers_features.csv, customers_clusters.csv)

notebooks/ → análisis exploratorio y modelado (EDA_Customer_Behavior.ipynb)

scripts/ → funciones auxiliares y pipelines reproducibles

visuals/ → gráficos y dashboards exportados

README.md → documentación del proyecto

Flujo de Trabajo
Definición del problema y objetivos

Exploratory Data Analysis (EDA)

Distribución por género y edad

Cruce entre membresía y satisfacción

Correlaciones entre variables clave

Detección de outliers

Feature Engineering

Frecuencia de compra, monto total, recencia

Normalización y Clustering

K-Means con Elbow Method

Validación de clusters con estadísticas

Visualización de segmentos

Gráficos interactivos con Plotly

Dashboards en Power BI

Integración con SQL/PostgreSQL

Queries de validación y agregación

Resultados Clave del EDA
Los clientes Gold concentran más del 65% del gasto total pese a ser ~40% del dataset.

El grupo de 30–35 años es el más activo en compras, con gasto superior al promedio.

Clientes Bronze muestran alta insatisfacción (>70%), mientras que Gold mantienen ratings de 4.5–4.9.

Existe una correlación positiva (≈0.65) entre Items Purchased y Total Spend.

San Francisco y New York concentran el mayor gasto y satisfacción, mientras que Miami y Chicago presentan baja satisfacción.

Los clientes con descuentos aplicados tienen menor satisfacción promedio (3.5 vs 4.5).

Segmentación por Clusters (K-Means)
Se identificaron tres segmentos principales de clientes:

Cluster 0 – Clientes en riesgo

Gasto promedio: ~546

Compras promedio: ~9.5

Rating promedio: ~3.5

Recencia: ~36 días

Interpretación: clientes con bajo gasto, pocas compras y mayor tiempo desde la última compra. Representan riesgo de abandono.

Acciones recomendadas: campañas de retención, descuentos personalizados, encuestas de satisfacción.

Cluster 1 – Clientes estables

Gasto promedio: ~985

Compras promedio: ~13.5

Rating promedio: ~4.3

Recencia: ~20 días

Interpretación: clientes regulares, con gasto medio y satisfacción alta.

Acciones recomendadas: programas de fidelización, recompensas por constancia, mantener su satisfacción.

Cluster 2 – Clientes VIP

Gasto promedio: ~1460

Compras promedio: ~20

Rating promedio: ~4.8

Recencia: ~11 días

Interpretación: clientes de alto valor, con gasto elevado, compras frecuentes y alta satisfacción.

Acciones recomendadas: beneficios premium, trato preferencial, mantener su lealtad.

Visualizaciones
Distribución de gasto por género y edad.

Satisfacción promedio por tipo de membresía.

Matriz de correlación entre variables clave.

Outliers de gasto y frecuencia.

Segmentación por clusters (gráficos interactivos y estáticos).

Insights Ejecutivos
Cluster 0: clientes en riesgo → campañas de retención.

Cluster 1: clientes estables → fidelización y recompensas.

Cluster 2: clientes VIP → beneficios premium y exclusividad.

Ciudades críticas (Miami, Chicago): requieren mejoras en experiencia y servicio.

Clientes premium (> $1,500): potenciales programas VIP.

Reproducibilidad
Clonar el repositorio.

Crear entorno virtual:
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

Instalar dependencias:
pip install -r requirements.txt

Ejecutar notebooks en notebooks/.

Revisar visualizaciones en visuals/.