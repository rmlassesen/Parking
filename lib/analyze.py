import pandas as pd

# Number of parking spaces in an area.
def number_of_p_spaces(df, area):
    data = df[df.bydel == area]
    gb = data.groupby(['antal_pladser', 'vejnavn']).sort_values()

    return data, gb

# Number of parking spaces per road name
def p_spaces_per_road(df):
    pass

# Number of parking spaces by odd and even house numbers
def p_spaces_odd_even(df):
    most_Lige = df[df.vejside == 'Lige husnr.']
    most_ulige = df[df.vejside == 'Ulige husnr.']

    return 'Lige husnr {}'.format(len(most_Lige)) , 'Ulige husnr {}'.format(len(most_ulige))
    


# Number of marked parking spaces in data serial
def marked_p_spaces(ds):
    pass

# Most common family constellations per area
def fam_const(df):
    constellations = df.groupby(['DISTRIKTSNAVN', 'FAMILIEGRUPPE']).size()

    areas = set()
    for area, value in constellations.iteritems():
        areas.add(area[0])

    area_const_dict = {}
    for area in areas:
        area_const_dict[area] = constellations[area].sort_values(ascending=False).keys()[0]

    return areas, area_const_dict

# Best parking opportunities for family constellations
def best_parking(df_p, df_s):
    _, area_const_dict = fam_const(df_s)
    spaces_by_area = df_p.groupby(['bydel'])['antal_pladser'].sum()
    spaces_by_area = spaces_by_area.sort_values(ascending=False)

    const_with_best_parking = area_const_dict[spaces_by_area.keys()[0]]

    return const_with_best_parking