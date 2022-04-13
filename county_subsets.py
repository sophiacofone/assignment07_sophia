#Sophia Cofone, DS5010, 4/10/22
#File is intended to 

import geopandas as gpd
import folium
import matplotlib.pyplot as plt
import rtree
from shapely.geometry import Point
from geopandas import datasets, GeoDataFrame, read_file

'''
references
https://geopandas.org/en/stable/gallery/spatial_joins.html#Spatial-Joins-between-two-GeoDataFrames
'''

"""DATA"""
'''Counties'''
urlcounties = "https://raw.githubusercontent.com/PhilipMathieu/maine-counties/main/Maine_County_Boundary_Polygons_Dissolved_Feature.geojson"
'''Tier 4-5'''
urlt4 = "https://raw.githubusercontent.com/pbogden/broadband/master/zipfiles/tier-4-50-10-100-100-layer--pCgIFfvOkurYcKDZ1Db7.zip"
urlt5 = "https://raw.githubusercontent.com/pbogden/broadband/master/zipfiles/tier-5-100-m-layer-zo2lbPrGRte_B5Ug-kEqS.zip"
'''Underserved/Unserved'''
#underserved-subscriber-locations-2-22-layer - THERE IS A PROBLEM HERE, UNSURE WHY
#url_under = "https://raw.githubusercontent.com/pbogden/broadband/master/zipfiles/underserved-subscriber-locations-2-22-layer-hB7nPTjNUkTq5GppZ-zz0.zip"
#unserved-layer
url_un1 = "https://raw.githubusercontent.com/pbogden/broadband/master/zipfiles/unserved-layer-R8i8goNVLFFHfh1Xun4rj.zip"
#unserved-subscriber-loactions-2-22-layer
url_un2 = "https://raw.githubusercontent.com/pbogden/broadband/master/zipfiles/unserved-subscriber-loactions-2-22-layer-fHdE-gCVA5OAEm5DCUt2P.zip"

def create_gdf(url):
    gdf = gpd.read_file(url)
    return gdf

def select_county(county_name):
    gdf_counties = create_gdf(urlcounties)
    county = gdf_counties.loc[gdf_counties['COUNTY'] == county_name]
    return county

def subset_broadband_gdf(county_name,broadband_data_url):
    filt_county_gdf = select_county(county_name)
    broadband_gdf = create_gdf(broadband_data_url)
    broadband_gdf.crs = filt_county_gdf.crs
    join_inner_gdf = broadband_gdf.sjoin(filt_county_gdf, how="inner")
    
    return join_inner_gdf

def simple_plot(county_name,broadband_data_url):
    join_inner_gdf = subset_broadband_gdf(county_name,broadband_data_url)
    join_inner_gdf.plot()

def layer_plot(county_name,broadband_data_url,broadband_data_url2,broadband_data_url3):
    join_inner_gdf = subset_broadband_gdf(county_name,broadband_data_url)
    join_inner_gdf2 = subset_broadband_gdf(county_name,broadband_data_url2)
    join_inner_gdf3 = subset_broadband_gdf(county_name,broadband_data_url3)

    base_layer = join_inner_gdf.plot(color = 'blue')
    join_inner_gdf2.plot(ax = base_layer,color = 'red')
    final_plot = join_inner_gdf3.plot(ax = base_layer, color = 'green')

    return final_plot

#simple_plot('Oxford',url_un1)
#layer_plot('Oxford',urlt4,urlt5,url_un1)
#plt.show()

def single_folium_map(county_name,broadband_data_url):   
    m = folium.Map(width=600, height=400, location=[43.6591, -70.2568], control_scale=True)
   
    join_inner_gdf = subset_broadband_gdf(county_name,broadband_data_url)
   
    folium.GeoJson(join_inner_gdf,style_function=lambda feature: {'color': 'blue','weight': 0.5,},name="underserved-subscriber-locations-2-22-layer").add_to(m)
    m.save("single_map.html")

def layer_folium_map(county_name,broadband_data_url,broadband_data_url2,broadband_data_url3):   
    m = folium.Map(width=600, height=400, location=[43.6591, -70.2568], control_scale=True)
    
    join_inner_gdf = subset_broadband_gdf(county_name,broadband_data_url)
    join_inner_gdf2 = subset_broadband_gdf(county_name,broadband_data_url2)
    join_inner_gdf3 = subset_broadband_gdf(county_name,broadband_data_url3)

    folium.GeoJson(join_inner_gdf,style_function=lambda feature: {'color': 'blue','weight': 0.5,},name="underserved-subscriber-locations-2-22-layer").add_to(m)
    folium.GeoJson(join_inner_gdf2,style_function=lambda feature: {'color': 'green','weight': 0.5,},name="unserved-layer").add_to(m)
    folium.GeoJson(join_inner_gdf3,style_function=lambda feature: {'color': 'red','weight': 0.5,},name="unserved-subscriber-loactions-2-22-layer").add_to(m)
    folium.LayerControl().add_to(m)
    
    m.save("layer_map.html")

#single_folium_map('Oxford',url_un1)
layer_folium_map('Oxford',urlt4,urlt5,url_un1)