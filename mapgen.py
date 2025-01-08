import folium


def mapgen():
    m = folium.Map(location = [43,12], zoom_start = 6, tiles = "CartoDB positron")
    return (m)