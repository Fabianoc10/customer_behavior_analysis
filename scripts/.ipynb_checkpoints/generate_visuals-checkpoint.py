import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

# Cargar dataset
df = pd.read_csv('../data/customers.csv')

# Crear carpeta visuals si no existe
import os
if not os.path.exists('../visuals'):
    os.makedirs('../visuals')

# 1. Distribución de gasto por género
plt.figure(figsize=(6,4))
sns.boxplot(x='Gender', y='Total Spend', data=df)
plt.title("Distribución de gasto por género")
plt.savefig('../visuals/gender_spend.png')
plt.close()

# 2. Total Spend por rango de edad y género
df['AgeGroup'] = pd.cut(df['Age'], bins=[20,30,40,50], labels=['20-29','30-39','40-49'])
plt.figure(figsize=(6,4))
sns.barplot(x='AgeGroup', y='Total Spend', hue='Gender', data=df, estimator=sum)
plt.title("Total Spend por rango de edad y género")
plt.savefig('../visuals/age_gender_spend.png')
plt.close()

# 3. Satisfacción promedio por tipo de membresía
plt.figure(figsize=(6,4))
sns.boxplot(x='Membership Type', y='Average Rating', data=df)
plt.title("Satisfacción promedio por membresía")
plt.savefig('../visuals/membership_satisfaction.png')
plt.close()

# 4. Matriz de correlación
corr = df[['Total Spend','Items Purchased','Average Rating','Days Since Last Purchase']].corr()
plt.figure(figsize=(6,4))
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title("Matriz de correlación")
plt.savefig('../visuals/correlation_matrix.png')
plt.close()

# 5. Outliers en gasto
plt.figure(figsize=(6,4))
sns.boxplot(y=df['Total Spend'])
plt.title("Outliers en gasto")
plt.savefig('../visuals/outliers_spend.png')
plt.close()

# 6. Segmentación preliminar por membresía
df.groupby('Membership Type')['Total Spend'].sum().plot(kind='bar')
plt.title("Participación en gasto por membresía")
plt.savefig('../visuals/membership_spend.png')
plt.close()

# 7. Distribución de satisfacción por ciudad
df.groupby('City')['Satisfaction Level'].value_counts(normalize=True).unstack().plot(kind='bar', stacked=True)
plt.title("Distribución de satisfacción por ciudad")
plt.savefig('../visuals/city_satisfaction.png')
plt.close()

# 8. Dashboard preliminar con Plotly (ejemplo)
fig = px.bar(df.groupby('City')['Total Spend'].sum().reset_index(),
             x='City', y='Total Spend', title='Ventas por Ciudad')
fig.write_image('../visuals/city_sales_plotly.png')
