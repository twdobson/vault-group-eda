import pickle

import numpy as np
import pandas as pd
import plotly.io as pio
from plotly import graph_objs as go
from shapely.geometry import LineString, MultiLineString

#from source.config.config import Config

with open('data/processed/sites_with_geo_coding.pickle', 'rb') as input:
    geo_coded_sites = pickle.load(input)


def shapefile_to_geojson(gdf, index_list, geo_names_col, tolerance=0.01):
    # gdf - geopandas dataframe containing the geometry column and values to be mapped to a colorscale
    # index_list - a sublist of list(gdf.index)  or gdf.index  for all data
    # level - int that gives the level in the shapefile
    # tolerance - float parameter to set the Polygon/MultiPolygon degree of simplification

    # returns a geojson type dict

    geo_names = list(gdf[geo_names_col])
    geojson = {'type': 'FeatureCollection', 'features': []}
    for index in index_list:
        geo = gdf['geometry'][index].simplify(tolerance)

        if isinstance(geo.boundary, LineString):
            gtype = 'Polygon'
            bcoords = np.dstack(geo.boundary.coords.xy).tolist()

        elif isinstance(geo.boundary, MultiLineString):
            gtype = 'MultiPolygon'
            bcoords = []
            for b in geo.boundary:
                x, y = b.coords.xy
                coords = np.dstack((x, y)).tolist()
                bcoords.append(coords)
        else:
            pass

        feature = {'type': 'Feature',
                   'id': index,
                   'properties': {'name': geo_names[index]},
                   'geometry': {'type': gtype,
                                'coordinates': bcoords},
                   }

        geojson['features'].append(feature)
    return geojson


site_list = pd.read_csv('data/raw/sites.csv')
site_list['latitude'] = site_list['Store Name'].map({
    store_name: None if not geo_coded_sites.get(
        store_name
    ) else geo_coded_sites.get(store_name)[0]['geometry']['location']['lat']
    for store_name
    in geo_coded_sites
})
site_list['longitude'] = site_list['Store Name'].map({
    store_name: None if not geo_coded_sites.get(
        store_name
    ) else geo_coded_sites.get(store_name)[0]['geometry']['location']['lng']
    for store_name
    in geo_coded_sites
})

site_list.columns = site_list.columns.str.lower().str.replace(
    ' +', '_',
    regex=True
).str.replace(
    'unit_1',
    'unit_id'
)

site_list['vault_id'] = site_list.groupby(['store_name', 'unit_id']).ngroup()

site_list.to_pickle('data/processed/dataprocessed_site_data.pkl')

# import geopandas as gpd

# gdf = gpd.read_file('data/shape_files/zaf_admbnda_adm2_sadb_ocha_20201109.shp')
# gdf.plot()

# geojsdata = shapefile_to_geojson(gdf, list(gdf.index), geo_names_col='ADM2_EN')

# lats = site_list['latitude'].tolist()
# lons = site_list['longitude'].tolist()
# # text = gdf['label'].tolist()

# bluecart = [
#     [0.0, 'rgb(255, 255, 204)'],
#     [0.35, 'rgb(161, 218, 180)'],
#     [0.5, 'rgb(65, 182, 196)'],
#     [0.6, 'rgb(44, 127, 184)'],
#     [0.7, 'rgb(8, 104, 172)'],
#     [1.0, 'rgb(37, 52, 148)']
# ]

# choro = go.Choroplethmapbox(
#     z=gdf['ADM2_EN'].tolist(),
#     locations=gdf.index.tolist(),
#     colorscale=bluecart,  # carto
#     colorbar=dict(thickness=20, ticklen=3),
#     geojson=geojsdata,
#     text=gdf['ADM2_EN'],
#     # below=True,
#     hovertemplate='<b>Province</b>: <b>%{text}</b>' +
#                   '<br><b>Val </b>: %{z}<br>',
#     marker_line_width=0.1,
#     marker_opacity=0.7
# )
# scatt = go.Scattermapbox(
#     lat=lats,
#     lon=lons,
#     mode='markers+text',
#     # text=text,
#     # hoverinfo='none',
#     below='',
#     marker=dict(size=12, color='rgb(235, 0, 100)')
# )
# layout = go.Layout(
#     title_text='Netherlands mapbox choropleth',
#     title_x=0.5,
#     width=750,
#     height=700,
#     mapbox=dict(
#         center=dict(lat=-28, lon=26),
#         accesstoken=Config.mapbox_token,
#         zoom=4,
#         style="light"

#     )
# )

# fig = go.Figure(data=[choro, scatt], layout=layout)
# pio.renderers.default = "browser"
# fig.show()
