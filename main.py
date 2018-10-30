from lib import analyze, datahandler


# URLs to datasets needed
URL_P_INFO = "https://raw.githubusercontent.com/rmlassesen/dataset/master/p_pladser.csv"
URL_SOCECO = "https://raw.githubusercontent.com/rmlassesen/dataset/master/indkomstbruttohustype.csv"

# Assign datasets to dataframes
df_p_info = datahandler.get_dataframe(URL_P_INFO)
df_soceco = datahandler.get_dataframe(URL_SOCECO)



if __name__ == '__main__':

    p_spaces = analyze.number_of_p_spaces(df_p_info, 'Indre By')
    p_odd_or_even = analyze.p_spaces_odd_even(df_p_info)
    print('"Indre" By has', p_spaces, 'parking spaces.')
    #print("number of parking spaces ",  p_odd_or_even)