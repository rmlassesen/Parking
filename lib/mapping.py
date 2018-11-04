from lib import helpers
import folium, webbrowser

# Chloromap, showing the average income pr. area in Copenhagen


def income_map(self):
    '''
    Createa a Chrolopleth map based on the Dataframe, showing the distribution of parking spaces pr. area
    :param df: Dataframe holding UFO statistics
    :return: HTML page as string, showing Choropleth map
    '''

    m = folium.Map(location=[55.67, 12.54], zoom_start=12)
    mapframe = helpers._income_to_int(self.income_dist_dict)

    m.choropleth(
        geo_data='cph.json',
        name='choropleth',
        data=mapframe,
        key_on='properties.navn',
        fill_color='YlOrRd',
        fill_opacity=0.5,
        line_opacity=0.5,
        legend_name='Income'
    )

    folium.LayerControl().add_to(m)

    m.save('map.html')

    # return m.get_root().render()

    webbrowser.open('map.html')

    return "HTML Map Created"

# Add markers for electric cars and private parking to the map