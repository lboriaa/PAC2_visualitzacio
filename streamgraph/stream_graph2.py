import pandas as pd
import requests

# Fetch the data.
df = pd.read_csv("https://ourworldindata.org/grapher/share-of-final-energy-consumption-from-renewable-sources.csv?v=1&csvType=full&useColumnShortNames=true&utm_source=chatgpt.com", storage_options = {'User-Agent': 'Our World In Data data fetch/1.0'})

# Fetch the metadata
metadata = requests.get("https://ourworldindata.org/grapher/share-of-final-energy-consumption-from-renewable-sources.metadata.json?v=1&csvType=full&useColumnShortNames=true&utm_source=chatgpt.com").json()


print(df.columns)
