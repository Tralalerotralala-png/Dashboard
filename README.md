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

El análisis exploratorio se encuentra en `notebooks/EDA.ipynb`.

## Aplicación web

https://vehicles-dashboard-sprint7.onrender.com/
