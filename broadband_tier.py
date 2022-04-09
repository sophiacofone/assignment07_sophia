#Sophia Cofone, DS5010, 3/28/22
#File is intended to visualize tier 0-5 of the broadband data

'''references:
https://stackoverflow.com/questions/60358344/json-file-does-not-load-on-a-folium-map
https://geopandas.org/en/stable/docs/user_guide/mapping.html
https://python-visualization.github.io/folium/quickstart.html#GeoJSON/TopoJSON-Overlays
'''

import geopandas as gpd
import folium
import matplotlib as plt


'''TIER 0-5'''

urlt0 = "https://raw.githubusercontent.com/pbogden/broadband/master/zipfiles/tier-0-no-address-range-layer-jLQPM-g3RfNthOkroK_Mf.zip"
urlt1 = "https://raw.githubusercontent.com/pbogden/broadband/master/zipfiles/tier-1-0-10-1-layer-2Vbn3XwU7ghduyFrvsX3i.zip"
urlt2 = "https://raw.githubusercontent.com/pbogden/broadband/master/zipfiles/tier-2-10-1-25-3-layer-8lhS3piFE8p5Sof4IZ4C0.zip"
urlt3 = "https://raw.githubusercontent.com/pbogden/broadband/master/zipfiles/tier-3-25-3-50-10-layer-axu8CkkozyfVxf5kjgcSY.zip"
urlt4 = "https://raw.githubusercontent.com/pbogden/broadband/master/zipfiles/tier-4-50-10-100-100-layer--pCgIFfvOkurYcKDZ1Db7.zip"
urlt5 = "https://raw.githubusercontent.com/pbogden/broadband/master/zipfiles/tier-5-100-m-layer-zo2lbPrGRte_B5Ug-kEqS.zip"

gdf0 = gpd.read_file(urlt0)
gdf1 = gpd.read_file(urlt1)
gdf2 = gpd.read_file(urlt2)
gdf3 = gpd.read_file(urlt3)
gdf4 = gpd.read_file(urlt4)
gdf5 = gpd.read_file(urlt5)


def simple_plot():
    gdf0b = gdf0.plot(color = 'blue')
    gdf1.plot(ax = gdf0b,color = 'red')
    gdf2.plot(ax = gdf0b,color = 'green')
    gdf3.plot(ax = gdf0b,color = 'purple')
    gdf4.plot(ax = gdf0b,color = 'orange')
    final_plot = gdf5.plot(ax = gdf0b, color = 'yellow')
    return final_plot

simple_plot()
plt.pyplot.show()

def folium_teir_map():   
    m = folium.Map(width=600, height=400, location=[43.6591, -70.2568], control_scale=True)
    folium.GeoJson(gdf0,style_function=lambda feature: {'color': 'blue','weight': 0.5,},name="tier0").add_to(m)
    folium.GeoJson(gdf1,style_function=lambda feature: {'color': 'red','weight': 0.5,},name="tier1").add_to(m)
    folium.GeoJson(gdf2,style_function=lambda feature: {'color': 'green','weight': 0.5,},name="tier2").add_to(m)
    folium.GeoJson(gdf3,style_function=lambda feature: {'color': 'purple','weight': 0.5,},name="tier3").add_to(m)
    folium.GeoJson(gdf4,style_function=lambda feature: {'color': 'orange','weight': 0.5,},name="tier4").add_to(m)
    folium.GeoJson(gdf5,style_function=lambda feature: {'color': 'yellow','weight': 0.5,},name="tier5").add_to(m)
    folium.LayerControl().add_to(m)
    m.save("tier_map_all_layer.html")


folium_teir_map()
