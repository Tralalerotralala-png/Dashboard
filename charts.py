from pathlib import Path
import pandas as pd
import plotly.express as px

ROOT = Path(__file__).resolve().parent

def load_data(root=ROOT):
    return pd.read_csv(Path(root) / 'vehicles_us.csv')

def histogram(data):
    fig = px.histogram(data.dropna(subset=['odometer']), x='odometer', nbins=30,
                       labels={'odometer': 'Odómetro (millas)'},
                       title='Distribución del kilometraje')
    fig.update_layout(yaxis_title='Número de anuncios', bargap=0.05)
    return fig

def scatter(data):
    return px.scatter(data.dropna(subset=['odometer', 'price', 'type']),
                      x='odometer', y='price', color='type', opacity=0.55,
                      labels={'odometer': 'Odómetro (millas)', 'price': 'Precio (USD)', 'type': 'Tipo de vehículo'},
                      title='Precio frente al kilometraje')
