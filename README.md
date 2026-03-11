Customer Behavior Analysis
📌 Objetivo
Analizar el comportamiento de clientes a partir de un dataset de compras, con el fin de identificar patrones de gasto, satisfacción y segmentación que permitan proponer estrategias de negocio y fidelización.

📂 Estructura del Proyecto
data/ → dataset original (customers.csv)

notebooks/ → análisis exploratorio y modelado (EDA_Customer_Behavior.ipynb)

scripts/ → funciones auxiliares y pipelines reproducibles

visuals/ → gráficos y dashboards exportados

README.md → documentación del proyecto

🔎 Flujo de Trabajo
Definición del problema y objetivos

EDA (Exploratory Data Analysis)

Distribución por género y edad

Cruce entre membresía y satisfacción

Correlaciones entre variables clave

Detección de outliers

Segmentación preliminar por gasto y satisfacción

Feature Engineering

Frecuencia de compra, monto total, recencia

Normalización y Clustering

K-Means con Elbow Method

Visualización de segmentos

Gráficos interactivos con Plotly

Integración con SQL/PostgreSQL

Queries de validación y agregación

Dashboard en Power BI

KPIs de ventas, satisfacción y segmentos

Documentación y conclusiones ejecutivas

📊 Resultados Clave del EDA
Los clientes Gold concentran más del 65% del gasto total pese a ser ~40% del dataset.

El grupo de 30–35 años es el más activo en compras, con gasto superior al promedio.

Clientes Bronze muestran alta insatisfacción (>70%), mientras que Gold mantienen ratings de 4.5–4.9.

Existe una correlación positiva (≈0.65) entre Items Purchased y Total Spend.

San Francisco y New York concentran el mayor gasto y satisfacción, mientras que Miami y Chicago presentan baja satisfacción.

Se identifican outliers premium en San Francisco con gastos >$1,500.

Los clientes con descuentos aplicados tienen menor satisfacción promedio (3.5 vs 4.5).

📈 Visualizaciones
Distribución de gasto por género y edad.

Satisfacción promedio por tipo de membresía.

Matriz de correlación entre variables clave.

Outliers de gasto y frecuencia.

Segmentación preliminar por membresía y ciudad.

Dashboard interactivo en Power BI.

🧩 Insights Ejecutivos
Segmento Gold: clientes de alto valor → estrategias de fidelización y exclusividad.

Segmento Silver: clientes intermedios → promociones para aumentar gasto.

Segmento Bronze: clientes de bajo gasto y alta insatisfacción → campañas de reactivación.

Ciudades críticas (Miami, Chicago): requieren mejoras en experiencia y servicio.

Clientes premium (> $1,500): potenciales programas VIP.

⚙️ Reproducibilidad
Clonar el repositorio.

Crear entorno virtual:
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

Instalar dependencias:

pip install -r requirements.txt
Ejecutar notebooks en notebooks/.

Revisar visualizaciones en visuals/.