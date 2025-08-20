# Script: 01_analisis_productividad.py
# Análisis de la brecha entre productividad y salarios en EE.UU.
# Evidencia para el Capítulo 1: "El Financierismo y la desconexión del valor real"

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Configurar estilo visual
sns.set_style("whitegrid")
plt.rcParams["font.family"] = "DejaVu Sans"

# Cargar datos
df = pd.read_csv('datos_brutos/productivity_vs_wages.csv')

# Crear gráfico
plt.figure(figsize=(12, 6))
plt.plot(df['Year'], df['Productivity'], label='Productividad (Output por hora)', linewidth=2)
plt.plot(df['Year'], df['Hourly_Compensation'], label='Compensación por hora', linewidth=2)

# Personalizar
plt.title('Brecha entre Productividad y Salarios en EE.UU. (1970-2020)', fontsize=16, pad=20)
plt.xlabel('Año')
plt.ylabel('Índice (1970 = 100)')
plt.legend()
plt.fill_between(df['Year'], df['Productivity'], df['Hourly_Compensation'], alpha=0.3, color='gray')

# Guardar gráfico
plt.savefig('imagenes_graficos/brecha_productividad_salarios.png', dpi=300, bbox_inches='tight')
plt.close()