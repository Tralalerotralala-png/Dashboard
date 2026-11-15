import pandas as pd
import plotly.express as px
import streamlit as st
from charts import load_data, settings, histogram, scatter

st.set_page_config(page_title='Explorador de vehículos', layout='wide')
st.header('Explorador de vehículos')
st.write('Sprint 7 · Panel interactivo de análisis exploratorio de datos.')
try:
    data, mode, filename = load_data()
except (OSError, ValueError) as error:
    st.error(f'No se pudieron cargar los datos: {error}')
    st.stop()
st.caption(f'Fuente: {filename}')
if mode == 'mpg':
    st.info('Se utiliza el dataset alternativo mpg, basado en datos de economía de combustible de la EPA.')
config = settings(mode)
category = config['category']
options = sorted(data[category].dropna().unique().tolist())
selected = st.sidebar.multiselect('Tipos de vehículo', options, default=options)
filtered = data[data[category].isin(selected)]
if filtered.empty:
    st.warning('Selecciona al menos un tipo de vehículo con datos.')
    st.stop()
x, y = config['x'], config['y']
col1, col2, col3 = st.columns(3)
col1.metric('Registros', f'{len(filtered):,}')
col2.metric(f'Mediana: {config["labels"][x]}', f'{filtered[x].median():,.1f}')
col3.metric(f'Mediana: {config["labels"][y]}', f'{filtered[y].median():,.1f}')
st.subheader('Visualizaciones interactivas')
if st.checkbox('Construir histograma', value=True):
    st.write(config['hist_title'])
    st.plotly_chart(histogram(filtered, mode), use_container_width=True)
if st.checkbox('Construir gráfico de dispersión', value=True):
    st.write(config['scatter_title'])
    st.plotly_chart(scatter(filtered, mode), use_container_width=True)
with st.expander('Vista previa de los datos'):
    st.dataframe(filtered.head(100), use_container_width=True)
