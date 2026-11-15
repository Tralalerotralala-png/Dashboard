# Análisis de anuncios de venta de vehículos

Este proyecto tiene como objetivo desarrollar una aplicación web interactiva para explorar un conjunto de datos de vehículos. La aplicación permite visualizar la distribución de distintas características de los automóviles y analizar la relación entre ellas mediante gráficos interactivos.

## Funcionalidades

- Histograma para visualizar la distribución de los datos.
- Gráfico de dispersión para comparar variables.
- Filtros por tipo de vehículo.
- Casillas de verificación para mostrar u ocultar los gráficos.
- Consulta de estadísticas descriptivas y vista previa de los datos.

## Herramientas utilizadas

- Python
- Pandas
- Plotly
- Streamlit
- Git y GitHub
- Render

## Datos

La aplicación admite el archivo `vehicles_us.csv`, que contiene anuncios de venta de vehículos en Estados Unidos, así como el archivo `mpg.csv`, que contiene datos de rendimiento de combustible.

## Ejecución local

```bash
pip install -r requirements.txt
streamlit run app.py
```

El análisis exploratorio se encuentra en `notebooks/EDA.ipynb`.

## Aplicación web

Despliegue en Render pendiente.
