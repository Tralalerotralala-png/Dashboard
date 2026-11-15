# Explorador de vehículos | Sprint 7

Proyecto de TripleTen: aplicación web interactiva de análisis exploratorio con pandas, Plotly y Streamlit. Incluye histograma, dispersión, casillas de verificación, filtros y estadísticas.

**Aplicación en Render:** pendiente de desplegar.

## Datos
Se utiliza el dataset alternativo mpg (234 registros de economía de combustible de vehículos). Fuente: https://github.com/tidyverse/ggplot2/blob/main/data-raw/mpg.csv y documentación https://ggplot2.tidyverse.org/reference/mpg.html. El archivo original del curso no fue proporcionado. Si se añade vehicles_us.csv a la raíz, la aplicación cambia automáticamente a kilometraje y precio.

## Ejecución local
```bash
python -m venv vehicles_env
pip install -r requirements.txt
streamlit run app.py
```
Activa el entorno antes de instalar: en Windows, ` .\vehicles_env\Scripts\Activate.ps1 `; en Linux/macOS, `source vehicles_env/bin/activate`.

El análisis exploratorio está en notebooks/EDA.ipynb. Instala ipykernel en el entorno si necesitas ejecutar Jupyter.

## Render
Crea un Web Service desde este repositorio, rama main, runtime Python, plan Free.
- Build: `pip install --upgrade pip && pip install -r requirements.txt`
- Start: `streamlit run app.py --server.address=0.0.0.0 --server.port=$PORT`

También se incluye render.yaml. Cuando el servicio esté disponible, actualiza este README con su URL real.
