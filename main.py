from lib import *


# URLs to datasets needed
URL_P_INFO = "https://raw.githubusercontent.com/rmlassesen/dataset/master/p_pladser.csv"
URL_SOCECO = "https://raw.githubusercontent.com/rmlassesen/dataset/master/indkomstbruttohustype.csv"

# Assign datasets to dataframes
df_p_info = datahandler.get_dataframe(URL_P_INFO)
df_soceco = datahandler.get_dataframe(URL_SOCECO)

df_p_info['antal_pladser'] = df_p_info['antal_pladser'].apply(int)
df_soceco['HUSTANDE'] = df_soceco['HUSTANDE'].apply(int)

df_soceco = df_soceco[(df_soceco.AAR == '2014') & (df_soceco.DISTRIKTSNAVN != 'Uden for inddeling')]
df_soceco['DISTRIKTSNAVN'] = df_soceco['DISTRIKTSNAVN'].apply(helpers, normalize_area)


if __name__ == '__main__':

    p_spaces, p_spaces_by_road = analyze.number_of_p_spaces(df_p_info, 'Indre By')
    p_odd_or_even = analyze.p_spaces_odd_even(df_p_info)

    print('"Indre" By has', p_spaces, 'parking spaces.')

    print("number of parking spaces ",  p_odd_or_even)