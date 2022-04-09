#Sophia Cofone, DS5010, 3/28/22
#File is intended to visualize the served locations vs the underserved locations


import geopandas as gpd
import matplotlib.pyplot as plt
import folium



'''May be underserved'''

#served-subscirber-locations-2-22-layer
url_served = "https://raw.githubusercontent.com/pbogden/broadband/master/zipfiles/served-subscirber-locations-2-22-layer-9a3JpnMadKDLj_zPqDCkv.zip"
#density-of-unserved-may-be-layer
url_den_may_under= "https://raw.githubusercontent.com/pbogden/broadband/master/zipfiles/density-of-unserved-may-be-layer-UKtUhvoEC95KBH6HsnWIU.zip"
#may-be-unserved-layer
url_may_under = "https://raw.githubusercontent.com/pbogden/broadband/master/zipfiles/may-be-unserved-layer-gpC0SCaV9wS6W-zZCePjz.zip"


gdf_served = gpd.read_file(url_served)
gdf_den_may = gpd.read_file(url_den_may_under)
gdf_may_under = gpd.read_file(url_may_under)

def simple_plot_4():
    gdf0b = gdf_served.plot(color = 'blue')
    gdf_den_may.plot(ax = gdf0b,color = 'red')
    final_plot = gdf_may_under.plot(ax = gdf0b, color = 'yellow')

    return final_plot

simple_plot_4()
plt.show()


# NOTE THIS DOES NOT WORK, I suspect the HTML is way too large.
def folium_map_4():   
    m = folium.Map(width=600, height=400, location=[43.6591, -70.2568], control_scale=True)
    folium.GeoJson(gdf_served,style_function=lambda feature: {'color': 'blue','weight': 0.5,},name="served-subscirber-locations-2-22-layer").add_to(m)
    folium.GeoJson(gdf_den_may,style_function=lambda feature: {'color': 'green','weight': 0.5,},name="density-of-unserved-may-be-layer").add_to(m)
    folium.GeoJson(gdf_may_under,style_function=lambda feature: {'color': 'red','weight': 0.5,},name="may-be-unserved-layer").add_to(m)
    folium.LayerControl().add_to(m)
    m.save("may_underserved_map.html")

#folium_map_4()