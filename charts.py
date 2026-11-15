from pathlib import Path
import pandas as pd
import plotly.express as px

ROOT = Path(__file__).resolve().parent

def load_data(root=ROOT):
    root = Path(root)
    path = root / 'vehicles_us.csv'
    if path.is_file():
        mode = 'listings'
        required = {'odometer', 'price', 'type'}
    else:
        path = root / 'mpg.csv'
        mode = 'mpg'
        required = {'hwy', 'displ', 'class'}
    data = pd.read_csv(path)
    missing = required.difference(data.columns)
    if missing:
        raise ValueError(f'{path.name}: faltan columnas {", ".join(sorted(missing))}')
    return data, mode, path.name

def settings(mode):
    if mode == 'listings':
        return dict(category='type', x='odometer', y='price', labels={'odometer':'Odómetro (millas)','price':'Precio (USD)','type':'Tipo de vehículo'}, hist_title='Distribución del kilometraje', scatter_title='Precio frente al kilometraje')
    return dict(category='class', x='displ', y='hwy', labels={'displ':'Cilindrada (L)','hwy':'Rendimiento en carretera (MPG)','class':'Tipo de vehículo'}, hist_title='Distribución de la cilindrada', scatter_title='Rendimiento en carretera frente a cilindrada')

def histogram(data, mode):
    c = settings(mode)
    fig = px.histogram(data.dropna(subset=[c['x']]), x=c['x'], nbins=30, labels=c['labels'], title=c['hist_title'])
    fig.update_layout(yaxis_title='Número de registros', bargap=0.05)
    return fig

def scatter(data, mode):
    c = settings(mode)
    return px.scatter(data.dropna(subset=[c['x'],c['y'],c['category']]), x=c['x'], y=c['y'], color=c['category'], opacity=0.65, labels=c['labels'], title=c['scatter_title'])
