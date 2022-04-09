#Sophia Cofone, DS5010, 3/28/22
#File is intended to visualize the eligible areas and the grant application data

import geopandas as gpd
import matplotlib.pyplot as plt
import folium

'''Grant'''

#eligible-areas-2-22-layer
url_elg = "https://raw.githubusercontent.com/pbogden/broadband/master/zipfiles/eligible-areas-2-22-layer-G8qemhB46k7dh-m1XZ2JM.zip"
#grant-applications-layer
url_grant = "https://raw.githubusercontent.com/pbogden/broadband/master/zipfiles/grant-applications-layer-o-xxbSzyTNCM52P_VsBxG.zip"

gdf_elg = gpd.read_file(url_elg)
gdf_grant = gpd.read_file(url_grant)

def simple_plot_2():
    gdf0b = gdf_elg.plot(color = 'blue')
    final_plot = gdf_grant.plot(ax = gdf0b, color = 'yellow')
    return final_plot

simple_plot_2()
plt.show()

def folium_map_2():   
    m = folium.Map(width=600, height=400, location=[43.6591, -70.2568], control_scale=True)
    folium.GeoJson(gdf_elg,style_function=lambda feature: {'color': 'blue','weight': 0.5,},name="eligible-areas-2-22-layer").add_to(m)
    folium.GeoJson(gdf_grant,style_function=lambda feature: {'color': 'green','weight': 0.5,},name="grant-applications-layer").add_to(m)
    folium.LayerControl().add_to(m)
    m.save("grant_map.html")

folium_map_2()