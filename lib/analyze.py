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


# Number of parking spaces for electric vehicles and number of private parkingspaces
def featured_spaces(df):
    spaces_by_type = df.groupby(['bydel', 'p_ordning'])['antal_pladser'].sum()
    spaces_by_status = df.groupby(['bydel', 'vejstatus'])['antal_pladser'].sum()

    electric_spaces_per_area = {}
    private_spaces_per_area = {}

    for area in areas:
        electric_spaces_per_area[area] = spaces_by_type[area]['El-Bil plads']
        private_spaces_per_area[area] = spaces_by_status[area]['Privat fællesvej']

        if 'Privat fællesvej §2 stk1' in spaces_by_status[area]:
            private_spaces_per_area[area] += spaces_by_status[area]['Privat fællesvej §2 stk1']

        if 'Privat fællessti' in spaces_by_status[area]:
            private_spaces_per_area[area] += spaces_by_status[area]['Privat fællessti']

    return electric_spaces_per_area, private_spaces_per_area



# Number of marked parking spaces in data serial
def marked_p_spaces(ds):
    pass

# Most common family constellations per area
def fam_const(df, areas):
    constellations = df.groupby(['DISTRIKTSNAVN', 'FAMILIEGRUPPE'])['HUSTAND'].sum()

    area_const_dict = {}
    for area in areas:
        area_const_dict[area] = constellations[area].sort_values(ascending=False).keys()[0]

    return area_const_dict

# Best parking opportunities for family constellations
def best_parking(df_p, df_s):
    area_const_dict = fam_const(df_s)
    spaces_by_area = df_p.groupby(['bydel'])['antal_pladser'].sum()
    spaces_by_area = spaces_by_area.sort_values(ascending=False)

    const_with_best_parking = area_const_dict[spaces_by_area.keys()[0]]
    
    return const_with_best_parking


def income_by_area(df, areas):
    incomes = df.groupby(['DISTRIKTSNAVN','INDKOMSTKATEGORI'])['HUSSTANDE'].sum()

    income_dist_dict = {}
    for area in areas:
        income_dist_dict[area] = incomes[area].mean()

    return income_dist_dict