import pandas as pd
import requests
import plotly.express as px

# Fetch the data
df = pd.read_csv(
    "https://ourworldindata.org/grapher/global-energy-substitution.csv?v=1&csvType=full&useColumnShortNames=true",
    storage_options={'User-Agent': 'Our World In Data data fetch/1.0'}
)

# Fetch the metadata
metadata = requests.get(
    "https://ourworldindata.org/grapher/global-energy-substitution.metadata.json?v=1&csvType=full&useColumnShortNames=true"
).json()

cols = [
    'Year',
    'coal__twh_substituted_energy',
    'oil__twh_substituted_energy',
    'gas__twh_substituted_energy',
    'nuclear__twh_substituted_energy',
    'hydropower__twh_substituted_energy',
    'wind__twh_substituted_energy',
    'solar__twh_substituted_energy',
    'biofuels__twh_substituted_energy',
    'other_renewables__twh_substituted_energy',
    'traditional_biomass__twh_substituted_energy'
]

df_world = df[df["Entity"] == "World"][cols]

df_long = df_world.melt(
    id_vars="Year",
    var_name="Energy Source",
    value_name="Value"
)

df_long["Energy Source"] = df_long["Energy Source"].str.replace("__twh_substituted_energy", "")

# Crear la figura
fig = px.area(
    df_long,
    x='Year',
    y='Value',
    color='Energy Source',
    title='Evolució del consum global d’energia primària per font (substitució)',
    labels={'Value': 'Energia (TWh substituïda)', 'Year': 'Any'}
)
fig.update_layout(
    legend_title_text='Font d’energia',
    template='simple_white'
)

fig.write_html("energia_global.html")
