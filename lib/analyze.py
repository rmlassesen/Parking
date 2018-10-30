import pandas as pd
# Number of parking spaces in an area.
def number_of_p_spaces(df, area):
    data = df[df.bydel == area]
    gb = data.groupby(['antal_pladser', 'vejnavn']).sort_values()
    return 
    pass

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
    pass

# Best parking opportunities for family constellations
def best_parking(df_p, df_s):
    #fam_const(df_p)
    #number_of_p_spaces(df_s)
    pass