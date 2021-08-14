

# for this program we install a library called folium uising - python -m pip install folium
import folium
import pandas as pd

# this function returns a color based on the elevation of the Terrain
def color_producer(elevation):
    if elevation < 1000:
        return "green"
    elif 1000 <= elevation < 3000:
        return "orange"
    else:
        return "green"

data = pd.read_csv("Volcanoes.txt")


#----------------------------------------- Begin code
print("Welcome to mapping")

lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

#1. creating a map object.
map = folium.Map(location=[38.58, -99.09], zoom_start=6, tiles = "Stamen Terrain")

fgv = folium.FeatureGroup(name="volcanoes")#_____________________________________________ creating the object
for lt, ln, el in zip(lat, lon, elev):
    #map.add_child(folium.Marker(location=[lt,ln], popup = str(el)+" m", icon=folium.Icon(color=color_producer(el))))
    fgv.add_child(folium.CircleMarker(location=[lt,ln], radius=6, popup = str(el)+" m", color = "grey",
     fill_color=color_producer(el), fill_opacity=0.7)) # to make the icon a circle

fgp = folium.FeatureGroup(name="population")#_____________________________________________ creating the object
fgp.add_child(folium.GeoJson(data=( open("world.json", "r", encoding="utf-8-sig").read() ) ,
                            style_function = lambda x: {"fillColor": "green" if x["properties"]["POP2005"] < 10000000
                            else "yellow" if 10000000 <= x["properties"]["POP2005"] < 20000000 else "red"}))


map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())


map.save("map1.html")
