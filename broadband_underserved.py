#Sophia Cofone, DS5010, 3/28/22
#File is intended to visualize the underserved locations

import geopandas as gpd
import matplotlib.pyplot as plt
import folium



'''Underserved'''

#underserved-subscriber-locations-2-22-layer
url_under = "https://raw.githubusercontent.com/pbogden/broadband/master/zipfiles/underserved-subscriber-locations-2-22-layer-hB7nPTjNUkTq5GppZ-zz0.zip"
#unserved-layer
url_under2 = "https://raw.githubusercontent.com/pbogden/broadband/master/zipfiles/unserved-layer-R8i8goNVLFFHfh1Xun4rj.zip"
#unserved-subscriber-loactions-2-22-layer
url_under3 = "https://raw.githubusercontent.com/pbogden/broadband/master/zipfiles/unserved-subscriber-loactions-2-22-layer-fHdE-gCVA5OAEm5DCUt2P.zip"

gdf_under = gpd.read_file(url_under)
gdf_under2 = gpd.read_file(url_under2)
gdf_under3 = gpd.read_file(url_under3)

def simple_plot_3():
    gdf0b = gdf_under.plot(color = 'blue')
    gdf_under2.plot(ax = gdf0b,color = 'red')
    final_plot = gdf_under3.plot(ax = gdf0b, color = 'yellow')
    return final_plot

simple_plot_3()
plt.show()

# NOTE THIS DOES NOT WORK, I suspect the HTML is way too large.
def folium_map_3():   
    m = folium.Map(width=600, height=400, location=[43.6591, -70.2568], control_scale=True)
    folium.GeoJson(gdf_under,style_function=lambda feature: {'color': 'blue','weight': 0.5,},name="underserved-subscriber-locations-2-22-layer").add_to(m)
    folium.GeoJson(gdf_under2,style_function=lambda feature: {'color': 'green','weight': 0.5,},name="unserved-layer").add_to(m)
    folium.GeoJson(gdf_under3,style_function=lambda feature: {'color': 'red','weight': 0.5,},name="unserved-subscriber-loactions-2-22-layer").add_to(m)
    folium.LayerControl().add_to(m)
    m.save("underserved_map.html")

#folium_map_3()