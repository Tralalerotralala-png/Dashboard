# Análisis de anuncios de venta de vehículos

Este proyecto consiste en una aplicación web interactiva para explorar anuncios de venta de vehículos usados en Estados Unidos. Su objetivo es visualizar la distribución del kilometraje y analizar su relación con el precio de venta de los automóviles.

## Funcionalidades

- Histograma de kilometraje.
- Gráfico de dispersión de precio frente al kilometraje.
- Filtros por tipo de vehículo.
- Casillas de verificación para mostrar u ocultar los gráficos.
- Estadísticas descriptivas y vista previa de los datos.

## Datos y herramientas

El conjunto de datos utilizado es `vehicles_us.csv`. El proyecto se desarrolló con Python, pandas, Plotly y Streamlit.

## Ejecución local

```bash
pip install -r requirements.txt
streamlit run app.py
```

Para reproducir el análisis exploratorio desde la raíz del proyecto:

```python
import pandas as pd
car_data = pd.read_csv('vehicles_us.csv')
print(car_data.info())
print(car_data.describe())
print(car_data.isna().sum())
print(car_data[['odometer', 'price']].corr())
```

La aplicación conserva el histograma y el gráfico de dispersión originales; los valores ausentes se excluyen solo de las visualizaciones que los requieren.

## Aplicación web

https://vehicles-dashboard-sprint7.onrender.com/
