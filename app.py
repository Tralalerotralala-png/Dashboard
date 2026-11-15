import streamlit as st
import pandas as pd
import plotly.express as px
from charts import load_data, histogram, scatter

st.set_page_config(page_title='Explorador de vehículos', layout='wide')
st.header('Análisis de anuncios de venta de vehículos')
st.write('Explora el kilometraje y los precios de los vehículos usados en Estados Unidos.')

@st.cache_data
def read_data():
    return load_data()

car_data = read_data()
options = sorted(car_data['type'].dropna().unique())
selected = st.sidebar.multiselect('Tipo de vehículo', options, default=options)
filtered = car_data[car_data['type'].isin(selected)]

if filtered.empty:
    st.warning('Selecciona al menos un tipo de vehículo.')
    st.stop()

col1, col2, col3 = st.columns(3)
col1.metric('Anuncios', f'{len(filtered):,}')
col2.metric('Precio mediano (USD)', f'${filtered["price"].median():,.0f}')
col3.metric('Kilometraje mediano (millas)', f'{filtered["odometer"].median():,.0f}')

if st.checkbox('Construir histograma', value=True):
    st.write('Distribución del kilometraje de los vehículos.')
    st.plotly_chart(histogram(filtered), use_container_width=True)

if st.checkbox('Construir gráfico de dispersión', value=True):
    st.write('Relación entre el kilometraje y el precio de venta.')
    st.plotly_chart(scatter(filtered), use_container_width=True)

with st.expander('Vista previa de los datos'):
    st.dataframe(filtered.head(100), use_container_width=True)
