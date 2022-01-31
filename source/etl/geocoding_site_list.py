import pickle
import time

import googlemaps
import pandas as pd

pd.options.display.max_rows = 500
pd.options.display.max_columns = 5100
pd.options.display.width = 2000
pd.options.display.max_colwidth = 1000

site_list = pd.read_csv('data/raw/sites.csv')
site_list['address'] = site_list['Shipping Street'] + ', ' + site_list['Shipping City'] + ', ' + 'South Africa'

from source.config.config import Config

gmaps = googlemaps.Client(key=Config.google_api_key)

results = []
counter = 0
for site in site_list['address']:
    time.sleep(1)
    print(site)
    counter += 1
    if site:
        results.append(gmaps.geocode(site))
    else:
        results.append(None)

site_list['Store Name'].value_counts()
site_list['Store Name'].isna().sum()
site_list['Unit 1'].value_counts()

store_results = {
    store: geo_coding
    for store, geo_coding
    in zip(site_list['Store Name'], results)
}

with open('data/processed/sites_with_geo_coding.pickle', 'wb') as output:
    pickle.dump(store_results, output)
