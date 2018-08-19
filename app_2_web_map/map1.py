import folium
import pandas

data = pandas.read_csv("Volcanoes_USA.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])


def color_producer(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'


map = folium.Map([38.4259014, -99.3664178],
                 zoom_start=6, tiles="Mapbox Bright")

fgv = folium.FeatureGroup("Volcanoes")

# for current_lat, current_lon, current_elev in zip(lat, lon, elev):
#     fg.add_child(folium.Marker(location=[current_lat, current_lon], popup=str(
#         current_elev) + " m", icon=folium.Icon(color_producer(current_elev))))

for current_lat, current_lon, current_elev in zip(lat, lon, elev):
    fgv.add_child(folium.CircleMarker(location=[current_lat, current_lon], radius=6, popup=str(
        current_elev) + " m", fill=True, fill_opacity = 0.7, fill_color=color_producer(current_elev)))

fgp = folium.FeatureGroup("Population")

fgp.add_child(folium.GeoJson(data=open("world.json", encoding="utf-8-sig").read(), style_function=lambda x: {'fillColor':'green' if x["properties"]["POP2005"] < 10000000
else "orange" if x["properties"]["POP2005"] < 20000000 else "red"}))

map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())

map.save("Map1.html")
